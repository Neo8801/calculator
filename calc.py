
print("Best calculator ever!")

x = int(input("X: "))
y = int(input("Y: "))

print(f"sum: {x + y}")
print(f"sub: {x - y}")
print(f"mul: {x * y}")

if y == 0:
	print("Can't do it!")
else:
    print(f"div: {x / y}")
