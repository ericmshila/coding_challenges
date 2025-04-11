def is_float(num_str):
    try:
        # Check for multiple dots
        if num_str.count('.') != 1:
            return False

        # Convert to float to trigger exceptions for invalid cases
        float(num_str)

        # Must have at least one digit after the decimal
        integer_part, decimal_part = num_str.split('.')
        if len(decimal_part) == 0:
            return False

        return True
    except ValueError:
        return False


# Input number of test cases
n = int(input())

# Process each test case
for _ in range(n):
    test_str = input()
    print(is_float(test_str))
