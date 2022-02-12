#!/bin/bash

for i in {1..10000}; do
	nc 172.31.1.1 5353 &
done
