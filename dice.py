import random

while True:
    
  choice= input("Are you ready to play Y/N :").lower()
  

  if choice == 'y':
       x=int(input("How many dies you want to role :"))
       if x==1:
         die1=random.randint(1,6)
         print(f'({die1})')
       if x==2:
         die1=random.randint(1,6)
         die2=random.randint(1,6)
         print(f'({die1},{die2})')
       if x==3:
         die1=random.randint(1,6)
         die2=random.randint(1,6)
         die3=random.randint(1,6)
         print(f'({die1},{die2},{die3})')
       if x==4:
         die1=random.randint(1,6)
         die2=random.randint(1,6)
         die3=random.randint(1,6)
         die4=random.randint(1,6)
         print(f'({die1},{die2},{die3},{die4})')
       if x==5:
         die1=random.randint(1,6)
         die2=random.randint(1,6)
         die3=random.randint(1,6)
         die4=random.randint(1,6)
         die5=random.randint(1,6)
         print(f'({die1},{die2},{die3},{die4},{die5} )')

       if x==6 :
         die1=random.randint(1,6)
         die2=random.randint(1,6)
         die3=random.randint(1,6)
         die4=random.randint(1,6)
         die5=random.randint(1,6)
         die6=random.randint(1,6)
         print(f'({die1},{die2},{die3},{die4},{die5},{die6})')  

       else:
          print("Choose no. only between 1 to 6 ")

       
      
  elif choice=='n':

      print('Thanks for playing')
      break
  else:
     print('Enter valid character :')



