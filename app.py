# \' >>> special karakter'
# \" >>> special karakter "
# \\ >>> special karakter \
# \n >>> Untuk new line / ganti baris
import math

print("hello \nbabby")
x = 2
y = 3
unit = 4
b = 4

# .upper() digunakan untuk mengkapitalkan semua huruf
# .lower() digunakan untuk mengkecilkan semua huruf
# .title() digunakan untuk menghuruf besar kan huruf pertama
# .find() digunakan untuk mengcari karakter ke berapa
# .replace() digunakan untuk mengganti huruf
# "" in Tipe data >> Digunakan untuk mencari benar apa salah karakter yang ada di variable (boolean.. true/false)
# "" not in Tipe data >> Digunakan untuk mencari benar apa salah karakter yang ada di variable (boolean.. true/false)


text_banyak = 'Hello im new here'
print(text_banyak.upper())
print(text_banyak.lower())
print(text_banyak.title())
print(text_banyak.find("im"))
print(text_banyak.replace("e", "o"))
print("im" in text_banyak)
print("im" not in text_banyak)


# mencetak banyaknya karakter
print(len(text_banyak))
# memilih karakter yang diinginkan dengan tanda "[]""
print(text_banyak[4])
print(text_banyak[-2])

# Mencetak gabungan nama
# tanda "{}" dapat diisi apa saja
# Contoh 1
awal = "Nalendra"
akhir = "Satria"
full = awal + " " + akhir
print(full)

# Contoh 2
awal = "Nalendra"
akhir = "Satria"
full = f"{awal} {akhir}"
print(full)


# input data
# x = input("x : ")
# y = int(x) + 1
# print(f"x: {x}, y: {y}")

# ord digunakan untuk mencari besar karakter dalam bentuk bilangan
# ord("c") >>>> 99


# if>>elif (Boolean)
# perhatikan setelah penulisan if .. baris kosong mempengaruhi program
temperature = 15
if temperature > 30:
    print("Panas")
    print("banget")
elif temperature > 20:
    print("Dingin")
else:
    print("its cold")
print("done")


age = 12
message = "Tua" if age >= 35 else "Muda"
print(message)


# Gerbang logika and or not
pintu = True
kaca = True
gelas = False

if (pintu and kaca) and not gelas:
    print("serasi")
else:
    print("tidak cocok")

# contoh operasi chaining

age = 5
if 18 <= age < 65:
    print("Masih muda")
else:
    print("unknown")

# loop
for number in range(1, 10, 5):
    print("peringatan", number, number * ".")

# loop 2
succesfull = True
for number in range(4):
    print("peringatan")
    if succesfull:
        print("Kesalahan")
        break
else:
    print("Berhasil")

# loop in loop
for x in range(3):
    for y in range(4):
        print(f"({x}, {y})")

# itterartion

shopping_cart = "dd"
for item in shopping_cart:
    print(item)

# range(1, 10) lompat 2

count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"we have {count} even number")

# fungsi


def nal():
    print("fungsi buatan sendiri")
    print("ini contoh ya")


nal()

# fungsi 2
# perintah "def" untuk membuat fungsi kita sendiri


def qbz(nama_awal, nama_akhir):  # berisi parameter
    print(f"Hallo {nama_awal} {nama_akhir}")
    print("Selamat Datang")


qbz("Nalendra", "Satria")  # ini berisi argumen


