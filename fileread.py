#!/usr/bin/python


with open('quiz.txt') as f:
    array = []
    score = 0
    for line in f:
    	array.append(line.rstrip('\n').split(','))
    	# n = int(raw_input())
    linelength = len(array)

    for i in range(linelength):
    	input = array[i][0]
    	input2 = int(array[i][1])
    	print input
    	commandinput = int(raw_input())
    	if(input2 == commandinput):
    		score += 1


    print "your score is",score

    