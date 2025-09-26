def add_numbers(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b

def divide_numbers(a: int, b: int) -> float:
    """Return the result of dividing a by b. Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b

def main():
    result = add_numbers(2, 3)
    print("Sum:", result)

    try:
        print("Division:", divide_numbers(5, 2))
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()

