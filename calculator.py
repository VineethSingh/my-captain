def add(x, y):  
   return x + y 
def sub(x, y): 
   return x - y 
def mul(x, y): 
   return x * y 
def divide(x, y):
   return x / y  
print("Select operation.")  
print("1.Add")  
print("2.Subtract")  
print("3.Multiply")  
print("4.Divide")  
  
choice = input("Enter choice(1/2/3/4):")  
num1 = int(input("Enter first number: "))  
num2 = int(input("Enter second number: "))  
  
if choice == '1':  
   print(num1,"+",num2,"=", add(num1,num2))  
  
elif choice == '2':  
   print(num1,"-",num2,"=", sub(num1,num2))  
  
elif choice == '3':  
   print(num1,"*",num2,"=", mul(num1,num2))  
elif choice == '4':  
     if num2 == 0   
 print("Invalid input")
else: print(num1,"/",num2,"=", divide(num1,num2)) 
else: print(“Invalid operator”)
