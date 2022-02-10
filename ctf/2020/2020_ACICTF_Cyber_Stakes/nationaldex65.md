## [100] National Dex #65 (Reverse Engineering)

### Prompt:
We found the encryptor (encrypt) but it won't decrypt encrypted?

### Initial Analysis:
Fire up gdb and disassemble the main function:

```
$gdb -q ./encrypt
Reading symbols from ./encrypt...
(No debugging symbols found in ./encrypt)
(gdb) disas main
Dump of assembler code for function main:
...
   0x0000000000400dc5 <+218>:   callq  0x401ba0 <BF_set_key>
   0x0000000000400dca <+223>:   lea    -0x30(%rbp),%rcx
--Type <RET> for more, q to quit, c to continue without paging--c
   0x0000000000400dce <+227>:   mov    -0x108c(%rbp),%eax
   0x0000000000400dd4 <+233>:   mov    $0x10,%edx
   0x0000000000400dd9 <+238>:   mov    %rcx,%rsi
   0x0000000000400ddc <+241>:   mov    %eax,%edi
   0x0000000000400dde <+243>:   callq  0x44ae60 <read>
   0x0000000000400de3 <+248>:   mov    %eax,-0x1084(%rbp)
   0x0000000000400de9 <+254>:   cmpl   $0x0,-0x1084(%rbp)
   0x0000000000400df0 <+261>:   jle    0x400e96 <main+427>
   0x0000000000400df6 <+267>:   mov    -0x1084(%rbp),%eax
   0x0000000000400dfc <+273>:   movslq %eax,%rdx
   0x0000000000400dff <+276>:   lea    -0x30(%rbp),%rax
   0x0000000000400e03 <+280>:   mov    %rdx,%rsi
   0x0000000000400e06 <+283>:   mov    %rax,%rdi
   0x0000000000400e09 <+286>:   callq  0x400b4d <hexdump>
   0x0000000000400e0e <+291>:   mov    -0x1084(%rbp),%eax
   0x0000000000400e14 <+297>:   movslq %eax,%rdx
   0x0000000000400e17 <+300>:   lea    -0x1080(%rbp),%rcx
   0x0000000000400e1e <+307>:   lea    -0x20(%rbp),%rsi
   0x0000000000400e22 <+311>:   lea    -0x30(%rbp),%rax
   0x0000000000400e26 <+315>:   mov    $0x1,%r9d
   0x0000000000400e2c <+321>:   lea    0x2bb2bd(%rip),%r8        # 0x6bc0f0 <GLOBAL1>
   0x0000000000400e33 <+328>:   mov    %rax,%rdi
   0x0000000000400e36 <+331>:   callq  0x401670 <BF_cbc_encrypt>
...
```

Two functions jump out: <BF_set_key> and <BF_cbc_encrypt>.  Now, we _could_ get bogged down in trying to crypto-smash the CBC, but let's investigate further to see if we can manipulate the program to give us what we want.

```
(gdb) disas BF_cbc_encrypt
...
   0x000000000040181c <+428>:   callq  0x4012a0 <BF_decrypt>
...
```

Awesome!  We found a decrypt function already built into the program!  Although we find many instances of <BF_encrypt> and <BF_decrypt>, we're more concerned about decrypting, so let's investigate how to get the program to run <BF_decrypt> on our input file.

### Solution:
Let's start by setting some pretty simple breakpoints at the entryways for each stage of the program related to the <BF_cbc_encrypt> function.  Remember, we want to force the information down the decryption path, so if you trace the <BF_decrypt> back to the beginning of its parent function, the path looks like this (it was my preference to take the address before each of the jumps):

```
(gdb) break *0x4016b0
Breakpoint 1 at 0x4016b0
(gdb) break *0x4017b0
Breakpoint 2 at 0x4017b0
(gdb) break *0x401876
Breakpoint 3 at 0x401876
(gdb) break *0x4018A6
Breakpoint 4 at 0x4018a6
```

In each of these locations, the way to force the <BF_cbc_encrypt> to follow the decryption path is to modify the eflags at each of the breakpoints.

Without knowing how the file "encrypted" was encrypted, we can still use trial and error to find the eflags modification sequence that outputs the correct flag.  In our case, we're going to carefully switch the ZERO flag (ZF, value = 0x0040) on and off.  This is demonstrated below (flag redacted):

```
(gdb) run encrypted demo.txt
Starting program: /home/kali/Documents/acictf/nationaldex65/encrypt encrypted demo.txt
B7 10 4B 89 1E D7 A8 77  63 7E 65 B3 56 67 B7 D4  |  ..K....wc~e.Vg.. 

Breakpoint 1, 0x00000000004016b0 in BF_cbc_encrypt ()
(gdb) set $eflags = 0x242
(gdb) c
Continuing.

Breakpoint 2, 0x00000000004017b0 in BF_cbc_encrypt ()
(gdb) set $eflags = 0x202
(gdb) c
Continuing.

Breakpoint 3, 0x0000000000401876 in BF_cbc_encrypt ()
(gdb) c
Continuing.

Breakpoint 3, 0x0000000000401876 in BF_cbc_encrypt ()
(gdb) set $eflags = 0x242
(gdb) c
Continuing.

Breakpoint 4, 0x00000000004018a6 in BF_cbc_encrypt ()
(gdb) set $eflags = 0x202
(gdb) c
Continuing.
00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |  ACI{readactedred 

5E EC F1 22 42 AE DB B4  73 32 BA 30 65 3C 56 64  |  ^.."B...s2.0e<Vd 

Breakpoint 1, 0x00000000004016b0 in BF_cbc_encrypt ()
(gdb) set $eflags = 0x242
(gdb) c
Continuing.

Breakpoint 2, 0x00000000004017b0 in BF_cbc_encrypt ()
(gdb) set $eflags = 0x202
(gdb) c
Continuing.

Breakpoint 3, 0x0000000000401876 in BF_cbc_encrypt ()
(gdb) c
Continuing.

Breakpoint 3, 0x0000000000401876 in BF_cbc_encrypt ()
(gdb) set $eflags = 0x242
(gdb) c
Continuing.

Breakpoint 4, 0x00000000004018a6 in BF_cbc_encrypt ()
(gdb) set $eflags = 0x202
(gdb) c
Continuing.
00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |  actedredactedre} 
```

eflags --> ACIflag!

END
