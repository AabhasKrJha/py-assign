def calculate_area(length, width):
    if length == width:
        return "This is a square!"
    else:
        return length * width

try:
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    
    area_or_message = calculate_area(length, width)
    
    print(area_or_message)
except ValueError:
    print("Please enter valid numeric values for length and width.")

