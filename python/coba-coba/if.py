nilai = int(input("Masukan Nilai Ujian mu : "))

if nilai >= 90:
    hasil = "A"
elif nilai >= 80:
    hasil = "B"
elif nilai >= 70:
    hasil = "C"
elif nilai >= 60:
    hasil = "D"
elif nilai >= 50:
    hasil = "E"
elif nilai <= 50:
    hasil = "kamu Ulang Lagi"

print ("Hasil Yang Kamu Dapatkan :\n %s" % hasil)

umur = int(input("berapa umur kamu : "))

if umur >= 20 :
    print ("Kamu boleh membuat sim")

else :
    print ("Kamu belum boleh membuat Sim")