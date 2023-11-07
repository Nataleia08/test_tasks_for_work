from function import Shape, ShapeName

def main():
    user_input = input("\nEnter command >>> ")
    try:
        info_list = user_input.split(" ")
        new_shape = Shape(int(info_list[2]), int(info_list[3]), info_list[0])
        match new_shape.type:
            case ShapeName.square.value: result = new_shape.area_and_perimeter_square(int(info_list[5]))
            case ShapeName.rectangle.value: result = new_shape.area_and_perimeter_rectangle(int(info_list[5]), int(info_list[6]))
            case ShapeName.circle.value: result = new_shape.area_and_perimeter_circle(int(info_list[5]))
        print(f"{new_shape.type} Perimeter {result[0]} Area {result[1]}")
    except TypeError as e:
        print(f"This command not right! {e}")


if __name__ == "__main__":
    main()




