nama = input("Masukkan nama pembeli: ")


total = float(input("Masukkan total belanja: "))


diskon = 0


if nama.lower() == "desi" or nama.lower() == "desta":
    diskon = 0.5
    
elif total >= 500000:
    diskon = 0.2
    
elif total >= 300000:
    diskon = 0.1
    

harga_akhir = total - (total * diskon)


print("Diskon yang didapat:", diskon * 100, "%")
print("Total bayar:", harga_akhir)

