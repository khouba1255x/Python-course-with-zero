# ------------------
# -- Type Hinting --
# ------------------
print("=" * 40)

def say_hello(name) -> str: 
    print(f"Hello {name}")

say_hello("Ahmed")

print("=" * 40)

def calculate(n1, n2) -> int:
    print(n1 + n2)

calculate(10, 40)