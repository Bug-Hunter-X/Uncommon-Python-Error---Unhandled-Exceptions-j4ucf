def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError:
        print("Error: Invalid input type")
        return None

# Example usage that demonstrates the error
print(function_with_uncommon_error(10, 0)) # This will print an error message
print(function_with_uncommon_error(10, 'a')) # This will print an error message
print(function_with_uncommon_error(10, 2)) # This will print 5.0