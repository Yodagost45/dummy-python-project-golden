"""Basic mathematics helper functions."""


# Function is comprehensively tested
def multiply_three(x, y, z):
    """Return the product of x, y, and z."""
    return x * y * z


# Function is comprehensively tested
def add_three(x, y, z):
    """Return the sum of x, y, and z."""
    return x + y + z


# Function is comprehensively tested
def subtract_three(x, y, z):
    """Return x minus y minus z."""
    return x - y - z


# Function is comprehensively tested
def average_three(x, y, z):
    """Return the arithmetic mean of x, y, and z."""
    return (x + y + z) / 3


# Function is comprehensively tested
def sum_of_squares(x, y, z):
    """Return the sum of the squares of x, y, and z."""
    return x**2 + y**2 + z**2


if __name__ == "__main__":
    print("multiply_three(2, 3, 4) =", multiply_three(2, 3, 4))
    print("add_three(2, 3, 4) =", add_three(2, 3, 4))
    print("subtract_three(10, 3, 2) =", subtract_three(10, 3, 2))
    print("average_three(2, 3, 4) =", average_three(2, 3, 4))
    print("sum_of_squares(2, 3, 4) =", sum_of_squares(2, 3, 4))
