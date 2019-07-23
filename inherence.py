class Human(object):

	def __init__(self,name,gender,age):
		self.name = name
		self.gender = gender
		self.age = age
		print('human')

	def sing(self):
		return '{} can sing'.format(self.name)

	def walk(self):
		return 'can walk'

	def dance(self):
		return 'can dance'

	def talk(self):
		return 'can talk'

class Mother(Human):

	def sing(self):
		return 'can sing'

	def walk(self):
		return 'can walk'

	def dance(self):
		return 'can dance'

	def talk(self):
		return 'can talk'

class Father(Human):

	def sing(self):
		return 'cant sing'

	def walk(self):
		return 'can walk'

	def dance(self):
		return 'cant dance'

	def talk(self):
		return 'can talk'

class Child(Mother,Father):

	def sing(self):
		return 'cant sing'

	def walk(self):
		return 'can walk'

	def dance(self):
		return 'cant dance'

	def talk(self):
		return 'can talk'

h1 = Human("namitha","female","28")
print(h1.name + " " + h1.gender + " " + h1.age)
print(h1.talk())
print(h1.walk())
print(h1.sing())
print(h1.dance())

mother = Mother("ratna","female","28")
print(mother.name + " " + mother.gender + " " + mother.age)
print(mother.talk())
print(mother.walk())
print(mother.sing())
print(mother.dance())

father = Father("thirumalaiah","female","28")
print(father.name + " " + father.gender + " " + father.age)
print(father.talk())
print(father.dance())
print(father.sing())
print(father.walk())

child = Child("nami","female","28")
print(child.name + " " + child.gender + " " + child.age)
print(child.talk())
print(child.dance())
print(child.sing())
print(child.walk())
















