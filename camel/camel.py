# Get input from the user
camel_case = input("Enter a variable name in camel case: ")

# Convert camel case to snake case
snake_case = ''.join(['_' + i.lower() if i.isupper() else i for i in camel_case]).lstrip('_')

# Print the result
print(snake_case)
