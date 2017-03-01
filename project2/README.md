Project 02
==========

There is no need to compile the program since it is a Python script. The program
works by first reading in the filename of the file defining the rules of the
dpda, and then the filename containing the strings to be tested. To make this
process easier, I have text files that contain the names of machine rules files
and strings files, so that just that file can be piped into standard input when
the program is run, and it will automatically read in the contents. For example,
to run the strings that should be accepted by M1, just run:

    ./dpda.py < M1-test-accept.txt

This is an easy way to run the program with multiple different inputs because
M1-test-accept.txt contains "M1.txt" on the first line and "M1-Accept.txt" on
the second line. This same convention is applied to all the other machines. The
output dump of the program running against all machines can be found in the file
name "output".

I also wrote a script to test the program against all possible machines and
inputs. It can be run using the following command:

    ./test.sh [machine]

If no command line arguments are passed the script will test all machines.

*Note*: M2 and M2-v2 are the same except "ac" is in accept for M2 and reject for
M2-v2. I was under the impression that if the stack is not empty when the input
is done, then even if the machine is in the accept state, we would not accept
the string, so in that case ac would not be accepted (which makes sense because
it is not a palindrome). In either case, the only difference in the program
would be adding a "len(stack) == 0" to the if statement before printing accepted
at the end of the program.
