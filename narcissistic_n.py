def narcissistic( value ):
    t = 0 # Accumulator variable
    str_value = str(value) # Convert the parameter to a string
    digit_amount = len(str_value) # Count the amount of chars in the string
    
    for x in str_value: #Loop thru the string
        
        t += int(x) ** digit_amount # Add to the accumulator the power operation

    return t == value # Returns true If the accumulator is equal to the parameter

print(narcissistic(153))
