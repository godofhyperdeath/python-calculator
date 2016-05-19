modes=[]
modes.append("Add");
def add():
    n1 = int(raw_input('Enter the first number you want:'))
    n2 = int(raw_input('Enter the second number you want:'))
    return n1 + n2

modes.append("Subtract");
def take():
    n1 = int(raw_input('Enter the first number you want:'))
    n2 = int(raw_input('Enter the second number you want:'))
    return n1 - n2
    
modes.append("Multiply");
def multiply():
    n1 = int(raw_input('Enter the first number you want:'))
    n2 = int(raw_input('Enter the second number you want:'))
    return n1 * n2
    
modes.append("Divide");
def divide():
    n1 = int(raw_input('Enter the first number you want:'))
    n2 = int(raw_input('Enter the second number you want:'))
    return n1 / n2
    
print("Calculator")
print("ver 0.0.0.1")
print("modes:")
for x in modes: print x,
print("")
mode = raw_input('Enter the mode you want:')
if mode == "add":
   print(add())
elif mode =="subtract":
   print(take())
elif mode == "divide":
    print(divide())
elif mode == "multiply":
    print(multiply())
else:
    print Unknown Mode Type
   
