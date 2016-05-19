modes=[]
modes.append("add");
def add():
    n1 = int(raw_input('Enter the first number you want:'))
    n2 = int(raw_input('Enter the second number you want:'))
    return n1 + n2
modes.append("take");
def take():
    n1 = int(raw_input('Enter the first number you want:'))
    n2 = int(raw_input('Enter the second number you want:'))
    return n1 - n2
print("calculator")
print("ver 0.0.0.1")
print("modes:")
for x in modes: print x,
print("")
mode = raw_input('Enter the mode you want:')
if mode == "add":
   print(add())
elif mode =="take":
   print(take())
else:
    print("unknown mode")
