
def add():
    n1 = int(raw_input('Enter the first number you want:'))
    n2 = int(raw_input('Enter the second number you want:'))
    return n1 + n2

print("calculator")
print("ver 0.0.0.0")
print("modes: add")
mode = raw_input('Enter the mode you want:')
if mode == "add":
   res = add()
   print(res)
else:
    print("1")

