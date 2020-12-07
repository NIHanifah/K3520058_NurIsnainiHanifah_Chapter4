sewa1 = 200000
sewa2 = 10000
JamMulaiSewa = 6
JamSelesaiSewa = 23
MenitMulaiSewa = 0
MenitSelesaiSewa = 50

#Durasi sewa selama 17 jam
#50 menit terakhir tidak dihitung
#Karena belum mencapai satu jam

HargaJamSewa = (JamSelesaiSewa - JamMulaiSewa)
TotalSewa = sewa1 + ((HargaJamSewa - 12) * sewa2)
MenitSewa = MenitSelesaiSewa - MenitMulaiSewa
if HargaJamSewa == 12:
     print ("Harga Sewa = ", sewa1)
elif HargaJamSewa > 12:
    print ('Harga Sewa = ', TotalSewa )
elif HargaJamSewa > 12 and MenitSewa >= 60:
    print ('Harga Sewa = ', TotalSewa + sewa2)