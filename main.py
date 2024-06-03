# Membuat variable kosong dengan tipe data list
kontak = []

# Membuat fungsi yang digunakan untuk menginput data dari pengguna
def tambah_kontak():
  # Pengguna menginput nama
  nama = input("Masukkan nama: ")
  # Pengguna menginput nomor telepon
  nomor_hp = input("Masukkan nomor HP: ")
  # Pengguna menginput email namun bisa untuk tidak diisi (opsional)
  email = input("Masukkan email (optional): ")
  # Program menampilkan data yang dimasukkan pengguna
  kontak.append({"nama": nama, "nomor_hp": nomor_hp, "email": email})

# Membuat fungsi yang digunakan untuk mencari data dari variable kontak
def lihat_kontak():
  # Pernyataan jika di dalam variable kontak belum ada data
  if not kontak:
    # Maka akan menampilkan ini
    print("Belum ada kontak yang tersimpan.")
    # Mengembalikan nilai yang sudah di proses
    return
  # 
  for i, data_kontak in enumerate(kontak):
    print(f"{i+1}. {data_kontak['nama']} - {data_kontak['nomor_hp']}")
    if data_kontak["email"]:
      print(f"  Email: {data_kontak['email']}")

# Memebuat fungsi yang digunakan untuk mencari data dari variable kontak
def cari_kontak():
  # Pengguna memasukkan data yang akan di cari
  nama_dicari = input("Masukkan nama kontak yang ingin dicari: ")
  # Pernyataan jika data yang dicari tidak ada 
  ditemukan = False
  # Jika menemukan data yang dicari maka,
  for data_kontak in kontak:
    # Mengubah huruf kapital menjadi huruf kecil saat pengguna mencari data menggunakan huruf kapital di dalam variable data_kontak
    if nama_dicari.lower() in data_kontak["nama"].lower():
      # Menampilkan data yang dicari pengguna
      print(f"Nama: {data_kontak['nama']}")
      print(f"No HP: {data_kontak['nomor_hp']}")
      # Menampilkan email jika pada data tersebut terdapat email
      if data_kontak["email"]:
        print(f"Email: {data_kontak['email']}")
        # Pernyataan jika data yang dicari ada
      ditemukan = True
      break
    # Digunakan untuk menampilkan kepada pengguna jika data yang dicari tidak ditemukan
  if not ditemukan:
    print("Kontak tidak ditemukan.")

# Melakukan perulangan yang digunakan untuk pengguna memasukkan opsi
while True:
  # Digunakan untuk membuat line baru 
  print("\nMenu:")
  # Menampilkan opsi pertama
  print("1. Tambah Kontak")
  # Menampilkan opsi kedua
  print("2. Lihat Kontak")
  # Menampilkan opsi ketiga
  print("3. Cari Kontak")
  # Menampilkan opsi keempat
  print("4. Keluar")
  # Digunakan untuk pengguna memasukkan opsi
  pilihan = input("Masukkan pilihan: ")

# Membuat pernyataan untuk pengguna memasukkan opsi
  if pilihan == "1":
    tambah_kontak()
  elif pilihan == "2":
    lihat_kontak()
  elif pilihan == "3":
    cari_kontak()
    # Jika pengguna memasukkan opsi ini, maka program akan berhenti
  elif pilihan == "4":
    break
  # Jika pengguna memasukkan opsi yang tidak terdaftar, meskipun pengguna salah memasukkan input, perulangan akan tetap berjalan sampai pengguna memasukkan opsi untuk menghentikan program
  else:
    print("Pilihan tidak valid.")