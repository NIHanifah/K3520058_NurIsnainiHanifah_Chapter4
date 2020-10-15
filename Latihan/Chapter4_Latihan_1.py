sewa1 = 200000
sewa2 = 10000
JamMulaiSewa = 6
JamSelesaiSewa = 23
MenitMulaiSewa = 0
MenitSelesaiSewa = 50

HargaJamSewa = (JamSelesaiSewa - JamMulaiSewa)
TotalSewa = sewa1 + ((HargaJamSewa - 12) * sewa2)
MenitSewa = MenitSelesaiSewa - MenitMulaiSewa
if HargaJamSewa == 12:
     print ("Harga Sewa = ", sewa1)
elif HargaJamSewa > 12 and MenitSewa < 30:
    print ('Harga Sewa = ', TotalSewa )
elif HargaJamSewa > 12 and MenitSewa >= 30:
    print ('Harga Sewa = ', TotalSewa + sewa2)