#!/bin/bash

kf=$(cat answer.txt)
echo "${kf}" > /tmp/plain.key; xxd -r -p /tmp/plain.key > /tmp/enc.key
