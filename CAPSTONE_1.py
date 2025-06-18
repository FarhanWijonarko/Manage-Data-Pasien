

dataPasien = [
    ['alrafa', 'Ali', 'Rafa', 3174123456780001, 25, 'Pria', 'Dirawat', 'Jakarta'],
    ['mufgal', 'Mufid', 'Galang', 3275012345670002, 30, 'Pria', 'Sembuh', 'Bandung'],
    ['sisnur', 'Siska', 'Nurlaila', 3578123456780003, 28, 'Wanita', 'Dirawat', 'Surabaya'],
    ['rindyw', 'Rina', 'Dewi', 3476123456780004, 22, 'Wanita', 'Sembuh', 'Yogyakarta'],
    ['wianm22', 'Wijonarko', 'Wijonarko', 3378123456780005, 22, 'Pria', 'Dirawat', 'Semarang'],
    ['adiptr', 'Adi', 'Putra', 3274123456780006, 18, 'Pria', 'Dirawat', 'Bekasi'],
    ['lismrn', 'Lisna', 'Marni', 3174123456780007, 60, 'Wanita', 'Sembuh', 'Jakarta'],
    ['triynt', 'Tri', 'Yanti', 3375123456780008, 35, 'Wanita', 'Dirawat', 'Solo'],
    ['basyri', 'Basyir', 'Ridwan', 3278123456780009, 45, 'Pria', 'Sembuh', 'Bogor'],
    ['dinkml', 'Dinda', 'Kemala', 3376123456780010, 27, 'Wanita', 'Dirawat', 'Malang'],
    ['ridman', 'Ridho', 'Iman', 3178123456780011, 40, 'Pria', 'Sembuh', 'Depok'],
    ['zahrna', 'Zahra', 'Nabila', 3279123456780012, 16, 'Wanita', 'Dirawat', 'Tangerang'],
    ['fernda', 'Ferry', 'Anda', 3378123456780013, 50, 'Pria', 'Dirawat', 'Makassar'],
    ['salima', 'Salsa', 'Salim', 3478123456780014, 31, 'Wanita', 'Sembuh', 'Banjarmasin'],
    ['rahmna', 'Rahman', 'Naufal', 3579123456780015, 29, 'Pria', 'Dirawat', 'Palembang'],
    ['fikriy', 'Fikri', 'Yusuf', 3277123456780016, 33, 'Pria', 'Dirawat', 'Medan'],
    ['syhnna', 'Syahnaz', 'Najwa', 3179123456780017, 21, 'Wanita', 'Sembuh', 'Padang'],
    ['johsmi', 'Johan', 'Smith', 3374123456780018, 63, 'Pria', 'Sembuh', 'Pekanbaru'],
    ['lilikh', 'Lili', 'Khasanah', 3276123456780019, 41, 'Wanita', 'Dirawat', 'Cirebon'],
    ['danasd', 'Dana', 'Sudirman', 3178123456780020, 58, 'Pria', 'Dirawat', 'Cilacap'],
    ['anismt', 'Anisa', 'Mutiara', 3279123456780021, 19, 'Wanita', 'Sembuh', 'Bekasi'],
    ['fahmin', 'Fahmi', 'Nur', 3379123456780022, 26, 'Pria', 'Sembuh', 'Bogor'],
    ['safani', 'Safa', 'Nisa', 3479123456780023, 55, 'Wanita', 'Dirawat', 'Solo'],
    ['alwinr', 'Alwi', 'Nur', 3579123456780024, 38, 'Pria', 'Dirawat', 'Surabaya'],
    ['nurfit', 'Nuri', 'Fitriani', 3274123456780025, 44, 'Wanita', 'Sembuh', 'Semarang'],
    ['dikiwk', 'Diki', 'Wicaksono', 3378123456780026, 23, 'Pria', 'Sembuh', 'Yogyakarta'],
    ['rismaw', 'Risma', 'Widya', 3174123456780027, 17, 'Wanita', 'Dirawat', 'Depok'],
    ['hndyna', 'Hendy', 'Nanda', 3276123456780028, 36, 'Pria', 'Dirawat', 'Tangerang'],
    ['sylvnm', 'Sylvia', 'Naomi', 3477123456780029, 20, 'Wanita', 'Sembuh', 'Jakarta'],
    ['harvsy', 'Harvy', 'Syah', 3578123456780030, 59, 'Pria', 'Dirawat', 'Bekasi'],
    ['melati', 'Mela', 'Tika', 3379123456780031, 65, 'Wanita', 'Dirawat', 'Bandung'],
]

