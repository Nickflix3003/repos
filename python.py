
def task1() :
    first_number = int(input("enter a number of hours that will be turned into min: "))
    output = (first_number * 60)

    print(str(first_number) + " hours turns into " + str(output) + "min")

def task2():
    type = int(input ("Do you want to convert min to hours (type in : 1), or convert hours to min (type in : 2) : "))
    first_number = int(input ("enter the number: "))
    output = 0
    if type == 1:
        output = first_number / 60
        print(str(first_number) + " min turns into " + str(output) + " hours")
    elif (type == 2):
        output = first_number * 60
        print(str(first_number) + " hours turns into " + str(output) + " min")
    else:
        print("invalid input")
    

def task3() :
    word = input ("Enter a string to be counted : ")
    output = len(word)
    print("The number of characters in this string is : " + str(output))

while (True):
    ඞ = int(input("Enter a mode (1 for task 1, 2 for task 2, 3 for task 3, and 4 to exit): "))
    if ඞ == 1 : 
        task1()
    elif ඞ == 2 : 
        task2()
    elif ඞ == 3 : 
        task3()
    elif ඞ == 4 : 
        break
    else : 
        print ("invalid input")