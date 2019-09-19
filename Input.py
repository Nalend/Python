temperature = 15
if temperature > 30:
    print("Panas")
    print("banget")
elif temperature > 20:
    print("Dingin")
else:
    print("its cold")
print("done")


# Command

command = ""
while command.lower() != "quit":
    command = input("Task >>")
    print("ECHO", command)

# Command 2

while True:
    command = input("Task >>")
    print("ECHO", command)
    if command.lower() == "quit":
        break
