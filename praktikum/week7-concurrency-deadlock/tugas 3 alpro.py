nama = input("Masukkan nama pembeli: ")
# Input nama pembeli.

total = float(input("Masukkan total belanja: "))
# Input total belanja.

diskon = 0
# Variabel untuk menyimpan besar diskon.

if nama.lower() == "desi" or nama.lower() == "desta":
    diskon = 0.5
    # Nama Desi atau Desta → diskon 50%.
elif total >= 500000:
    diskon = 0.2
    # Belanja ≥ 500.000 → diskon 20%.
elif total >= 300000:
    diskon = 0.1
    # Belanja ≥ 300.000 → diskon 10%.

harga_akhir = total - (total * diskon)
# Menghitung harga akhir setelah diskon.

print("Diskon yang didapat:", diskon * 100, "%")
print("Total bayar:", harga_akhir)
# Menampilkan diskon dan total bayar.
