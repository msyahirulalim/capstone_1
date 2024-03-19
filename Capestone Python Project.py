#Capestone Python Project
from tabulate import tabulate
import sys

headers = ["Index", "Brand", "Name", "Stok", "Harga"]
list_mobil=[
            ['Toyota','Innova',3,550000],
            ['Toyota','Avanza',2,300000],
            ['Daihatsu','Xenia',2,350000],
            ['Mitsubishi','Pajero',2,1300000],
            ['Daihatsu','Terios',3,350000]
            ]
cart=[]

def menampilkan_mobil():
    if(len(list_mobil) > 0):
        print('Daftar Mobil\n')
        formatted_list_mobil = []
        for mobil in list_mobil:
            formatted_mobil = [mobil[0],mobil[1], mobil[2], "Rp. {:,.0f}".format(mobil[3])]  # Menggunakan format {:,.0f} untuk menambahkan titik pada satuan ribuan
            formatted_list_mobil.append(formatted_mobil)
        table = tabulate(formatted_list_mobil, headers=headers, tablefmt="grid", showindex=True)
        print(table)
    else:    
        print('Tidak ada stock mobil\n')
    
def mencari_mobil():
    try:
        if len(list_mobil) == 0:                                       #jika angka lebih dari panjang list makan print tidak ada mobil di list
            print("Data tidak ada di stok mobil")
            menu_a()
        else:
            indexMobil=int(input('Masukkan Index Mobil yang ingin dicari : '))
            if (indexMobil > len(list_mobil)-1):                                        #jika angka lebih dari panjang list makan print tidak ada mobil di list
                print("Data tidak ada. Masukkan indeks yang benar.")
                menu_a()
            elif indexMobil < 0:
                print("Indeks tidak boleh negatif. Silakan coba lagi.")
                return  #Kembali ke Sub Menu
            print('Daftar Mobil: ')
            mobil_data = [[indexMobil, *list_mobil[indexMobil]]]                    # Sisipkan indeks ke dalam data mobil
            print(tabulate(mobil_data, headers=headers, tablefmt="grid"))
    except ValueError:
        print("Input harus berupa angka. Silakan coba lagi.")

def menambah_mobil():
    indexMobil = int(input('Masukkan Index Mobil yang ingin ditambahkan: '))
    if indexMobil < 0 or indexMobil >= len(list_mobil)+1:
        print('Indeks tidak boleh Negatif atau\nIndeks yang dimasukkan melebihi data pada list mobil.\nMohon input kembali.')
        return  # Kembali ke submenu
    if 0 <= indexMobil < len(list_mobil):
        print('Daftar Mobil :')
        mobil_data = [[indexMobil, *list_mobil[indexMobil]]]
        print(tabulate(mobil_data, headers=headers, tablefmt="grid"))
        print('Index yang ingin ditambahkan sudah ada')
    else:
        brandMobil = input('Masukkan Brand Mobil: ')[:8]
        while not brandMobil.isalpha() or not brandMobil.strip():
            print("Nama merek mobil harus terdiri dari huruf dan tidak boleh kosong.")
            brandMobil = input('Masukkan Brand Mobil: ')[:8]
        
        namaMobil = input('Masukkan Nama Mobil: ')[:8]
        while not namaMobil.isalpha() or not namaMobil.strip():
            print("Nama mobil harus terdiri dari huruf dan tidak boleh kosong.")
            namaMobil = input('Masukkan Nama Mobil: ')[:8]

        while True:
            try:
                stockMobil = int(input('Masukkan Stok Mobil: '))
                if stockMobil <= 0:
                    print("Stok mobil tidak boleh negatif. Silahkan coba lagi.")
                else:
                    break
            except ValueError:
                print("Input harus berupa angka, mohon input kembali.")
        while True:
            try:
                hargasewaMobil = int(input('Masukkan Harga Sewa: '))
                if hargasewaMobil <= 0:
                    print("Harga sewa mobil tidak boleh negatif. Silakan coba lagi.")
                else:
                    break
            except ValueError:
                print("Input harus berupa angka, mohon input kembali.")

        print('Daftar Mobil Baru:')
        data_mobilBaru = [[indexMobil, brandMobil, namaMobil, stockMobil, hargasewaMobil]]
        print(tabulate(data_mobilBaru, headers=headers, tablefmt="grid"))
        
        while True:
            checker = input('Anda ingin menyimpan data yang sudah di input (Y/N): ').strip().upper()
            if checker == 'Y':
                list_mobil.append([brandMobil, namaMobil, stockMobil, hargasewaMobil])
                menampilkan_mobil()
                print("Data Tersimpan")
                break
            elif checker == 'N':
                print("Data Tidak Tersimpan")
                break
            else:
                print("Input tidak valid. Silakan masukkan 'Y' untuk ya atau 'N' untuk tidak.")

