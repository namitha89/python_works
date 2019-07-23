def string_operation3():
  prefixes = "JKLMNOPQ"
  suffix = "ack"
  for letter in prefixes:
  	result = letter + suffix
  	if(result == 'Oack'):
  		print('Ouack')
  	elif(result == 'Qack'):
  		print('Quack')
  	else:
  		print result

string_operation3()
