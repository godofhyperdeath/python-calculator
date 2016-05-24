#--variables start--#
modes=[]
version = "0.0.0.1"
modes.append("Add");
modes.append("Subtract");
modes.append("Multiply");
modes.append("Divide");
modes.append("interest");
#--variables end--#
def simpleInterest(p, r, t):
    return p * r * t
def add(num1, num2):
    return num1 + num2
def take(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2

print("Ver " + version)
print("Modes:")
for x in modes: print x,
print("")
mode = raw_input('Enter the mode you want:')
if mode == "add":
    n1 = float(raw_input('Enter the first number you want:'))
    n2 = float(raw_input('Enter the second number you want:'))
    print(add(n1, n2))
elif mode =="subtract":
    n1 = float(raw_input('Enter the first number you want:'))
    n2 = float(raw_input('Enter the second number you want:'))
    print(take(n1, n2))
elif mode == "divide":
    n1 = float(raw_input('Enter the first number you want:'))
    n2 = float(raw_input('Enter the second number you want:'))
    print(divide(n1, n2))
elif mode == "multiply":
    n1 = float(raw_input('Enter the first number you want:'))
    n2 = float(raw_input('Enter the second number you want:'))
    print(multiply(n1, n2))
elif mode =="interest":
    n1 = float(raw_input('Enter the Princapal:'))
    n2 = float(raw_input('Enter the Intrest Rate:'))
    n3 = float(raw_input('Enter the Time:'))
    print(simpleInterest(n1, n2, n3))
else:
    print "Unknown Mode Type"
   
