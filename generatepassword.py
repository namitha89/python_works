import random

def generate(plen) :
	t = "ekedjeryiu3rhvmsdnuyruyeriuyeiruosldjkhdjgyjdjgwydgywteyttwfytdfu"
	return "".join(random.sample(t,plen ))

print(generate(8))