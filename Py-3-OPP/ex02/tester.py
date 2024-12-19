from DiamondTrap import King

Joffrey = King("Joffrey")
print(Joffrey.__dict__)

Joffrey.set_eyes("blue")
Joffrey.set_hairs("light")

print(Joffrey.get_eyes())
print(Joffrey.get_hairs())
print(Joffrey.__dict__)

# Method Resolution Order (MRO) is the order in which
# Python looks for a method in a hierarchy of classes.
# print(King.mro())
