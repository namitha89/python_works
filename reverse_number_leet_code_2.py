def reverse_number():
    reverse = 0
    number = int(raw_input("please enter the number to be reversed : "))
    while (number > 0):
        lastdigit = number%10
        reverse = (reverse*10) + lastdigit
        number = number/10

    print(reverse)

reverse_number()