def mengupdateMobil():
    while True:
        try:
            index_Mobil=int(input('Masukkan Index Mobil yang ingin dicari : '))
            if index_Mobil < 0:
                print("Indeks tidak boleh negatif. Silakan coba lagi.")
                return  # Mengembalikan kontrol ke menu pemanggil
            if (index_Mobil > len(list_mobil)-1):                                        #jika angka lebih dari panjang list makan print tidak ada mobil di list
                print("Data tidak ada. Masukkan indeks yang benar.")
                menu_c()
            else:
                print('Daftar Mobil :')
                mobil_data = [[index_Mobil, *list_mobil[index_Mobil]]]                    # Sisipkan indeks ke dalam data mobil
                print(tabulate(mobil_data, headers=headers, tablefmt="grid"))
                while True:
                    checker = input('Anda ingin melanjutkan update data mobil (Y/N)  : ').strip().upper()
                    if checker == 'Y':
                        kolom_update = input("Masukkan Kolom yang ingin diupdate (Brand/Nama/Stok/Harga): ").strip().lower()
                        if kolom_update not in ["brand", "nama", "stok", "harga"]:
                            print("Kolom tidak valid.")
                            break

                        if 0 <= index_Mobil < len(list_mobil):
                            if kolom_update == "brand":
                                brand_mobil_baru = input("Masukkan Brand mobil baru: ")[:8]
                                while not brand_mobil_baru.isalpha() or not brand_mobil_baru.strip():
                                    print("Brand mobil harus terdiri dari huruf dan tidak boleh kosong.")
                                    brand_mobil_baru = input("Masukkan Brand mobil baru: ")[:8]
                                while True:
                                    checker = input('Anda ingin menyimpan data yang sudah di input (Y/N)  : ').strip().upper()
                                    if checker == 'Y':
                                        list_mobil[index_Mobil][0] = brand_mobil_baru
                                        print("Data Berhasil Diupdate.")
                                        menampilkan_mobil()
                                        menu_c()
                                    elif checker == 'N':
                                        print("Data Tidak Terupdate")
                                        menu_c()
                                    else:
                                        print("Input tidak valid. Silakan masukkan 'Y' untuk ya atau 'N' untuk tidak.")

                            elif kolom_update == "nama":
                                nama_mobil_baru = input("Masukkan nama mobil baru: ")[:8]
                                while not nama_mobil_baru.isalpha() or not nama_mobil_baru.strip():
                                    print("Brand mobil harus terdiri dari huruf dan tidak boleh kosong.")
                                    nama_mobil_baru = input("Masukkan nama mobil baru: ")[:8]
                                while True:
                                    checker = input('Anda ingin menyimpan data yang sudah di input (Y/N)  : ').strip().upper()
                                    if checker == 'Y':
                                        list_mobil[index_Mobil][1] = nama_mobil_baru
                                        print("Data Berhasil Diupdate.")
                                        menampilkan_mobil()
                                        menu_c()
                                    elif checker == 'N':
                                        print("Data Tidak Terupdate")
                                        menu_c()
                                    else:
                                        print("Input tidak valid. Silakan masukkan 'Y' untuk ya atau 'N' untuk tidak.")

                            elif kolom_update == "stok":
                                stok_mobil_baru = int(input("Masukkan jumlah stok mobil baru: "))
                                while True:
                                    if stok_mobil_baru <= 0:
                                        print("Stok mobil tidak boleh negatif. Silakan coba lagi.")
                                        stok_mobil_baru = int(input("Masukkan jumlah stok mobil baru: "))
                                    else:
                                        break
                                checker = input('Anda ingin menyimpan data yang sudah di input (Y/N)  : ').strip().upper()
                                if checker == 'Y':
                                    list_mobil[index_Mobil][2] = stok_mobil_baru
                                    print("Data Berhasil Diupdate.")
                                    menampilkan_mobil()
                                    menu_c()
                                elif checker == 'N':
                                    print("Data Tidak Terupdate")
                                    menu_c()
                                else:
                                    print("Input tidak valid. Silakan masukkan 'Y' untuk ya atau 'N' untuk tidak.")

                            elif kolom_update == "harga":
                                harga_sewa_baru = int(input("Masukkan harga sewa baru (Rp): "))
                                while True:
                                    if harga_sewa_baru <= 0:
                                        print("Harga sewa mobil tidak boleh negatif. Silakan coba lagi.")
                                        harga_sewa_baru = int(input("Masukkan harga sewa baru (Rp): "))
                                    else:
                                        break
                                checker = input('Anda ingin menyimpan data yang sudah di input (Y/N)  : ').strip().upper()
                                if checker == 'Y':
                                    list_mobil[index_Mobil][3] = harga_sewa_baru
                                    print("Data Berhasil Diupdate.")
                                    menampilkan_mobil()
                                    menu_c()
                                elif checker == 'N':
                                    print("Data Tidak Terupdate")
                                    menu_c()
                                else:
                                    print("Input tidak valid. Silakan masukkan 'Y' untuk ya atau 'N' untuk tidak.")
                            
                        else:
                            print("Data tidak ada di List")
                        break
                    elif checker == 'N':
                        menu_c()
                        break
                    else:
                        print("Input tidak valid. Silakan masukkan 'Y' untuk ya atau 'N' untuk tidak.")
                        break
        except ValueError:
            print("Input harus berupa angka. Silakan coba lagi.")
            
