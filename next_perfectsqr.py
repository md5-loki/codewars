def get_perfectsqr(sq):
    # Return the next square if sq is a square, -1 otherwise
    # Case -> 121
    
    sqr = sq ** 0.5
    
    # 121 ^ 1/2 = 11
    
    if(sqr.is_integer()):
        sqr = sqr + 1
        # (121 ^ (1/2)) + 1 = 12
        return sqr * sqr
        # 12 is the next one   
    return False

    
print(get_perfectsqr(121))
print(get_perfectsqr(155))

# WITHOUT USING math module !
