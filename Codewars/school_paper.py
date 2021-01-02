def paperwork(n, m):
    # Happy Coding! ^_^
    if n >= 0 and m >= 0:
        return int(n or 0) * int(m or 0)
    else:
        return 0

results = paperwork(-5,5)
print(results)



# Other Solutions:

# 1. 
# def paperwork(n, m):
#     return n * m if n > 0 and m > 0 else 0

# 2. 
# def paperwork(n, m):
#     return max(n, 0)*max(m, 0)

# 3. 
# def paperwork(n, m):
#     if m<0 or n<0:
#         return 0
#     else:
#         return n*m