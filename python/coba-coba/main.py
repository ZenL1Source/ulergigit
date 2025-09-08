
while True:
    # try:
        nilai = int(input("Berapa Nilai Ujian Kamu : "))

        if nilai > 100 or nilai < 0:
            print("Input Tidak Valid")

        elif nilai >= 90 :
            print ("nilai kamu A, Sangat Baik!")

        elif nilai >= 80 :
            print ("nilai kamu B, Baik")

        elif nilai >= 70 :
            print ("nilai kamu C, Cukup")

        elif nilai >= 60 :
            print ("nilai kamu D, Perlu usaha lebih")
        else :
            print ("nilai kamu E, Kamu Harus Belajar Lebih giat lagi!") 

        if 0 <= nilai <= 100:
            if nilai >= 70 :
                print("Status: Lulus✅")
        else :
            print ("Status: TIDAK LULUS ❌")

    # except ValueError:
        # print("⚠️ Harap masukkan angka!")

        ulang = input("Apakah kamu mau liat lagi?(y/n): ").lower()
        if ulang == 'n':
            print ("Program Telah Selesai. terimakasih!")
            break