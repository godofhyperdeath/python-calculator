modes=[]
modes.append("Add");
modes.append("Subtract");
modes.append("Multiply");
modes.append("Divide");
def add():
    n1 = int(raw_input('Enter the first number you want:'))
    n2 = int(raw_input('Enter the second number you want:'))
    return n1 + n2
def take():
    n1 = int(raw_input('Enter the first number you want:'))
    n2 = int(raw_input('Enter the second number you want:'))
    return n1 - n2
def multiply():
    n1 = int(raw_input('Enter the first number you want:'))
    n2 = int(raw_input('Enter the second number you want:'))
    return n1 * n2
def divide():
    n1 = int(raw_input('Enter the first number you want:'))
    n2 = int(raw_input('Enter the second number you want:'))
    return n1 / n2
version = "0.0.0.1"
print("Ver " + version)
print("Modes:")
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
   