def menghapus_mobil():
    indexMobil = int(input('Masukkan Index Mobil yang ingin dihapus: '))
    if len(list_mobil) == 0:
        print("Stock Mobil Tidak Ada")
        return                                                                  #kembali ke sub menu
    while True:
        try:
            if 0 <= indexMobil < len(list_mobil):
                mobil_data = [[indexMobil, *list_mobil[indexMobil]]]                    # Sisipkan indeks ke dalam data mobil
                print(tabulate(mobil_data, headers=headers, tablefmt="grid"))
                print("Anda akan menghapus mobil dengan index:", indexMobil)
                checker = input('Apakah anda yakin ingin menghapus data mobil? (Y/N)  : ').strip().upper()
                if checker == 'Y':
                    del list_mobil[indexMobil]
                    print("Data Mobil telah dihapus.")
                    menampilkan_mobil()
                    menu_d()
                elif checker == 'N':
                    print("Penghapusan data dibatalkan.")
                    break
                else:
                    print("Pilihan tidak valid. Silakan masukkan Y untuk ya atau N untuk tidak.")
            else:
                print("Data tidak ada. Masukkan indeks yang benar.")
                menu_d()
        except ValueError:                                      
            print("Input harus berupa angka. Silakan coba lagi.")

def sewa_mobil():
    while True:
        try:
            menampilkan_mobil()
            indexMobil = int(input('Masukkan Index Mobil yang ingin disewa : '))
            if indexMobil < 0 or indexMobil >= len(list_mobil):
                print('Mohon input kembali, pastikan stok mobil ada')
                return  # Kembali ke submenu

            while True:
                if indexMobil < 0:
                    print("Angka yang dimasukkan tidak boleh negatif. Silakan coba lagi.")
                    indexMobil = int(input('Masukkan Index Mobil yang ingin disewa : '))
                else:
                    break
            qtyMobil = int(input('Masukkan jumlah yang ingin disewa : '))
            while True:
                if qtyMobil <= 0:
                    print("Harga sewa mobil tidak boleh negatif. Silakan coba lagi.")
                    qtyMobil = int(input('Masukkan jumlah yang ingin disewa : '))
                else:
                    break
        except ValueError:                                       # Memastikan yang di input merupakan angka
            print("Input harus berupa angka. Silakan coba lagi.")
            continue
        
        if indexMobil > len(list_mobil) - 1:
            print("Tidak ada stock Mobil di list")
            return
        elif list_mobil[indexMobil][2] == 0:
            print(f"Stock mobil {list_mobil[indexMobil][1]} kosong")
        elif qtyMobil > list_mobil[indexMobil][2]:
            print(f'Stock tidak cukup, stock {list_mobil[indexMobil][1]} tersisa {list_mobil[indexMobil][2]}')
        else:
            list_mobil[indexMobil][2] -= qtyMobil               # Mengurangi stok mobil yang disewa dari stok yang tersedia
            cart.append([list_mobil[indexMobil][0],list_mobil[indexMobil][1], qtyMobil, list_mobil[indexMobil][3], qtyMobil*list_mobil[indexMobil][3]])
            print('Isi Cart :')
            print(tabulate(cart, headers=["Brand","Nama","Stok","Harga","Jumlah"], tablefmt="grid"))
            while True:
                checker = input('Mau sewa mobil yang Lain? (Y/N)  : ').strip().upper()
                if checker == 'Y' or checker == 'N':
                    break
                else:
                    print("Input tidak valid. Silakan masukkan 'Y' untuk ya atau 'N' untuk tidak.")
            if checker != 'Y':
                print('Daftar Sewa :')
                print(tabulate(cart, headers=["Brand","Nama","Stok","Harga","Jumlah"], tablefmt="grid"))
                totalHarga = sum(item[2] * item[3] for item in cart)
                print(f'Total Harga: {totalHarga:,}')
                pembayaran(totalHarga)
                menu_e()
                break
            else:
                menampilkan_mobil()

