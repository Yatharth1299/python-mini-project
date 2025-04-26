import random
x=random.randint(1,100)
while True:
   choose_no=int(input("Enter any number between 1 to 100"))

          
   if choose_no > x:
       print("very high")
   elif choose_no < x:
       print("very low")
   else:
       print("Congratulation you get the number")
       break



