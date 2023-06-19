expression = input("Expression: ")

x, operator, y = expression.split()

x = int(x)
y = int(y)

result = None

if operator == "-":
    result = x - y
elif operator == "+":
    result = x + y
elif operator == "*":
    result = x * y
elif operator == "/":
    result = x / y

formatedResult = "{:.1f}".format(result)
print(formatedResult)
