# -----------------------------------
# -- Modules => Create Your Module --
# -----------------------------------

# print("=" * 40)
# import sys
# # print(sys.path)

# print("=" * 40)
# sys.path.append(r"C:\Users")

# print(sys.path)

print("="* 40)

import elzero
print(dir(elzero))

elzero.sayHello("Ahmed")
elzero.sayHello("Osama")
elzero.sayHello("Mohammed")

print("=" * 10)
elzero.sayHowAreYou("Ahmed")
elzero.sayHowAreYou("Osama")
elzero.sayHowAreYou("Mohammed")

print("=" * 10)
# Alias
print("# Alias")

import elzero as kl
# print(dir(elzero))

kl.sayHello("Ahmed")
kl.sayHello("Osama")
kl.sayHello("Mohammed")

print("=" * 10)
kl.sayHowAreYou("Ahmed")
kl.sayHowAreYou("Osama")
kl.sayHowAreYou("Mohammed")

print("=" * 40)

from elzero import sayHello

sayHello("Osama")

print("=" * 10)

from elzero import sayHello as ss

ss("Osama")