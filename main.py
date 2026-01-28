import json
import os
from datetime import datetime

# File untuk menyimpan data tugas
DATA_FILE = "tugas.json"

def muat_tugas():
    """Memuat data tugas dari file JSON"""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []

def simpan_tugas(tugas_list):
    """Menyimpan data tugas ke file JSON"""
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(tugas_list, f, ensure_ascii=False, indent=2)
    print("✓ Data berhasil disimpan!")

def tambah_tugas(tugas_list):
    """Menambah tugas baru"""
    print("\n--- TAMBAH TUGAS BARU ---")
    nama_tugas = input("Nama tugas: ").strip()
    
    if not nama_tugas:
        print("❌ Nama tugas tidak boleh kosong!")
        return
    
    mata_pelajaran = input("Mata pelajaran: ").strip()
    
    # Input tanggal dengan validasi
    while True:
        try:
            tanggal = input("Tanggal input (DD-MM-YYYY): ").strip()
            datetime.strptime(tanggal, "%d-%m-%Y")
            break
        except ValueError:
            print("❌ Format tanggal salah! Gunakan DD-MM-YYYY")
    
    # Input deadline dengan validasi
    while True:
        try:
            deadline = input("Deadline (DD-MM-YYYY): ").strip()
            datetime.strptime(deadline, "%d-%m-%Y")
            break
        except ValueError:
            print("❌ Format tanggal salah! Gunakan DD-MM-YYYY")
    
    tugas_baru = {
        "id": len(tugas_list) + 1,
        "nama_tugas": nama_tugas,
        "mata_pelajaran": mata_pelajaran,
        "tanggal_input": tanggal,
        "deadline": deadline,
        "status": "Belum selesai"
    }
    
    tugas_list.append(tugas_baru)
    simpan_tugas(tugas_list)
    print(f"✓ Tugas '{nama_tugas}' berhasil ditambahkan!")

def tampilkan_tugas(tugas_list):
    """Menampilkan semua tugas"""
    if not tugas_list:
        print("\n❌ Tidak ada tugas. Daftar tugas kosong!")
        return
    
    print("\n" + "="*100)
    print(f"{'ID':<4} {'Nama Tugas':<25} {'Mata Pelajaran':<20} {'Tanggal Input':<15} {'Deadline':<15} {'Status':<15}")
    print("="*100)
    
    for tugas in tugas_list:
        print(f"{tugas['id']:<4} {tugas['nama_tugas']:<25} {tugas['mata_pelajaran']:<20} "
              f"{tugas['tanggal_input']:<15} {tugas['deadline']:<15} {tugas['status']:<15}")
    
    print("="*100)

def hapus_tugas(tugas_list):
    """Menghapus tugas berdasarkan ID"""
    tampilkan_tugas(tugas_list)
    
    if not tugas_list:
        return
    
    try:
        id_hapus = int(input("\nMasukkan ID tugas yang ingin dihapus: "))
        
        tugas_ditemukan = False
        for i, tugas in enumerate(tugas_list):
            if tugas['id'] == id_hapus:
                nama_tugas = tugas['nama_tugas']
                tugas_list.pop(i)
                
                # Update ID untuk tugas-tugas setelahnya
                for j in range(i, len(tugas_list)):
                    tugas_list[j]['id'] = j + 1
                
                simpan_tugas(tugas_list)
                print(f"✓ Tugas '{nama_tugas}' berhasil dihapus!")
                tugas_ditemukan = True
                break
        
        if not tugas_ditemukan:
            print(f"❌ Tugas dengan ID {id_hapus} tidak ditemukan!")
    
    except ValueError:
        print("❌ ID harus berupa angka!")

def ubah_status(tugas_list):
    """Mengubah status tugas menjadi selesai"""
    tampilkan_tugas(tugas_list)
    
    if not tugas_list:
        return
    
    try:
        id_ubah = int(input("\nMasukkan ID tugas yang sudah selesai: "))
        
        tugas_ditemukan = False
        for tugas in tugas_list:
            if tugas['id'] == id_ubah:
                tugas['status'] = "Selesai"
                simpan_tugas(tugas_list)
                print(f"✓ Status tugas '{tugas['nama_tugas']}' diubah menjadi Selesai!")
                tugas_ditemukan = True
                break
        
        if not tugas_ditemukan:
            print(f"❌ Tugas dengan ID {id_ubah} tidak ditemukan!")
    
    except ValueError:
        print("❌ ID harus berupa angka!")

def menu_utama():
    """Menampilkan menu utama"""
    while True:
        print("\n" + "="*50)
        print("       APLIKASI TODO LIST SEDERHANA")
        print("="*50)
        print("1. Tampilkan Daftar Tugas")
        print("2. Tambah Tugas Baru")
        print("3. Hapus Tugas")
        print("4. Ubah Status Tugas")
        print("5. Keluar")
        print("="*50)
        
        pilihan = input("Pilih menu (1-5): ").strip()
        
        tugas_list = muat_tugas()
        
        if pilihan == "1":
            tampilkan_tugas(tugas_list)
        elif pilihan == "2":
            tambah_tugas(tugas_list)
        elif pilihan == "3":
            hapus_tugas(tugas_list)
        elif pilihan == "4":
            ubah_status(tugas_list)
        elif pilihan == "5":
            print("\n👋 Terima kasih telah menggunakan Aplikasi TODO LIST!")
            break
        else:
            print("❌ Pilihan tidak valid! Silakan pilih 1-5")

if __name__ == "__main__":
    menu_utama()
