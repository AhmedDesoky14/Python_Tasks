"""**************************************************************************************************************************************************
Description:   This code is to get the largest number from a list using sorting

**************************************************************************************************************************************************"""
lst = [5,9,11,15,20,17,16,1,3,21,55,74,12,45,99]
lst.sort(reverse=True)
print("largest number: "+str(lst[0]))