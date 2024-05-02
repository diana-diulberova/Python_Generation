str = input()

if str[0] == '@' and 5 <= len(str) <= 15 and str[1:].isalnum() == True:
    if str[1:].isdigit() == True:
        print("Correct")
    elif str[1:].isalpha() == True:
        if str[1:].islower() == True:
            print("Correct")
        else:
            print("Incorrect")
    elif str[1:].islower() == True:
        print("Correct")
    else:
        print("Incorrect")
else:
    print("Incorrect")
