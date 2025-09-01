#Operator logika 
# digunakan untuk membuat operasi logika, seperti 
# logika AND, OR, dan NOT (negasi/kebalikan).

a = True
b = False

#Logika and Operasi ini hanya menghasilkan hasil benar jika kedua nilai tersebut benar.
# c = a and b
# print ("%r and %r = %r" %(a,b,c))

# c = a or b
# print ("%r or %r = %r" %(a,b,c))

# c = not a
# print ("%r not : %r" % (a,c))

options = True, False 
for a in options:
    for b in options:
        print (f"{a} and {b} gives {a and b}")

names = "James", "Bob", "David", "Jane", "Kate", "Mary"
for name in names:
   if len(name) < 5 and name[0] == "J":
      print(name)
