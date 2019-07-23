def swap(x,y):
	x,y = y,x
	print(x,y)

# swap(2,3)

def make_empty(seq):
    """
      >>> make_empty([1, 2, 3, 4])
      []
      >>> make_empty(('a', 'b', 'c'))
      ()
      >>> make_empty("No, not me!")
      ''
    """
    if seq == []:
    	return seq
print(make_empty([1, 2, 3, 4]))	
# make_empty(('a', 'b', 'c'))
# make_empty("No, not me!")