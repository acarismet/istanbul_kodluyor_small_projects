"""
TR 1. 1-Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle indeksini (VKİ = ağırlık/(boy*boy)) hesaplayınız.
***
EN 1-Calculate the body mass index (BMI = weight/(height*height)) according to the height and weight values entered by the user.
*****
"""

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
TR 2-Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda gösteriniz.
***
EN 2-Calculate the increased salary of the worker whose salary and increase rate is entered and display it on the screen.
*****
"""

"""
TR 3-Kullanıcının girdiği üç sayı arasında en büyük olanı bulan ve sonucu yazdıran bir program yazınız.
***
EN 3-Write a program that finds the largest of the three numbers entered by the user and prints the result.
*****
"""

"""
TR 4-Dairenin alanını ve çevresini hesaplayan python kodunu yazınız.(Dairenin yarıçapını kullanıcıdan alınız)
***
EN 4-Write the python code that calculates the area and circumference of the circle.(Get the radius of the circle from the user)
*****
"""


"""
TR 5-Kullanıcıdan alınan bir sayının palindrom olup olmadığını bulan bir program yazınız.
***
EN 5-Write a program that finds whether a number received from the user is a palindrome or not.
*****
"""