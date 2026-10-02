from math import sqrt

class Vector2:
    def __init__(self, x : float, y : float) -> None:
        self.x = x
        self.y = y

    @property
    def magnitude(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def __add__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x + other.x, self.y + other.y)
        if isinstance(other, int) or isinstance(other, float):
            return Vector2(self.x + other, self.y + other)
        

    def __sub__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x - other.x, self.y - other.y)
        if isinstance(other, int) or isinstance(other, float):
            return Vector2(self.x - other, self.y - other)
        

    def __mul__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x * other.x, self.y * other.y)
        if isinstance(other, int) or isinstance(other, float):
            return Vector2(self.x * other, self.y * other)
        

    def __pow__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x ** other.x, self.y ** other.y)
        if isinstance(other, int) or isinstance(other, float):
            return Vector2(self.x ** other, self.y ** other)
        

    def __abs__(self):
        return Vector2(abs(self.x), abs(self.y))

    # <
    def __lt__(self, other):
        if isinstance(other, Vector2):
            other = other.magnitude

        return self.magnitude < other
    # <=
    def __le__(self, other):
        if isinstance(other, Vector2):
            other = other.magnitude

        return self.magnitude <= other
    # >
    def __gt__(self, other):
        if isinstance(other, Vector2):
            other = other.magnitude

        return self.magnitude > other
    # >=
    def __ge__(self, other):
        if isinstance(other, Vector2):
            other = other.magnitude

        return self.magnitude >= other
    # ==
    def __eq__(self, other) -> bool:
        if not isinstance(other, Vector2):
            return False

        return (self.x == other.x and self.y == other.y)

    def __repr__(self) -> str:
        return "X: {x}, Y: {y}".format(x = self.x, y = self.y)

