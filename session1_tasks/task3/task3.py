"""**************************************************************************************************************************************************
Function description:   Function to count how many 4 is in the list
Arguments:  NONE
Return: NONE
**************************************************************************************************************************************************"""
def task3_part1():
    count = 0
    lst = [4,1,19,4,3,8,0,15,4,3,4]
    for i in lst:
        if(i == 4):
            count += 1
    print("4 is there for {} times".format(count))
"""**************************************************************************************************************************************************
Function description:   Function to check if the entered character is vowel or not
Arguments:  NONE
Return: NONE
**************************************************************************************************************************************************"""
def task3_part2():
    string = input("Enter a single character: ")
    while(len(string) != 1):
        string = input("Enter a single character: ")
    if(string.lower() in ['a','e','i','o','u']):
        print("This character is vowel")
    else:
        print("This character is not vowel")
"""**************************************************************************************************************************************************
Function description:   Function to access PATH environmental variable
Arguments:  NONE
Return: NONE
**************************************************************************************************************************************************"""    
def task3_part3():
    import os
    PATH = os.environ['PATH']
    print("PATH:{}".format(PATH))

#task3_part1()
#task3_part2()
#task3_part3()