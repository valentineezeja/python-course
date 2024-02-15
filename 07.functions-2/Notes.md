
**args: gathers remaining arguments into a tuple
*kwargs: gathers remaining arguments into a dictionary

#Parameter ordering in a function:
1. parameter
2. *args
3. Default parameters
4. **kwargs

# Tuple unpacking:
Because *args expect a tuple input, if a list is passed to the function for execution,
it treats it as 1 entity and the required job fails. To convert (unpack) the provided
argument into a tuple in order to be seen as separate values by python,
use *
Example: my_list = [1, 2, 3, 4, 5]
print my_function ((*my_list))

# Dictionary unpacking:
Works same as Tuple unpacking but for dictionaries.
See example in files.