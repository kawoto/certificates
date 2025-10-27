class Rectangle:
    """Represents a rectangle with width and height."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def get_perimeter(self):
        """Return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        """Return the diagonal length of the rectangle."""
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        """Return a string picture representation of the rectangle using '*'.

        Returns an error message if the rectangle is too large.
        """
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        return ('*' * self.width + '\n') * self.height

    def get_amount_inside(self, shape):
        """Return how many times another shape fits inside this one."""
        if shape.get_area() == 0:
            return 0
        return self.get_area() // shape.get_area()

    def __str__(self):
        """String representation."""
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    """Represents a square (inherits from Rectangle)."""

    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, side):
        """Set all sides of the square."""
        self.width = side
        self.height = side

    def set_width(self, side):
        """Ensure square stays square."""
        self.set_side(side)

    def set_height(self, side):
        """Ensure square stays square."""
        self.set_side(side)

    def __str__(self):
        """String representation."""
        return f"Square(side={self.width})"
