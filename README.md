# Create Akun Facebook

Script otomatis untuk membuat akun Facebook baru menggunakan **Python**, **requests**, dan **Faker**.  
Dibuat untuk tujuan **pengujian**, **riset**, dan **pembelajaran otomasi web** — **bukan** untuk penyalahgunaan.

---

## 📌 Fitur
- Pendaftaran akun Facebook otomatis dengan data acak
- Random konfigurasi **nama**, **tanggal lahir**, dan **gender**

---

## ⚠️ Disclaimer
Penggunaan script ini sepenuhnya menjadi tanggung jawab pengguna.  
Hanya untuk tujuan **legal** dan sesuai **ketentuan layanan Facebook**.  

> **Catatan:** Verifikasi email harus dilakukan **secara manual** setelah akun dibuat.  
> Hindari penggunaan layanan **temp-mail publik**, karena memiliki risiko **tinggi diminta verifikasi ulang** atau akun diblokir.

---

## 💡 Tips Mengurangi Risiko Verifikasi
- Gunakan **email domain pribadi** atau **Gmail asli** (`@gmail.com`)
- Hindari membuat terlalu banyak akun dalam waktu singkat
- Jika menggunakan domain sendiri, buat akun hari ini dan lakukan verifikasi keesokan harinya (lebih aman)
- Lengkapi profil setelah akun dibuat (foto profil, skrol atau tonton reels)

---

## 🔧 Instalasi & Menjalankan

Pastikan perangkat sudah terpasang **Python 3.8+**.

```bash
pkg update -y
pkg install python git
git clone https://github.com/khamdihi-dev/fbcreate
cd fbcreate
pip install requests faker
python fbcreate.py
