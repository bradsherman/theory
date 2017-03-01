Project 01
==========

There is no need to compile the program since it is a Python script. The program
works by first reading in the filename of the file defining rules of a dfa, and
then the filename containing the strings to be tested. To make this process
easier, I have text files that contain the names of machine rules files and
strings files, so that just that file can be piped into standard in when the
program is run, and it will automatically read in the contents. For example, to
run the strings that should be accepted by M1, just run:

    ./dfa.py < m1accept

This is an easy way to run the program with multiple different inputs because
m1accept contains "M1.txt" on the first line and "M1-Accept.txt" on the second
line. This same convention is applied to all the other machines. The output dump
of the program running against machines M1-M3, the mystery machine, and my
machine can be found in the file named "output."

I also wrote a script to test the program against all possible machines and
inputs. It can be run using the following command:

    ./test_all.sh
