def camel_to_snake(s):
    snake_case_name = ""
    for c in s:
        if c.isupper():
            snake_case_name += "_" + c.lower()
        else:
            snake_case_name += c
    return snake_case_name

variable_name = input("camelCase: ")
snake_case_name = camel_to_snake(variable_name)
print("snake_case:", snake_case_name)