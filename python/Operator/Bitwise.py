# Input Nilai  
a = int(input("Angka a : "))
b = int(input("Angka b : " ))

# Hasil Konversi dari desimal ke biner
biner_a = format(a,"08b")
biner_b = format(b,"08b")

""""""
print ("=" *15) 
print ("Dalam Biner :")
print ("=" *15) 
""""""
#Nilai hasil input yang menjadi biner 
print ("Biner a = ",biner_a)
print ("Biner b = ",biner_b)

print ("\n","="*5,"Hasil Konversi","="*5,"")

print ("-" *10,"AND","-"* 10) 
c = a & b
print('nilai :',c,' , binary :',format(c,'08b'))

print ("-" *10,"OR","-"* 10) 
c = a | b
print('nilai :',c,' , binary :',format(c,'08b'))

print ("-" *10,"XOR","-"* 10) 
c = a ^ b   
print('nilai :',c,' , binary :',format(c,'08b'))

print ("-" *10,"NOT/Negasi","-"* 10) 
c = ~a   
print('nilai :',c,' , binary :',format(c,'08b'))

print ("\n","-" *10,"Shift Left","-"* 10) 
c = a << 2
print('=========<<=========')
print('nilai :',a,' , binary :',format(a,'08b'))
print('----------------------------- (<<)')
print('nilai :',c,' , binary :',format(c,'08b'))

print ("-" *10,"Shift Right","-"* 10) 
c = a >> 2  
print('=========>>=========')
print('nilai :',a,' , binary :',format(a,'08b'))
print('----------------------------- (>>)')
print('nilai :',c,' , binary :',format(c,'08b'))


