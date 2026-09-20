data = True
user_input = input("Enter the word you want to find: ")
lines = 0
with open("python/sample.txt", "r") as f:
    while data:
        lines += 1
        data = f.readline()
        if (user_input in data):
            print(f"{user_input} was found at line {lines}")
            break
