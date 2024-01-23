from graphic.circle import circle_area
from graphic.circle import circle_perimeter
r=int(input("enter the radius:"))
area=circle_area(r)
perimeter=circle_perimeter(r)
print(area)
print(perimeter)


from graphic.rectangle import rectangle_area
from graphic.rectangle import rectangle_perimeter
l=int(input("enter the length:"))
b=int(input("enter the bredth:"))
r_area=rectangle_area(l,b)
r_perimeter=rectangle_perimeter(l,b)
print(r_area)
print(r_perimeter)


from graphic.dgraphic.cuboid import cuboid_area
from graphic.dgraphic.cuboid import cuboid_perimeter
l=int(input("enter the length:"))
b=int(input("enter the bredth:"))
h=int(input("enter the height:"))
area=cuboid_area(l,h,b)
perimeter=cuboid_perimeter(l,b,h)
print(area)
print(perimeter)

from graphic.dgraphic.sphere import sphere_area
from graphic.dgraphic.sphere import sphere_perimeter
r=int(input("enter the radius:"))
area=sphere_area(r)
perimeter=sphere_perimeter(r)
print(area)
print(perimeter)



