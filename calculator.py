#--variables start--#
modes=[]
version = "0.0.0.1"
modes.append("Add");
modes.append("Subtract");
modes.append("Multiply");
modes.append("Divide");
modes.append("interest");
#--variables end--#
def Simplefloaterest():
    n1 = float(raw_input('Enter the principal:'))
    n2 = float(raw_input('Enter the rate:'))
    n3 = float(raw_input('Enter the time:'))
    return n1 * n2 * n3
def add():
    n1 = float(raw_input('Enter the first number you want:'))
    n2 = float(raw_input('Enter the second number you want:'))
    return n1 + n2
def take():
    n1 = float(raw_input('Enter the first number you want:'))
    n2 = float(raw_input('Enter the second number you want:'))
    return n1 - n2
def multiply():
    n1 = float(raw_input('Enter the first number you want:'))
    n2 = float(raw_input('Enter the second number you want:'))
    return n1 * n2
def divide():
    n1 = float(raw_input('Enter the first number you want:'))
    n2 = float(raw_input('Enter the second number you want:'))
    return n1 / n2

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
elif mode =="interest":
    print(Simpleinterest())
else:
    print "Unknown Mode Type"
   
