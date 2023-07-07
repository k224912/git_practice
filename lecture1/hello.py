
name = input("whats your name?")
# oto fix white space in string
name = name.strip()

# to capitalize the first letter in a string
name = name.capitalize()

# to capitalize the first letter of every word in a one line sentence
name = name.title()

number = input("input the number").strip().title()

first, middle, last = name.split(" ")

print("my name is "+last, sep="space ", end="\n")

# making a function hello


def hello(name):
    # name = input("what is your name").strip().title()
    print(f"hello {name}")


hello("jaleed")
