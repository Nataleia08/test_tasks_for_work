import enum
import math

class ShapeName(enum.Enum):
    square = "Square"
    rectangle = "Rectangle"
    circle = "Circle"


class Shape:
    def __init__(self, x:int, y:int, type:ShapeName) -> None:
        self.x_start = x
        self.y_start = y
        self.type = type

    def area_and_perimeter_square(self, side:int):
        perimeter = 4*side
        area = side*side
        return (perimeter, area)
    
    def area_and_perimeter_rectangle(self, x_end:int, y_end:int)-> tuple:
        result_1 = 2*abs(x_end-self.x_start) + 2*abs(y_end - self.y_start) 
        result_2 = abs((x_end-self.x_start)*(y_end - self.y_start))
        return (result_1, result_2)
    
    def area_and_perimeter_circle(self, radius:int)-> tuple:
        result = (2*radius*math.pi, math.pi*pow(radius, 2))
        return result
