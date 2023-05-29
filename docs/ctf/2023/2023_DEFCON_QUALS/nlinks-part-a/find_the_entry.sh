#!/bin/bash

for filename in $(ls); do
	echo ${filename};
	timeout 1 ./${filename} | grep -v Passphrase
done
