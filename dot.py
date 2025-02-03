class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __add__(self, other):
        return Dot(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Dot(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):  # Allow both int and float
            return Dot(self.x * scalar, self.y * scalar)
        raise TypeError("Can only multiply by an integer")

    def __truediv__(self, scalar):
        if isinstance(scalar, (int, float)):  # Allow both int and float
            if scalar == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            return Dot(self.x / scalar, self.y / scalar)
        raise TypeError("Can only divide by an integer or float")

    def __str__(self):
        return f"({self.x}, {self.y})"

def main():
    a = Dot(1, 2)
    b = Dot(3, 4)
    print(a + b)  # (4, 6)
    print(a - b)  # (-2, -2)
    print(a * 2)  # (2, 4)
    print(a / 2)  # (0.5, 1.0)

if __name__ == "__main__":
    main()