def pembayaran(totalHargaYgHarusDibayar): 
    while True:
        print(f'Total yang harus dibayar = {totalHargaYgHarusDibayar:,}')
        try:
            jmlUang=int(input('Masukkan jumlah uang : '))
        except ValueError:                             # Memastikan yang di input merupakan angka
            print("Input harus berupa angka. Silakan coba lagi.")
            continue

        if(jmlUang>totalHargaYgHarusDibayar):
            kembali=jmlUang-totalHargaYgHarusDibayar
            print(f'Terimakasih \n Uang kembali anda : {kembali:,}')
            cart.clear()
            break
        elif(jmlUang==totalHargaYgHarusDibayar):
            print(f'Terimakasih')
            cart.clear()
            break
        else:
            kekurangan=totalHargaYgHarusDibayar-jmlUang
            print(f'Uang anda kurang sebesar {kekurangan}')
            pembayaran(kekurangan)
            break

def menu_utama():
    while True:
        try:
            menuUtama = int(input('''
                    Selamat Datang di Rental Mobil Wijaya
                        
                    Menu Utama:
                    1. Daftar Mobil
                    2. Menambah Mobil
                    3. Mengedit Mobil        
                    4. Menghapus Mobil
                    5. Sewa Mobil
                    6. Exit Program
                    Masukkan angka Menu yang ingin dijalankan :   '''))
            if menuUtama == 1:
                menu_a()
            elif menuUtama == 2:
                menu_b()
            elif menuUtama == 3:
                menu_c()    
            elif menuUtama == 4:
                menu_d()
            elif menuUtama == 5:
                menu_e()
            elif menuUtama == 6:
                print("Terima kasih telah menggunakan layanan kami.")
                sys.exit()
            else:
                print("Angka menu tidak valid. Silakan masukkan angka menu yang sesuai.")
        except ValueError:
            print("Input harus berupa angka. Silakan coba lagi.")

def menu_a():
    while True:
        try:
            menuDaftarMobil = int(input('''
                    List Menu:
                    1. List Mobil
                    2. Mencari Mobil
                    3. Kembali Menu Utama
                    Masukkan angka Menu yang ingin dijalankan:      '''))
            if menuDaftarMobil == 1:
                menampilkan_mobil()
            elif menuDaftarMobil == 2:
                mencari_mobil()
            elif menuDaftarMobil == 3:
                menu_utama()
                break
            else:
                print("Angka menu tidak valid. Silakan masukkan angka menu yang sesuai.")
        except ValueError:
            print("Input harus berupa angka. Silakan coba lagi.") 

def menu_b():
    while True:
        try:
            menutambahMobil = int(input('''
                    List Menu:
                    1. Menambah Mobil
                    2. Kembali Menu Utama
                    Masukkan angka Menu yang ingin dijalankan:      '''))
            if menutambahMobil == 1:
                menambah_mobil()
            elif menutambahMobil == 2:
                menu_utama()
                break
            else:
                print("Angka menu tidak valid. Silakan masukkan angka menu yang sesuai.")    
        except ValueError:
            print("Input harus berupa angka. Silakan coba lagi.")   

def menu_c():
    while True:
        try:
            menueditMobil = int(input('''
                    List Menu:
                    1. Update Data Mobil
                    2. Kembali Menu Utama
                    Masukkan angka Menu yang ingin dijalankan:      '''))
            if menueditMobil == 1:
                mengupdateMobil()
            elif menueditMobil == 2:
                menu_utama()
                break
            else:
                print("Angka menu tidak valid. Silakan masukkan angka menu yang sesuai.")    
        except ValueError:
            print("Input harus berupa angka. Silakan coba lagi.")

def menu_d():
    while True:
        try:
            menuhapusMobil = int(input('''
                    List Menu:
                    1. Hapus Data Mobil
                    2. Kembali Menu Utama
                    Masukkan angka Menu yang ingin dijalankan:      '''))
            if menuhapusMobil == 1:
                menghapus_mobil()
            elif menuhapusMobil == 2:
                menu_utama()
                break
            else:
                print("Angka menu tidak valid. Silakan masukkan angka menu yang sesuai.")    
        except ValueError:
            print("Input harus berupa angka. Silakan coba lagi.")

def menu_e():
    while True:
        try:
            sewaMobil = int(input('''
                    List Menu:
                    1. Sewa Mobil
                    2. Kembali Menu Utama
                    Masukkan angka Menu yang ingin dijalankan:      '''))
            if sewaMobil == 1:
                sewa_mobil()
            elif sewaMobil == 2:
                menu_utama()
                break
            else:
                print("Angka menu tidak valid. Silakan masukkan angka menu yang sesuai.")    
        except ValueError:
            print("Input harus berupa angka. Silakan coba lagi.") 

menu_utama()
