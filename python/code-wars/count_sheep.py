
def count_sheeps(sheep):
    i = 0 
    for each in sheep:
        if each == True:
            i += 1
    return i

###########################################################    

array1 = [True, True, True, False, True, True, True, True, True, False, True, False, True, False, False, True, True, True,  True, True, False, False, True, True ];
result = count_sheeps(array1)
print(result)

###########################################################    
