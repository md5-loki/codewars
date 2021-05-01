def digital_root(number):

    while(number >= 10): # While number has 2 digits 
         number = sum(int(i) for i in str(number)) # Sum all the numbers in the given quantity 
    return number

print(digital_root(953)) # 8
