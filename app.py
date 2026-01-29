def greet(name):
	return f"Hello, {name}!"

print(greet("World!"))

def greet_uppercase(name):
    return greet(name).upper()

DEBUG: temporary debug line - DELETE THIS
print("DEBUG: This should not be in production")
