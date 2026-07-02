name='Aum'
age=17
print("Hello, my name is "+name+" and I am "+str(age)+" years old!")
# the below should result in the code printing 15
total=5
print(total + 10)

 
def rectangle (width, height):
    area= width * height
    perimeter=2 * (width + height)
    return area, perimeter

# This will result in an area of 6 and perimeter of 10
rectangle1=rectangle(3,2)
print("(area, perimeter) for rectanlge 1 is "+str(rectangle1))

# This will result in an area of 90 and a perimeter of 38
rectangle2=rectangle(height=10, width=9)
print("(area, perimeter) for rectanlge 2 is "+str(rectangle2))

# This will result in an area of 0.125 and a perimeter of 1.5
rectangle3=rectangle(1/2,1/4)
print("(area, perimeter) for rectanlge 3 is "+str(rectangle3))