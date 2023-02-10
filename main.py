from Naitik_Lodha.C028 import greatest_num, rev_90_triangle
from Naitik_Lodha import personal_details
from Naitik_Lodha.Naitik_Lodha_C028 import hobby_list, marks_dict

print(personal_details.details())
a = int(input("Enter number1: "))
b = int(input("Enter number2: "))
c = int(input("Enter number3: "))

print("Greatest number is:", greatest_num.greatest(a, b, c))
a = int(input("Enter length for reversed triangle: "))
print("Reversed triangle is:")
rev_90_triangle.traingle(a)
print("Hobby at index -2 is ", hobby_list.getHobbies())
print(marks_dict.getMarks())
