# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1 = name1.lower()
name2 = name2.lower()

t = 0
r = 0
u = 0
e = 0
l = 0
o = 0
v = 0
count_true = 0
count_love = 0
score = 0

t = name1.count('t')+name2.count('t')
r = name1.count('r')+name2.count('r')
u = name1.count('u')+name2.count('u')
e = name1.count('e')+name2.count('e')
l = name1.count('l')+name2.count('l')
o = name1.count('o')+name2.count('o')
v = name1.count('v')+name2.count('v')

count_true = t+r+u+e
count_love = l+o+v+e
score = count_true*10 + count_love 

if score <10 or score>90:
  print(f"Your score is {score},you go together like coke and mentos.")
elif score >40 and score <50:
  print(f"Your score is {score},you are alright together.")
else:
  print(f"Your score is {score}.")