dataPasienSatuan = []





def dataStatistik(jumlah,umurKurang18,umur18_30,umur30_60,umurLebih60,pria,wanita,dirawat,sembuh,rata2Umur,umurKu):
    print('\n======== Data Statistik ========')
    print(f'''
Jumlah Pasien     : {jumlah} Pasien
Jumlah Pria       : {pria} Pasien
Jumlah Wanita     : {wanita} Pasien
    ''')
    print(f'''Rata - Rata Umur  : {round((rata2Umur/jumlah),2)} Tahun
Umur Termuda      : {min(umurKu)} Tahun
Umur Tertua       : {max(umurKu)} Tahun
          ''')
    print(f'''Distribusi Umur   
- 1-18 Tahun      : {umurKurang18} Pasien
- 18-30 Tahun     : {umur18_30} Pasien
- 30-60 Tahun     : {umur30_60} Pasien
- <= 60 Tahun     : {umurLebih60} Pasien
          ''')
    
    print(f'''Status Kesehatan
- Dirawat         : {dirawat} Pasien ({round(((dirawat/jumlah)*100),2)}%)
- Sembuh          : {sembuh} Pasien ({round(((sembuh/jumlah)*100),2)}%)
           ''') 
    
def data(idPasien, inputNamaDepan, inputNamaBelakang, nik, inputUmur, inputGender, inputKesehatan, inputAlamat):
    dataPasienSementar = []
    
    dataPasienSementar.append(idPasien)
    dataPasienSementar.append(inputNamaDepan.capitalize())
    dataPasienSementar.append(inputNamaBelakang.capitalize())
    dataPasienSementar.append(nik)
    dataPasienSementar.append(inputUmur)
    dataPasienSementar.append(inputGender.capitalize())
    dataPasienSementar.append(inputKesehatan.capitalize())    
    dataPasienSementar.append(inputAlamat)
    dataPasien.append(dataPasienSementar) 
    return dataPasien

def tabelPasien():
    print('\n======== Data Pasien ========\n')
    print('\nNO | ID         | Nama Depan      | Nama Belakang   | NIK              | Umur  | Gender     | Status Kesehatan | Alamat')
    print('==========================================================================================================================')
    for pasien in range(len(dataPasien)): 
        print(f"{str(pasien + 1).ljust(2)} | {dataPasien[pasien][0].ljust(10)} | {dataPasien[pasien][1].ljust(15)} | {dataPasien[pasien][2].ljust(15)} | {str(dataPasien[pasien][3]).ljust(5)} | {str(dataPasien[pasien][4]).ljust(5)} | {dataPasien[pasien][5] .ljust(10)} | {dataPasien[pasien][6] .ljust(16)} | {dataPasien[pasien][7]}")

def tabelPasienSatuan():
    print('\n======== Data Pasien Berdasarkan ID ========\n')
    print('\nNO | ID         | Nama Depan      | Nama Belakang   | NIK              | Umur  | Gender     | Status Kesehatan | Alamat')
    print('==========================================================================================================================')
    for pasien in range(len(dataPasienSatuan)): 
        print(f"{str(pasien + 1).ljust(2)} | {dataPasienSatuan[pasien][0].ljust(10)} | {dataPasienSatuan[pasien][1].ljust(15)} | {dataPasienSatuan[pasien][2].ljust(15)} | {str(dataPasienSatuan[pasien][3]).ljust(5)} | {str(dataPasienSatuan[pasien][4]).ljust(5)} | {dataPasienSatuan[pasien][5] .ljust(10)} | {dataPasienSatuan[pasien][6] .ljust(16)} | {dataPasienSatuan[pasien][7]}")
def updateDataPasien(index):
    tabelPasienSatuan()
    inputNamaDepan = input('\nMasukan Nama Depan : ')
    inputNamaBelakang = input('Masukan Nama Belakang : ')
    while True:
        try:
            
            inputUmur = int(input('Masukan Umur Pasien : '))
            if inputUmur < 1:
                print('Umur Tidak Boleh Negatif dan Nol')
                continue
            break   
        except ValueError:
            print('Umur Harus Berupa Angka')
    while True:
        inputGender = str(input('Masukan Gender Pasien Pria / Wanita : '))
        if inputGender.lower() == 'pria' or inputGender.lower() == 'wanita':
            break
        else:
            print('Pilihan Tidak Tersedia')
    inputAlamat = input('Masukan Alamat Pasien : ')
    
    index[1] = inputNamaDepan
    index[2] = inputNamaBelakang
    index[4] = inputUmur
    index[5] = inputGender
    index[7] = inputAlamat
    
    print('\n======== Data Berhasil Diupdate ========')
    
    
    dataPasienSatuan.clear()

