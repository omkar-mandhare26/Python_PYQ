class repeatString:
    def __init__(self, string):
        self.str = string

    def __mul__(self, n):
        return self.str * n

str = input("Enter a string: ")
n = int(input("Enter a number to repeat the string: "))

obj = repeatString(str)

result = obj * n

print(f"Repeated string: {result}")