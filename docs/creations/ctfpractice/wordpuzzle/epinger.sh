#!/bin/bash

a=0;

while [ True ]; do
	for i in {1..254}; do
		ping -c 1 10.0.0.${i} 2>&1;
	done;
done
