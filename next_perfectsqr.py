import math 

def find_next_square(sq):
    if (math.sqrt(sq).is_integer()):
         n_sq = math.floor(math.sqrt(sq)) + 1 #Grab the sqrt of the parameter, floor it, add 1 to it
         return n_sq * n_sq #return the square number if is perfect
    else:
        return -1

print(find_next_square(121))
print(find_next_square(625))

print(find_next_square(155))
print(find_next_square(342786627))

