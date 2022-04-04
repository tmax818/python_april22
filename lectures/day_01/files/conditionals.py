expression = "Something that returns a value."
if expression:
    print("Will this print?")
print("...or will this?")

if not True:
    print("this ran...")
print("no this ran!!!")


if not True:
    print("this ran...")
else:
    print("no this ran!!!")
print("of course this ran, it's outside the conditional!!!")


if not True:
    print("this ran...")
elif True:
    print("the elif ran...")
else:
    print("no this ran!!!")
print("of course this ran, it's outside the conditional!!!")