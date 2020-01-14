def findComplement(n):
	binary_value = convertToBinary(n)
	str_binary_value = str(binary_value)
	num_val = ''
	for i in str_binary_value:
		if i == '0':
			i = str(1)
			num_val +=i
		else:
			i = str(0)
			num_val +=i
	num_val = num_val
	decimal_val = convertToDecimal(num_val)
	print(decimal_val)


def convertToDecimal(n):
	return int(n,2)

def convertToBinary(n):
	return int(bin(n)[2:])

n=1
findComplement(n)