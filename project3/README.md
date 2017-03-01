Project 03
==========

There is no need to compile the program since it is a Python script. The program
works by first reading in the filename of the file defining the rules of the tm,
and then the filename containing the strings to be tested. To make this process
easier, I have text files that contain the names of the machine rules files and
strings files, so that just that files can be piped into standard input when the
program is run. For example, to run the strings that should be accepted by M1,
just run:

    ./tm.py < M1-test-accept.txt

This is an easy way to run the program with multiple different inputs because
M1-test-accept.txt contains "M1.txt" and "M1-Accept.txt". This same convention
is applied to the other machines, and for machines that perform computations
there is only one strings file so there is only one file needed to test instead
of having an accept or reject file.

I also wrote a script to test the program against all possible machines and
inputs. It can be run using the following command:

    ./test.sh [machine]

If no command line arguments are passed the script will test all machines. An
output dump of the simulator running against all test machines can be found in
the output file.

MyMachine is a Turing Machine that only accepts string with an equal number of
0s and 1s.
