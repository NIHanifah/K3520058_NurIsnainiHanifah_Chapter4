jarak = 795
tempuh1lt = 12
kapasitasTangki = 50

literBensinDiperlukan = jarak/tempuh1lt
print ("Bensin yang diperlukan = ", literBensinDiperlukan)
if literBensinDiperlukan <= 50:
    print ("Tidak Perlu Isi Bensin")
elif literBensinDiperlukan <= 100:
    print ('Isi Bensin Satu Kali')