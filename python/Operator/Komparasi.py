# Operasi Komparasi atau Pembanding 
# Operator ini digunakan untuk membandingkan dua buah nilai. 
# Operator ini juga dikenal dengan operator relasi dan sering digunakan untuk membuat sebuah logika atau kondisi.

# Lebih besar : >
# Lebih Kecil : < 
# Sama Dengan : ==
# Tidak Sama Dengan : !=
# Lebih Besar Sama Dengan : >=
# Lebih Kecil Sama Dengan : <=

a = int(input("Nilai a = "))
b = int(input("Nilai b = "))

c = a==b
print ("Apakah sama %d == %d: %r" % (a,b,c))

c = a > b
print ("Apakah sama %d > %d: %r" % (a,b,c))

c = a < b
print ("Apakah sama %d < %d: %r" % (a,b,c))

c = a != b 
print ("Apakah sama %d != %d: %r" % (a,b,c))

c = a >= b
print ("Apakah sama %d >= %d: %r" % (a,b,c))

c = a <= b
print ("Apakah sama %d <= %d: %r" % (a,b,c))
