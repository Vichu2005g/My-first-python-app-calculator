x = input('hi! Enter 1 for addition, 2 for subtraction, 3 for multiplication and 4 for division and 5 for exponet: ')

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
else:
  print("please write a valid option! Exitting...")
