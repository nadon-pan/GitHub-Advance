def greet(name):
    return f"Hello, {name}!"

def main():
    print(greet("World"))

if __name__ == "__main__":
    main()

def greet_uppercase(name):
    return greet(name).upper()
