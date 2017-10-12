#!/usr/bin/env python
# Brad Sherman
# CSE 30151
# Project 3

import sys


# function to easily print out current state of machine
def print_state(step, currentTapeHead, tape, currentState):
    sys.stdout.write(str(step) + "@" + str(currentTapeHead) + "#")
    for i in range(0, currentTapeHead):
        sys.stdout.write(tape[i])

    sys.stdout.write(currentState)

    for i in range(currentTapeHead, len(tape)):
        sys.stdout.write(tape[i])
    sys.stdout.write("\n")
    sys.stdout.flush()

if __name__ == "__main__":
    # Read in rules/strings file from stdin
    tmFile = raw_input()
    stringsFile = raw_input()

    with open(tmFile, "r") as tmFd:
        tmDef = tmFd.read()

    if "\r\n" in tmDef:
        tmDefList = tmDef.rstrip().split("\r\n")
    else:
        tmDefList = tmDef.rstrip().split("\n")

    tmName = tmDefList[0]
    tmAlph = tmDefList[1].split(",")
    tmTape = tmDefList[2].split(",")
    # add items to tape alphabet from input alphabet if not already in it
    for item in tmAlph:
        if item not in tmTape:
            tmTape.append(item)
    tmStates = tmDefList[3].split(",")
    tmStart = tmDefList[4].split()
    tmAccept = tmDefList[5].split(",")
    tmReject = tmDefList[6].split(",")
    tmTransitions = {}

    headLength = len(tmName) if len(tmName) > len(stringsFile) else \
        len(stringsFile)

    print ""
    print tmName
    print stringsFile
    print "=" * headLength
    print ""
    print "Transition Rules"
    print "----------------"

    ruleNum = 1  # Keep track of rule numbers
    for line in tmDefList[7:]:
        # Rest are transition rules
        trans = line.split("|")
        initial = trans[0].split(",")
        initialState = initial[0]
        initialTapeSymbol = initial[1]
        new = trans[1].split(",")
        newState = new[0]
        newTapeSymbol = new[1]
        direction = new[2]

        tmTransitions[initialState, initialTapeSymbol] = [
                newState,
                newTapeSymbol,
                direction,
                ruleNum]
        print "Rule " + str(ruleNum) + ": " + str(initialState) + ", " + \
            str(initialTapeSymbol) + " ==> " + str(newState) + ", " + \
            str(newTapeSymbol) + ", " + str(direction)
        ruleNum += 1

    with open(stringsFile, "r") as stringsFd:
        tmInput = stringsFd.read()

    tmInList = tmInput.rsplit()

    for string in tmInList:
        print "\nString: " + string
        # initialize variables
        tape = []
        currentState = tmStart[0]
        currentTapeSymbol = ""
        nextState = ""
        nextTapeSymbol = ""
        direction = ""
        blank = "_"
        step = 1
        ruleNum = 0
        currentTapeHead = 0
        # set tape
        for index in range(0, len(string)):
            tape.append(string[index])

        while currentState not in tmAccept and currentState not in tmReject:
            # append a blank if we've reached the end of the tape
            if currentTapeHead >= len(tape):
                tape.append(blank)
            currentTapeSymbol = tape[currentTapeHead]

            # check to see if we have a valid transition rule
            if (currentState, currentTapeSymbol) in tmTransitions:
                nextState, nextTapeSymbol, direction, ruleNum = \
                    tmTransitions[currentState, currentTapeSymbol]
            else:
                break

            # make sure tape symbol is valid
            if nextTapeSymbol not in tmTape:
                break

            # print current state of the machine
            print_state(step, currentTapeHead, tape, currentState)

            # update values based on transition rule
            tape[currentTapeHead] = nextTapeSymbol
            currentTapeHead += 1
            if direction == "L":
                if currentTapeHead == 1:
                    currentTapeHead = 0
                else:
                    currentTapeHead -= 2

            currentState = nextState

            step += 1

        print_state(step, currentTapeHead, tape, currentState)
        if currentState in tmAccept:
            print "Accepted"
        else:
            print "Rejected"
