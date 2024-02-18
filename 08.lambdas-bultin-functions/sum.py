# define sum_even_values
def sum_even_values(*args):
    return sum(num for num in args if num % 2 == 0)