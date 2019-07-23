def print_multiples(num, high):
    count = 1
    while count <= high:
    	import pdb; pdb.set_trace() 
        print num*count, '\t',
        count += 1
    print

def print_mult_table(high):
    count = 1
    while count <= high:
        print_multiples(count, high)
        count += 1

print_mult_table(3)