def deleteDataPasien(inputIdPasien):    
    for i, pasien in enumerate(dataPasien):
        if inputIdPasien == pasien[0].lower():
            dataPasienSatuan.append(pasien)
            tabelPasienSatuan()

            print('''
                    1. Hapus Data Pasien
                    2. Batal''')
            while True:
                try:
                    inputPilihan = input('\nMasukan Pilihan : ')
                    if inputPilihan == '1':
                        del dataPasien[i]
                        dataPasienSatuan.clear()
                        print('\n======== Data Berhasil Dihapus ========')
                        break
                    elif inputPilihan == '2':
                        dataPasienSatuan.clear()
                        print('\n======== Data Tidak Dihapus ========')
                        break
                    else:
                        print('Pilihan Tidak Tersedia')
                except ValueError:
                    print('Pilihan Tidak Tersedia')
                    continue
           

while True:
    print('''
        Manage Data Pasien
        
        1. Menambahkan Data Pasien
        2. Melihat Data Pasien
        3. Update Data Pasien
        4. Hapus Data Pasien
        5. Statistik Data Pasien
        6. Keluar
        ''')
    menuPilihan = input('Masukan Pilihan : ')
    if menuPilihan == '1': 
        while True:
            print('''
              \n======== Menu Tambah Data Pasien ========\n
              1. Tambah Data Pasien
              2. Kembali
              ''')
            try:
                inputPilihan = input('\nMasukan Pilihan 1 / 2 : ')
                if inputPilihan == '1':
                    print('\n======== Tambah Data Pasien ========\n')
                    inputNamaDepan = input('Masukan Nama Depan : ')
                    inputNamaBelakang = input('Masukan Nama Belakang : ')
                    while True:
                        try:
                            nik = int(input('Masukan NIK Pasien : '))
                            if len(str(nik)) != 16:
                                print('NIK Harus 16 Angka')
                                continue
                            break
                        except ValueError:
                            print('NIK Harus Berupa Angka')
                    while True:
                        try:
                            inputUmur = int(input('Masukan Umur Pasien : '))
                            if inputUmur < 1:
                                print('Umur Tidak Boleh Negatif dan Nol')
                                continue
                            break   
                        except ValueError:
                            print('Umur Harus Berupa Angka')
                    while True:
                        inputGender = str(input('Masukan Gender Pasien Pria / Wanita : '))
                        if inputGender.lower() == 'pria' or inputGender.lower() == 'wanita':
                            break
                        else:
                            print('Pilihan Tidak Tersedia')
                    while True:
                        try:
                            inputKesehatan = input('Status Pasien Dirawat / Sembuh : ')
                            if inputKesehatan.lower() == 'dirawat' or inputKesehatan.lower() == 'sembuh':
                                break
                            else:
                                print('Pilihan Tidak Tersedia')
                        except ValueError:
                            print('Pilihan Tidak Tersedia')
                    inputAlamat = input('Masukan Alamat Pasien : ')
                    idPasien = (inputNamaBelakang[:2] + inputNamaDepan[-2:] + str(nik)[4:7] + str(inputUmur))
                    for index in range(len(dataPasien)):
                        if idPasien.lower() == dataPasien[index][0].lower():
                            print('\n======== ID Pasien Sudah Terdaftar ========')
                            break
                    else:
                        dataSementar = [idPasien, inputNamaDepan, inputNamaBelakang, nik, inputUmur, inputGender, inputKesehatan, inputAlamat]
                        dataPasienSatuan.append(dataSementar)
                        while True:
                            tabelPasienSatuan()
                            validasiSave = input('\nApakah Data Mau Di Simpan ? (Y/N) : ')
                            if validasiSave.lower() == 'y':
                                data(idPasien, inputNamaDepan, inputNamaBelakang, nik, inputUmur, inputGender, inputKesehatan, inputAlamat)
                                print('\n======== Data Berhasil Ditambahkan ========')
                                dataPasienSatuan.clear()
                                break
                            elif validasiSave.lower() == 'n':
                                print('\n======== Data Tidak Disimpan ========')
                                dataPasienSatuan.clear()
                                break
                            else:
                                print('Pilihan Tidak Tersedia')
                elif inputPilihan == '2':
                    break
                else:
                    print('Pilihan Tidak Tersedia')
            except ValueError:
                print('Pilihan Tidak Tersedia')
                continue
        
    elif menuPilihan == '2':
        if len(dataPasien) == 0:
            tabelPasien()
            print('\n======== Data Pasien Kosong ========')
            continue
        while True:
            print('''
            \n======== Menu Melihat Data Pasien ========\n
            1. Menampilkan Semua Data Pasien
            2. Menampilkan Data Pasien Berdasarkan ID
            3. Tampilkan Data Pasien Berdasarkan Status Kesehatan
            4. kembali''')
            try:
                pilihanRead = int(input('\nMasukan Pilihan 1 / 2 / 3 / 4 : '))
                if pilihanRead == 1:
                    tabelPasien()
                elif pilihanRead == 2:
                    tabelPasien()
                    while True:
                        inputData = input('\nMasukan ID Pasien : ').lower()
                        for index in range(len(dataPasien)):
                            if inputData.lower() == dataPasien[index][0].lower():
                                dataPasienSatuan.append(dataPasien[index])
                                tabelPasienSatuan()
                                dataPasienSatuan.clear()
                                break
                        else:
                            print('\n======== Data Tidak Ditemukan ========\n')
                            continue
                        break
                elif pilihanRead == 3:
                    while True:
                        try:
                            inputDataKesehatan = input('\nMasukan Status Kesehatan Dirawat / Sembuh : ').lower()
                            if inputDataKesehatan.lower() == 'dirawat' or inputDataKesehatan.lower() == 'sembuh':
                                for index in range(len(dataPasien)):
                                    if inputDataKesehatan.lower() == dataPasien[index][6].lower():
                                        dataPasienSatuan.append(dataPasien[index])
                                if len(dataPasienSatuan) == 0:
                                    tabelPasienSatuan()
                                    print('\n======== Data Pasien Kosong ========')
                                else:
                                    tabelPasienSatuan()
                                    dataPasienSatuan.clear()
                                break
                            else:
                                print('Pilihan Tidak Tersedia')
                        except ValueError:
                            print('Pilihan Tidak Tersedia')
                elif pilihanRead == 4:
                    break
                else:
                    print('Pilihan Tidak Tersedia')
                    
            except ValueError:
                print('Pilihan Tidak Tersedia')
    elif menuPilihan == '3':
        if len(dataPasien) == 0:
            tabelPasien()
            print('\n======== Data Pasien Kosong ========')
        else:
            while True:
                tabelPasien()
                try:
                    print('''
                    \n======== Menu Update Data Pasien ========\n
                    1. Update Data Pasien
                    2. Update Data Kesehatan Pasien
                    3. Kembali
                    ''')
                    subMenuPilihan = int(input('\nMasukan Pilihan 1 / 2 / 3 : '))
                    if subMenuPilihan == 1:
                        while True:
                            inputIdPasien = input('\nMasukan ID Pasien : ').lower()
                            for index in range(len(dataPasien)):
                                if inputIdPasien.lower() == dataPasien[index][0].lower():
                                    dataPasienSatuan.append(dataPasien[index])
                                    while True:
                                        try:
                                            inputPilihan = str(input('\nLanjut Update Data Pasien ? (Y/N) : ')).lower()
                                            if inputPilihan == 'y':
                                                updateDataPasien(dataPasien[index])
                                                break
                                            elif inputPilihan == 'n':
                                                dataPasienSatuan.clear()
                                                print('\n======== Data Tidak Diupdate ========')
                                                break
                                        except ValueError:
                                            print('Pilihan Tidak Tersedia')
                                    
                                    break
                            else:
                                print('\n======== Data Tidak Ditemukan ========\n')
                                dataPasienSatuan.clear()
                                continue
                            break
                    elif subMenuPilihan == 2:
                        while True:
                            try:
                                inputIdPasien = input('\nMasukan ID Pasien : ').lower()
                                for index in range(len(dataPasien)):
                                    if inputIdPasien.lower() == dataPasien[index][0].lower():
                                        dataPasienSatuan.append(dataPasien[index])
                                        while True:
                                            try:
                                                tabelPasienSatuan()
                                                inputKesehatan = str(input('\nMasukan Status Kesehatan Dirawat / Sembuh : ')).lower()
                                                if inputKesehatan.lower() == 'dirawat' or inputKesehatan.lower() == 'sembuh':
                                                    while True:
                                                        try:
                                                            inputPilihan = str(input('\nLanjut Update Status Kesehatan ? (Y/N) : ')).lower()
                                                            if inputPilihan == 'y':
                                                                dataPasien[index][6] = inputKesehatan
                                                                print('\n======== Data Berhasil Diupdate ========')
                                                                dataPasienSatuan.clear()
                                                                break
                                                            elif inputPilihan == 'n':
                                                                print('\n======== Data Tidak Diupdate ========')
                                                                dataPasienSatuan.clear()
                                                                break
                                                        except ValueError:
                                                            print('Pilihan Tidak Tersedia')
                                                    break
                                                else:
                                                    print('Pilihan Tidak Tersedia')
                                            except ValueError:
                                                print('Pilihan Tidak Tersedia')
                                        break
                                else:
                                    print('\n======== Data Tidak Ditemukan ========\n')
                                    dataPasienSatuan.clear()
                                    continue
                                break
                            except ValueError:
                                print('Pilihan Tidak Tersedia')     
                    elif subMenuPilihan == 3:
                        break
                    else:
                        print('Pilihan Tidak Tersedia')
                except ValueError:
                    print('Pilihan Tidak Tersedia')    
            
    elif menuPilihan == '4':
        while True:
            print('''
            \n======== Menu Hapus Data Pasien ========\n
            1. Menghapus Data Pasien
            2. Kembali
            ''')
            try:
                pilihanRead = int(input('\nMasukan Pilihan 1 / 2 : '))
                if pilihanRead == 1:
                    if len(dataPasien) == 0:
                        tabelPasien()
                        print('\n======== Data Pasien Kosong ========')
                        continue
                    tabelPasien()
                    while True:        
                        try:
                            inputIdPasien = input('\nMasukan ID Pasien : ').lower()
                            for index in dataPasien:
                                if inputIdPasien.lower() == index[0].lower():
                                    deleteDataPasien(inputIdPasien)
                                    break
                            else:
                                print('\n======== Data Tidak Ditemukan ========\n')
                                dataPasienSatuan.clear()
                                continue
                            
                        except ValueError:
                            print('\n======== Data Tidak Ditemukan ========\n')     
                            break
                        break
                elif pilihanRead == 2:
                    break
                else:
                    print('Pilihan Tidak Tersedia')
                    
            except ValueError:
                print('Pilihan Tidak Tersedia')
    elif menuPilihan == '5':
        umurKu = []
        rata2Umur = 0
        umurKurang18 = 0 
        umur18_30 = 0
        umur30_60 = 0
        umurLebih60 = 0
        pria = 0
        wanita = 0  
        dirawat = 0
        sembuh = 0
        if len(dataPasien) == 0:
            print('\n======== Data Pasien Kosong ========')
            continue
        for i in range(len(dataPasien)):
            umur = dataPasien[i][4]
            gender = dataPasien[i][5]
            kesehatan = dataPasien[i][6]
            jumlah = i + 1
            if umur != 0:
                rata2Umur += umur
                umurKu.append(umur)
            if umur < 18 :
                umurKurang18 += 1
                umurKu.append(umur)
            elif 18 <= umur < 30:
                umur18_30 += 1
                umurKu.append(umur)
            elif 30 <= umur < 60:
                umur30_60 += 1
                umurKu.append(umur)
            elif umur >= 60:
                umurLebih60 += 1
                umurKu.append(umur)

            if gender.lower() == 'pria':
                pria += 1
            elif gender.lower() == 'wanita':
                wanita += 1
            
            if kesehatan.lower() == 'dirawat':
                dirawat += 1
            elif kesehatan.lower() == 'sembuh':
                sembuh += 1
        dataStatistik(jumlah,umurKurang18,umur18_30,umur30_60,umurLebih60,pria,wanita,dirawat,sembuh,rata2Umur,umurKu) 

    elif menuPilihan == '6':
        endPilihan = input('\nApakah Anda Yakin Ingin Keluar ? (Y/N) : ').lower()
        if endPilihan == 'y':
            print('\n======== Terima Kasih ========\n')
            break
        elif endPilihan == 'n':
            continue
        else:            
            print('Pilihan Tidak Tersedia')
    else:
        print('Pilihan Tidak Tersedia')
        
        
        
        