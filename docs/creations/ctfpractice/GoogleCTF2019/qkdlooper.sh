#!/bin/bash

i=0
while ($i -ne 1000); do
	echo "ITERATION # ${i}"
	python3 qkd.py
	sleep 60
	./makekey.sh
	sleep 5
	./decode.sh
	sleep 5
	((i++))
done
