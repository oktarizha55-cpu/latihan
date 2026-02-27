angka = int(input("nilai sebuah angka: "))

if angka > 0:
    print("angka tersebut bisa di katakan positif")
elif angka < 0:
    print("angka tersebut bisa di katakan negatif")
else:
    print("angka tersebut bisa di katakan nol")

################################################ lanjut 1
age = int(input("Masukkan usia Anda: "))
if age >= 17:
    print ("Anda sudah Dewasa")
if age < 17:
    print ("Anda masih Belum Dewasa")

################################################ Lanjut 2

int (input("Masukkan angka: "))
if angka > 0:
    print("angka tersebut bisa di katakan lebih besar dari nol")
if angka < 0:
    print("angka tersebut bisa di katakan lebih kecil dari nol")   

########################################1######## Lanjut 3

nilai1 = float(input("Masukkan nilai 1: "))
nilai2 = float(input("Masukkan nilai 2: "))
nilai3 = float(input("Masukkan nilai 3: "))

rata_rata = (nilai1 + nilai2 + nilai3) / 3

print("Rata-rata =", rata_rata)

################################################ Lanjut 4
# Input harga barang
harga = float(input("Masukkan harga barang: "))

# Cek apakah dapat diskon
if harga >= 100000:
    diskon = 0.10 * harga
else:
    diskon = 0

# Hitung total bayar
total_bayar = harga - diskon

# Tampilkan hasil
print("Diskon =", diskon)
print("Total bayar =", total_bayar)