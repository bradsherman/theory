#!/usr/bin/env python
# Brad Sherman
# CSE 30151
# Project 1

if __name__ == "__main__":
    # Read in rules/strings file from stdin
    dpdaFile = raw_input()
    stringsFile = raw_input()

    with open(dpdaFile, "r") as dpdaFd:
        dpdaDef = dpdaFd.read()

    if "\r\n" in dpdaDef:
        dpdaDefList = dpdaDef.rstrip().split("\r\n")
    else:
        dpdaDefList = dpdaDef.rstrip().split("\n")

    # Name of machine
    dpdaName = dpdaDefList[0]
    # Input Alphabet
    dpdaInputAlph = dpdaDefList[1].split(",")
    # Stack Alphabet
    dpdaStackAlph = dpdaDefList[2].split(",")
    # States
    dpdaStates = dpdaDefList[3].split(",")
    # Start State
    dpdaStart = dpdaDefList[4].split()
    # Accept States
    dpdaAccept = dpdaDefList[5].split(",")
    # Transitions dictionary
    dpdaTransitions = {}

    # length of equal sign line under machine name and strings file name
    headLength = len(dpdaName) if len(dpdaName) > len(stringsFile) else \
        len(stringsFile)

    print ""
    print dpdaName
    print stringsFile
    print "=" * headLength
    print ""
    print "Transition Rules"
    print "----------------"

    ruleNum = 1  # Keep track of rule numbers
    for line in dpdaDefList[6:]:
        # | splits transitions by before/after operation
        trans = line.split("|")
        # initial conditions of machine
        initial = trans[0]
        # state, char, and stack top are separated by a comma
        initialInfo = initial.split(",")
        initialState = initialInfo[0]
        inputChar = initialInfo[1]
        stackTop = initialInfo[2]
        # post conditions of machine after transition
        new = trans[1]
        # state, char, and stack top are separated by a comma
        newInfo = new.split(",")
        newState = newInfo[0]
        newStackTop = newInfo[1]
        # add rule to the dictionary
        dpdaTransitions[initialState, inputChar, stackTop] = \
            [newState, newStackTop, ruleNum]
        # print rule
        print "Rule " + str(ruleNum) + ": " + str(initialState) + ", " + \
            str(inputChar) + ", " + str(stackTop) + " ==> " + str(newState) + \
            ", " + str(newStackTop)
        ruleNum += 1

    with open(stringsFile, "r") as stringsFd:
        dpdaInput = stringsFd.read()

    dpdaInList = dpdaInput.rsplit()

    for string in dpdaInList:
        print "\nString: " + string
        # initialize variables
        currentState = dpdaStart[0]
        epsilon = "~"
        # stack top of "None" signifies empty stack
        currentStackTop = None
        nextState = ""
        nextStackTop = ""
        step = 1
        rule = 0
        # use a list as a stack with append (push) and pop as operations
        stack = []
        # ruleInput and ruleStackTop are used to display the rule to the user
        # so that the actual input/stack top and what rule is used is separated
        ruleInput = ""
        ruleStackTop = ""
        # variable to keep track of which char is our input
        index = 0
        while True:
            '''
                typeCounter is a counter used to see what kind of transition
                we used. It translates to the following
                0: not a valid combination (error)
                1: epsilon-epsilon rule
                2: input independent transition
                3: stack independent transition
                4: input and stack dependent transition
            '''
            typeCounter = 4
            # get current char, checking to make sure we are in bounds
            if index >= len(string):
                break
            currentInput = string[index]
            # make sure it is a valid char
            if currentInput not in dpdaInputAlph:
                break

            # for each of the try/excepts below, try to see if the rule is in
            # the dictionary of transitions, if it is not, we decrement the
            # typeCounter variable and try adding epsilons in the rule
            # the if statement before the 2-4 try/except is to make sure it
            # only runs if the typeCounter has been decremented the appropriate
            # amount of times

            # case where the specific input and top of stack matter
            try:
                nextState, nextStackTop, rule = dpdaTransitions[
                        currentState,
                        currentInput,
                        currentStackTop]
            except KeyError:
                typeCounter -= 1

            # case where only current input matters
            if typeCounter == 3:
                try:
                    nextState, nextStackTop, rule = dpdaTransitions[
                            currentState,
                            currentInput,
                            epsilon]
                except KeyError:
                    typeCounter -= 1

            # case where only top of stack matters
            if typeCounter == 2:
                try:
                    nextState, nextStackTop, rule = dpdaTransitions[
                            currentState,
                            epsilon,
                            currentStackTop]
                except KeyError:
                    typeCounter -= 1

            # case where neither input or top of stack matters
            if typeCounter == 1:
                try:
                    nextState, nextStackTop, rule = dpdaTransitions[
                            currentState,
                            epsilon,
                            epsilon]
                except KeyError:
                    typeCounter -= 1

            # Default value to be printed to the user, will be changed based on
            # what transition was used, derived from typeCounter
            ruleInput = currentInput
            ruleStackTop = currentStackTop

            # invalid transition
            if typeCounter == 0:
                break
            # double epsilon transition
            elif typeCounter == 1:
                ruleInput = epsilon
                ruleStackTop = epsilon
            # char epsilon transition
            elif typeCounter == 2:
                ruleInput = epsilon
                # only pop from the stack if we used the top of the stack in
                # the transition
                popped = stack.pop()
            # stack epsilon transition
            elif typeCounter == 3:
                ruleStackTop = epsilon
                # increment index only if we consumed the input from the string
                index += 1
            # No epsilon transition
            elif typeCounter == 4:
                # increment index only if we consumed the input from the string
                index += 1
                # only pop from the stack if we used the top of the stack in
                # the transition
                popped = stack.pop()

            print "Step: " + str(step) + " Rule #" + str(rule) + ": " + \
                str(currentState) + ", " + str(ruleInput) + ", " + \
                str(ruleStackTop) + " --> " + str(nextState) + ", " + \
                str(nextStackTop)

            # break on invalid stack input
            if nextStackTop not in dpdaStackAlph and nextStackTop != epsilon:
                break

            # if stack empty then set top to None, else get top element
            if len(stack) == 0:
                currentStackTop = None
            else:
                currentStackTop = stack[-1]

            # pop next stack input to the stack if it's not epsilon
            if nextStackTop != epsilon:
                stack.append(nextStackTop)
                currentStackTop = nextStackTop

            currentState = nextState
            step += 1

        if currentState in dpdaAccept and \
                index == len(string):
            print "Accepted"
        else:
            print "Rejected"
