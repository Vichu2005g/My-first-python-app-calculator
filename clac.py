x = input('hi! Enter 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division, 5 for exponet, 6 for nth term of ap and 7 for sum of nth term of an ap: ')
if x == '1' :
  a = float(input("first number: "))
  b = float(input("second number: "))
  print(a + b)
elif x == '2':
  aa = float(input("first number: "))
  bb = float(input("second number: "))
  print(aa - bb)
elif x == '3':
  aaa = float(input("first number: "))
  bbb = float(input("second number: "))
  print(aaa * bbb)
elif x == '4':
  aaaa = float(input("first number: "))
  bbbb  = float(input("second number: "))  
  print(aaaa / bbbb ,'your reminder is', aaaa % bbbb ) 
elif x == '5':
  aaaaa = float(input("first number (this would be your whole number): "))
  bbbbb = float(input("second number (this would be the power for the number): "))
  print(aaaaa ** bbbbb) 
elif x =='6':
  Ath = float(input("first term a: "))
  d = float(input("common difference d: "))
  n = float(input("the nth term of ap n: "))
  print(Ath + (n - 1)*d)    
elif x == '7':
  Ath1 = float(input("first term a: "))
  d1 = float(input("common difference d: "))
  n1 = float(input("nth term of ap n: "))
  print(n1/2*(2*Ath1 + (n1-1)*d1))  
else:
  print("please write a valid option! Exitting...")


