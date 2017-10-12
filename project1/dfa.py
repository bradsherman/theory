#!/usr/bin/env python
# Brad Sherman
# CSE 30151
# Project 1

if __name__ == "__main__":
    # Read in rules/strings file from stdin
    dfaFile = raw_input()
    stringsFile = raw_input()

    with open(dfaFile, "r") as dfaFd:
        dfaDef = dfaFd.read()

    if "\r\n" in dfaDef:
        dfaDefList = dfaDef.rstrip().split("\r\n")
    else:
        dfaDefList = dfaDef.rstrip().split("\n")

    dfaName = dfaDefList[0]
    dfaAlph = dfaDefList[1].split(",")
    dfaStates = dfaDefList[2].split(",")
    dfaStart = dfaDefList[3].split()
    dfaAccept = dfaDefList[4].split(",")
    dfaTransitions = {}

    headLength = len(dfaName) if len(dfaName) > len(stringsFile) else \
        len(stringsFile)

    print ""
    print dfaName
    print stringsFile
    print "=" * headLength
    print ""
    print "Transition Rules"
    print "----------------"

    ruleNum = 1  # Keep track of rule numbers
    for line in dfaDefList[5:]:
        # Rest are transition rules
        trans = line.split(",")
        initialState = trans[0]
        inputChar = trans[1]
        endState = trans[2]
        dfaTransitions[initialState, inputChar] = [endState, ruleNum]
        print "Rule " + str(ruleNum) + ": " + str(initialState) + ", " + \
            str(inputChar) + ", " + str(endState)
        ruleNum += 1

    with open(stringsFile, "r") as stringsFd:
        dfaInput = stringsFd.read()

    dfaInList = dfaInput.rsplit()

    for string in dfaInList:
        print "\nString: " + string
        currentState = dfaStart[0]
        nextState = ""
        step = 1
        ruleNum = 0
        for index in range(0, len(string)):
            currentInput = string[index]
            if currentInput not in dfaAlph:
                break
            try:
                nextState, rule = dfaTransitions[currentState, currentInput]
            except KeyError:
                break
            print "Step: " + str(step) + " Rule #" + str(rule) + ": " + \
                str(currentState) + ", " + str(currentInput) + ", " + \
                str(nextState)
            currentState = nextState
            step += 1

        if currentState in dfaAccept:
            print "Accepted"
        else:
            print "Rejected"
