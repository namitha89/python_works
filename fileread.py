with open('2city10.txt', 'r') as myfile:
    data=myfile.read().replace('\n', '')
    text = data.split(' ')
    uniquewords = {}

    for i in text:

      if i not in uniquewords:
        uniquewords[i] = 1
      else:
        uniquewords[i] += 1 

    # import pdb;pdb.set_trace()
    sv = sorted(uniquewords.items(), key=lambda x:x[1], reverse=True)
    for i in sv[0:10]: print i[0], ': ', i[1]



  