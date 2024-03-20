"""
TR 1. 1-Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle indeksini (VKİ = ağırlık/(boy*boy)) hesaplayınız.
***
EN 1-Calculate the body mass index (BMI = weight/(height*height)) according to the height and weight values entered by the user.
*****
"""
"""
print("\n *** Let's see how fit you are...\n")
height = float(input("Please enter your height: \n"))
weight = float(input("Please enter your weight: \n"))
bmi = weight / (height ** 2)
print("Your body mass index is: ", bmi)

if bmi < 18.5:
    print ("Your weight is below ideal weight")
elif bmi >= 18.5 and bmi < 24.9:
    print ("Your weight is ideal")
elif bmi >= 25 and bmi < 29.9:
    print ("Your weight is above ideal weight")
elif bmi >= 30 and bmi < 39.9:
    print ("Your weight is dangerously above ideal weight. It's obese")
else:
    print ("Your weight is highly above ideal weight. It's morbidly obese")
"""


"""
TR 2-Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda gösteriniz.
***
EN 2-Calculate the increased salary of the worker whose salary and increase rate is entered and display it on the screen.
*****
"""
"""
print("\n *** Let's how your new salary is satisfied for you...\n")
salary = int(input("Please enter your monthly salary: \n"))
raise_rate = float(input("Please enter the last salary increase you received: \n"))
current_salary = salary + (salary * (raise_rate / 100))
hr_message = f"Your current salary is: {current_salary} \n if it seems like low please knock on your boss's door \n Otherwise, we wish you happiness until the next hike period..."
print(hr_message)
"""


"""
TR 3-Kullanıcının girdiği üç sayı arasında en büyük olanı bulan ve sonucu yazdıran bir program yazınız.
***
EN 3-Write a program that finds the largest of the three numbers entered by the user and prints the result.
*****
"""
"""
print("\n *** We'll check which number is the biggest among three numbers you'll give \n")
num1 = int(input("Please enter first number: "))
num2 = int(input("Please enter second number: "))
num3 = int(input("Please enter third number: "))

top_num = None

if num1 > num2 and num1 > num3:
    top_num = num1
    print ("The biggest number is your first number which is: ", top_num)
elif num2 > num1 and num2 > num3:
    top_num = num2
    print ("The biggest number is your second number which is: ", top_num)
elif num3 > num1 and num3 > num2:
    top_num = num3
    print ("The biggest number is your third number which is: ", top_num)
else:
    if num1 == num2 and num1 != num3:
        top_num = num1
        print ("You gave your first and second numbers as same \n Therefore they are both the biggest: ", top_num)
    elif num1 == num3 and num1 != num2:
        top_num = num1
        print ("You gave your first and third numbers as same \n Therefore they are both the biggest: ", top_num)
    elif num2 == num3 and num2 != num1:
        print ("You gave your second and third numbers as same \n Therefore they are both the biggest: ", top_num)
    else:
        top_num = num1
        print ("You gave all your numbers as same \n Therefore there can't be the biggest with these inputs...")
"""

"""
TR 4-Dairenin alanını ve çevresini hesaplayan python kodunu yazınız.(Dairenin yarıçapını kullanıcıdan alınız)
***
EN 4-Write the python code that calculates the area and circumference of the circle.(Get the radius of the circle from the user)
*****
"""

print("\n *** We'll find out are and circumference of circle according to your radius input...\n ")
pi = 3.14159
radius = float(input("Please enter radius you like: "))
c_area = pi * (radius ** 2)
c_circumference = 2 * pi * radius
cal_message = f"\n Circle's area is: {c_area} \n Circle's circumference is: {c_circumference}\n"
print (cal_message)


"""
TR 5-Kullanıcıdan alınan bir sayının palindrom olup olmadığını bulan bir program yazınız.
***
EN 5-Write a program that finds whether a number received from the user is a palindrome or not.
*****
"""