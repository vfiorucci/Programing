"""Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string
 of those numbers in the form of a phone number.
 
The returned format must be correct in order to complete this challenge.
Don't forget the space after the closing parentheses!

Example
-------
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
"""
def create_phone_number(n):
    """Convert to Phone Number."""
    num_ints = [str(num) for num in n]
    str_ints = "".join(num_ints)
    return "(" + str_ints[0:3] + ") " + str_ints[3:6] + "-" + str_ints[6:10]
    # return phone_convert

phone_convert = create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
print(phone_convert)

# Other Solutions:
# 1.
# def create_phone_number(n):
#     return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

# 2.
# def create_phone_number(n):
#     n = ''.join(map(str,n))
#     return '(%s) %s-%s'%(n[:3], n[3:6], n[6:])

# 3.
# def create_phone_number(n):
#     n = "".join([str(x) for x in n] )
#     return("(" + str(n[0:3]) + ")" + " " + str(n[3:6]) + "-" + str(n[6:]))

# 4. 
# def create_phone_number(n):
#     m = ''.join(map(str, n))
#     return f"({m[:3]}) {m[3:6]}-{m[6:]}"
