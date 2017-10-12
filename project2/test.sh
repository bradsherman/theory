#!/bin/bash

# script to test the DPDA for project 2

machine=( "M1" "M2" "M2-v2" "M3" "Mystery" "MyMachine" )
if [[ $# -ne 0 ]]
then
    machine=( $1 )
fi

for m in "${machine[@]}"
do
    if [[ $m == "Mystery" ]]
    then
        ./dpda.py < "${m}-test.txt"
    else
        ./dpda.py < "${m}-test-accept.txt"
        ./dpda.py < "${m}-test-reject.txt"
    fi
done
