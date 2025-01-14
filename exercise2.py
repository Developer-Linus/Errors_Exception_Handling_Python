try:
    with open("sampsle.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError as e:
    print(e)