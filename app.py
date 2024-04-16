# Define the Visitor interface
class ShapeVisitor:
    def visit_circle(self, circle):
        pass

    def visit_rectangle(self, rectangle):
        pass

# Define the Visitable interface
class Shape:
    def accept(self, visitor):
        pass

# Concrete implementation of the Visitable interface - Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def accept(self, visitor):
        visitor.visit_circle(self)

# Concrete implementation of the Visitable interface - Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def accept(self, visitor):
        visitor.visit_rectangle(self)

# Concrete implementation of the Visitor interface - AreaCalculator
class AreaCalculator(ShapeVisitor):
    def __init__(self):
        self.total_area = 0

    def visit_circle(self, circle):
        area = 3.14 * circle.radius * circle.radius
        print(f"Calculating area of Circle with radius {circle.radius}: {area}")
        self.total_area += area

    def visit_rectangle(self, rectangle):
        area = rectangle.width * rectangle.height
        print(f"Calculating area of Rectangle with width {rectangle.width} and height {rectangle.height}: {area}")
        self.total_area += area

# Concrete implementation of the Visitor interface - PerimeterCalculator
class PerimeterCalculator(ShapeVisitor):
    def __init__(self):
        self.total_perimeter = 0

    def visit_circle(self, circle):
        perimeter = 2 * 3.14 * circle.radius
        print(f"Calculating perimeter of Circle with radius {circle.radius}: {perimeter}")
        self.total_perimeter += perimeter

    def visit_rectangle(self, rectangle):
        perimeter = 2 * (rectangle.width + rectangle.height)
        print(f"Calculating perimeter of Rectangle with width {rectangle.width} and height {rectangle.height}: {perimeter}")
        self.total_perimeter += perimeter

# Client code
if __name__ == "__main__":
    shapes = [Circle(5), Rectangle(3, 4), Circle(7)]

    area_calculator = AreaCalculator()
    perimeter_calculator = PerimeterCalculator()

    for shape in shapes:
        shape.accept(area_calculator)
        shape.accept(perimeter_calculator)

    print(f"Total area: {area_calculator.total_area}")
    print(f"Total perimeter: {perimeter_calculator.total_perimeter}")
