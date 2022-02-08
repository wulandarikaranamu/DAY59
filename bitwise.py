#operasi bitwise

print("\n"+"OR"+"\n"+10*"=")

a = True
print("nilai a =",a)
a |= False
print("nilai a |= False, nilai a menjadi",a)

print("\n"+"BATAS"+"\n"+30*"=")

a = False
print("nilai a =",a)
a |= False
print("nilai a |= False, nilai a menjadi",a)


print("\n"+"AND"+"\n"+10*"=")

b = True
print("nilai b =",b)
b &= False
print("nilai b &= False, nilai b menjadi",b)

print("\n"+"BATAS"+"\n"+30*"=")

b = True
print("nilai b =",b)
b &= True
print("nilai b &= True, nilai b menjadi",b)

print("\n"+"XOR"+"\n"+10*"=")

c = True
print("nilai c =",c)
c ^= False
print("nilai c ^= False, nilai c menjadi",c)

print("\n"+"BATAS"+"\n"+30*"=")

c = True
print("nilai c =",c)
c ^= True
print("nilai c ^= True, nilai c menjadi",c)


print("\n"+"MENGGESER SEBUAH NILAI"+"\n"+10*"=")

d = 0b0100
print("nilai d",d)




