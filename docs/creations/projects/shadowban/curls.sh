#!/bin/bash

curl https://twitter.com/verified/lists/verified-accounts/members?lang=en > tempcurl.txt

infile="./tempcurl.txt"

python3 createuserlist.py


