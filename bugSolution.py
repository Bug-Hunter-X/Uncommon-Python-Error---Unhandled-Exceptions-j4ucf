def function_with_uncommon_error_solution(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError:
        print("Error: Invalid input type")
        return None
    except Exception as e: #This catches all other potential exceptions.
        print(f"An unexpected error occurred: {e}")
        return None

# Example usage
print(function_with_uncommon_error_solution(10, 0))
print(function_with_uncommon_error_solution(10, 'a'))
print(function_with_uncommon_error_solution(10, 2))
print(function_with_uncommon_error_solution('10',2)) # This will print an error message now.