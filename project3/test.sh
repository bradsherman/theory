#!/bin/bash

# script to test the TM for project 3

machine=( "M1" "M2" "M3" "Mystery" "MyMachine" )
if [[ $# -ne 0 ]]
then
    machine=( $1 )
fi

for m in "${machine[@]}"
do
    if [[ $m == "M1" || $m == "MyMachine" ]]
    then
        ./tm.py < "${m}-test-accept.txt"
        ./tm.py < "${m}-test-reject.txt"
    else
        ./tm.py < "${m}-test.txt"
    fi
done
