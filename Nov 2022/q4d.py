def removeOdd(str):
    return str[::2]

str= input("Enter a string: ")

print(f"Original String: {str}") 

str = removeOdd(str)

print(f"String without odd indexes: {str}")