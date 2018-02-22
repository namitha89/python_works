#!/usr/bin/python

def execute(list1, command):
	# print list1
	# print command
	command = command.split(' ')
	count = len(command)
	if(count == 1):
		input1 = command[0]
		input2 = ''
		input3 = ''
	if(count == 2):
		input1 = command[0]
		input2 = int(command[1])
		input3 = '';
	if(count == 3):
		input1 = command[0]
		input2 = int(command[1])
		input3 = int(command[2])

	if(input1 == 'insert'): 
		list1.insert(input2,input3);
	elif(input1 == 'print'):
		print(list1);
	elif(input1  == 'remove'):
		list1.remove(input2);
	elif(input1 == 'append'):
		list1.append(input2);
	elif(input1 == 'sort'):
		list1.sort();
	elif(input1 == 'pop'):
		list1.pop();
	elif(input1 == 'reverse'):
		list1.reverse();


list1 = []
loop = int(raw_input())
for i in range(loop):
	n = raw_input()
	execute(list1, n)




	





   