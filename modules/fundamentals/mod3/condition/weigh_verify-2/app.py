name = input("What is your name: ").title()
kilo = float(input("What is your weigh: "))

if kilo <= 0:
    print(f"Hello, {name}!\nNumber Invalid")
elif kilo > 0 and kilo < 3:
    print(f"Hello, {name}!\nThis number is not available")
elif kilo >= 3 and kilo <= 5:
    print(f"Hello, {name}!\nYou're a baby")
elif kilo >= 6 and kilo <= 19:
    print(f"Hello, {name}!\nYou're a mid child")
elif kilo > 19 and kilo <= 29:
    print(f"Hello, {name}!\nYou're a child")
elif kilo >= 30 and kilo <= 59:
    print(f"Hello, {name}!\nYou're a teenager")
elif kilo >= 60 and kilo <= 100:
    print(f"Hello, {name}!\nYou're a adult ")
elif kilo > 100:
    print(f"Hello, {name}!\nYou're a monster")
