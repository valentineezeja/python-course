# def divide(num1, num2):
#     result = 0
#     try:
#         result = num1 / num2
#     except TypeError as err:
#         print("Please provide two integers or floats")
#     except ZeroDivisionError as err:
#         print("Please do not divide by zero")
#     finally:
#         return result
#
#
# divide(1, 0)

# Using raise

def divide(num1, num2):
    result = 0
    try:
        result = num1 / num2
    except TypeError as err:
        print("Please provide two integers or floats")
    except ZeroDivisionError as err:
        print("Please do not divide by zero")
    finally:
        return result


test = divide(1, 5)
print(test)
