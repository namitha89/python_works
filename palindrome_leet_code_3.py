def palindrome(num):
    reverse = 0
    actualnumber = num
    while(num > 0):
        lastdigit = num % 10
        reverse = (reverse * 10) + lastdigit
        num = num / 10

    if (reverse == actualnumber):
        print("The given number is palindrome")
    else:
        print("The given number is not a palindrome")

palindrome(131)

