student = []
marks = []
profile = []

for _ in range(int(raw_input())):
    name = str(raw_input())
    score = float(raw_input())
    student.append(name)
    marks.append(score)
profile = zip(student,marks)
marks = sorted(set(marks))
marks = list(marks)
marks.remove(min(marks))
secondlowest = min(marks)
secondname = []
for i in range(0,len(profile)):
	if(profile[i][1] == secondlowest):
		secondname.append(profile[i][0])

for j in sorted(secondname) :
	print j

