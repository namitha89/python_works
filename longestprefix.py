def longestPrefix( arr ):
	preffix = ''

	for i, ch in enumerate(arr[0]):
		print(ch)
		for word in arr:
			try:
				if ch != word[i]:
					return
			except KeyError:
				return
		# print ch






# def findPreffes()
arr = ['abccccllkku','abcccdvvvv','abcccef']
longestPrefix( arr )