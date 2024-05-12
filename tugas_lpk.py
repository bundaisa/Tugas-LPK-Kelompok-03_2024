import streamlit as st

#PEMBUKAAN
st.image("Ester Moon.jpg")
st.title (':blue[ESTER MOON]')
st.header ('Selamat Datang di Ester Moon')

#MEMBUAT TAB
Home, Materi_Praktik_Titrimetri , Perhitungan_Titrimetri, Materi_Praktik_kimia_Organik = st.tabs(["Home", "Materi Praktik Titrimetri", "Perhitungan Titrimetri", "Materi Praktik Kimia Organik"])

#KONTEN UNTUK TAB 1
with Home:
    st.header('Apa Itu Ester Moon?')
    st.write('Ester Moon adalah aplikasi web yang bergerak dalam menyediakan bahan ajar berupa kumpulan materi praktikum analisis titrimetri dan kimia organik. Materi praktikum yang tersedia merupakan materi dasar yang dapat mengasah skill analis dalam bidang analitik. Selain materi praktikum, aplikasi web ini menyediakan fitur berupa kalkulator perhitungan konsentrasi dan normalitas larutan untuk standardisasi. Dengan adanya aplikasi web ini analis akan lebih mudah dalam mengakses bahan ajar praktikum, karena bahan ajar yang tersedia sangat fleksibel dan bisa diakses kapan saja.')

    st.header('Kelompok 03')

    st.markdown ('**Nama Anggota:**')
    st.write('1. Deficha Tania E. P. (2360097)')
    st.write('2. Febyona Khairunnisa (2360127)')
    st.write('3. Fern Silvy S. N.    (2360128)')
    st.write('4. Istiqomah Salsabil  (2360149)')
    st.write('5. Maria Fransiska     (2360166)')


#KONTEN UNTUK TAB 2
with Materi_Praktik_Titrimetri:
   
    st.header("Materi Praktik Titrimetri")
    opsi1 = ('Pilih Materi Praktik Titrimetri', 'Percobaan 1. Pemilihan Indikator Asam Basa','Percobaan 2. Standardisasi Asam Basa', 'Percobaan 3. Standardisasi Larutan KMnO4', 'Percobaan 4. Standardisasi Larutan Tiosulfat')

    pilihan1 = st.selectbox('Pilih Materi Praktik Titrimetri:', opsi1)
    
#KONTEN UNTUK MATERI TITRIMETRI
    if pilihan1 == 'Pilih Materi Praktik Titrimetri':
         st.title ('')

    elif pilihan1 == 'Percobaan 1. Pemilihan Indikator Asam Basa':
        st.title ('Pemilihan Indikator Untuk Titrasi Asam Basa')
        st.header (' a. Tujuan')
        st.write ('Untuk menentukan atau memilih indikator asam-basa yang sesuai mekanisme reaksi asam-basa dan peruntukannya (Asidimetri-Alkalimetri) dengan benar.')
        st.header ('b. Prinsip')
        st.write ( 'Indikator asam-basa adalah senyawa asam-asam atau basa-basa organik lemah dimana bentuk molekulnya yang tidak terionisasi mempunyai warna yang berlainan dari pada warna ionnya.')
        st.header ('c. Alat dan Bahan')
        st.markdown ('**Alat:** ')
        st.write ('Pada percobaan ini alat yang digunakan adalah Buret makro, statip, Klem buret, Alas titar, Bulb hitam/merah, labu semprot, Erlenmeyer 250 mL, pipet volumetri 25 mL, pipet tetes, corong, piala gelas 250 mL.')
        st.markdown ('**Bahan:**')
        st.write ('Bahan yang digunakan Larutan HCl 0,1 N, NaOh 0,1 N, CH3COOH 0,1 N, dan NH4OH 0,1 N. Sedangkan indikator yang digunakan adalah iNDIKATOR SM, MM, BTB dan PP')
        st.header ('d. Prosedur')
        st.markdown ('**1. Titrasi Asam Kuat oleh Basa Kuat**')
        st.write('Dipipet 25 mL larutan HCl 0,1 N kedalam masing-masing erlenmeyer 250 mL, tambahkan pada masig-masing erlenmeyer 2-3 tetes indikator PP,BTB,MM, dan SM. Kemudian titar dengan larutan NaOH 0,1 N, dilakukan duplo atau triplo. Amati titik akhir titrasi dan catat volume titran yang digunakan.')
        st.markdown ('**2. Titrasi Asam Lemah oleh Basa Kuat**')
        st.write('Dipipet 25 mL larutan CH3COOH 0,1 N kedalam masing-masing erlenmeyer 250 mL, tambahkan pada masig-masing erlenmeyer 2-3 tetes indikator PP,BTB,MM, dan SM. Kemudian titar dengan larutan NaOH 0,1 N, dilakukan duplo atau triplo. Amati titik akhir titrasi dan catat volume titran yang digunakan.')
        st.markdown ('**3. Titrasi Basa Kuat oleh Asam Kuat**')
        st.write('Dipipet 25 mL larutan NaOH 0,1 N kedalam masing-masing erlenmeyer 250 mL, tambahkan pada masig-masing erlenmeyer 2-3 tetes indikator PP,BTB,MM, dan SM. Kemudian titar dengan larutan HCl 0,1 N, dilakukan duplo atau triplo. Amati titik akhir titrasi dan catat volume titran yang digunakan.')
        st.markdown ('**4. Titrasi Basa Lemah oleh Basa Kuat**')
        st.write('Dipipet 25 mL larutan NH4OH 0,1 N kedalam masing-masing erlenmeyer 250 mL, tambahkan pada masig-masing erlenmeyer 2-3 tetes indikator PP,BTB,MM, dan SM. Kemudian titar dengan larutan HCl 0,1 N, dilakukan duplo atau triplo. Amati titik akhir titrasi dan catat volume titran yang digunakan.')

        st.header("Data Pengamatan:")
        opsi2 = ('Pilih Data Pengamatan','1. Titrasi Asam Kuat oleh Basa Kuat', '2. Titrasi Asam Lemah oleh Basa Kuat', '3. Titrasi Basa Kuat oleh Asam Kuat', '4. Titrasi Basa Lemah oleh Asam Kuat')

        pilihan2 = st.selectbox('Pilih Data Pengamatan:', opsi2)

        if pilihan2 == 'Pilih Data Pengamatan':
             st.title('')

        elif pilihan2 == '1. Titrasi Asam Kuat oleh Basa Kuat':    
                def main():
                    st.title('Contoh Tabel Data Streamlit')

                    st.write('data')

                # Menampilkan tabel
                st.markdown('**Data Pengamatan Titrasi Asam Kuat oleh Basa Kuat**')
                data_table=[
                {'Indikator': 'MM', 'Perubahan Warna': 'Merah menjadi kuning ( dengan warna antara jingga)'}, 
                {'Indikator': 'BTB', 'Perubahan Warna': 'Kuning menjadi biru (dengan warna antra hijau)'}, {'Indikator': 'PP', 'Perubahan Warna': 'Larutan tidak berwarna menjadi merah muda '}
                ]
                st.table(data_table)

                st.markdown('**Pembahasan**')
                st.write('Indikator BTB : Berada dibagian yang curam dan mencakup titik ekuivalen') 
                st.write ('Indikator PP : masih dibagian yang curam dan melewati titik ekuivalen')

                
        elif pilihan2 == '2. Titrasi Asam Lemah oleh Basa Kuat':    
                def main():
                    st.title('Contoh Tabel Data Streamlit')

                    st.write('data')

              #MEMBUAT TABEL DENGAN st.table()
                st.markdown('**Data Pengamatan Titrasi Asam Lemah oleh Basa Kuat**')
                data_table = [ 
                {'Indikator': 'MM', 'Perubahan Warna': 'Merah menjadi kuning ( dengan warna antara jingga)'}, 
                {'Indikator': 'BTB', 'Perubahan Warna': 'Kuning menjadi biru (dengan warna antra hijau)'}, {'Indikator': 'PP', 'Perubahan Warna': 'Larutan tidak berwarna menjadi merah muda '} 
                ]
                st.table(data_table)

                st.markdown('**Pembahasan**')
                st.write('Indikator PP : berada dibagian yang curam dan mencakup titik ekuivalen') 

        elif pilihan2 == '3. Titrasi Basa Kuat oleh Asam Kuat':    
                def main():
                    st.title('Contoh Tabel Data Streamlit')

                    st.write('data')
            
              #MEMBUAT TABEL DENGAN st.table()
                st.markdown('**Data Pengamatan Titrasi Basa Kuat oleh Asam Kuat**')
                data_table = [ 
                {'Indikator': 'BTB', 'Perubahan Warna': 'Biru menjadi kuning ( dengan warna antara kuning kehijauan)'}
                ]
                st.table(data_table)

                st.markdown('**Pembahasan**')
                st.write('Indikator BTB : berada dibagian yang curam dan mencakup titik ekivalen.') 

  
        else:
            pilihan2 == '4. Titrasi Basa Lemah oleh Asam Kuat'
            def main():

                    st.markdown('**Data Pengamatan Titrasi Basa Lemah oleh Asam Kuat**')
                    data_table = [ 
                    {'Indikator': 'MM', 'Perubahan Warna':'Kuning menjadi Merah (dengan warna antara merah muda'},
                    {'Indikator': 'SM', 'Perubahan Warna':'Jingga menjadi Merah Pekat (dengan warna antara merah jingga)'}
                    ]
                    st.table(data_table)

                    st.markdown('**Pembahasan**')
                    st.write('Indikator MM: berada dibagian yang curam dan mencakup titik ekuivalen')
                    st.write('Indikator SM: masih berada dibagian yang curam dan melewati titik ekivalen.') 

            if __name__ == '__main__':
                main()



    elif pilihan1 == 'Percobaan 2. Standardisasi Asam Basa':
        st.title ('1. Standardisasi NaOH')
        st.header (' a. Tujuan')
        st.write ('Menstandardisasi larutan NaOH 0,1 N dengan baku primer asam oksalat.')
        st.header ('b. Prinsip')
        st.write ( 'Larutan NaOH merupakan larutan standar/baku sekunder yang dibakukan dengan larutan asam oksalat dengan indikator pp (fenoftalein).')
        st.header ('c. Alat dan Bahan')
        st.markdown ('**Alat:** ')
        st.write ('Pada percobaan ini alat yang digunakan adalah Buret makro, statip, Klem buret, Alas titar, Bulb hitam/merah, labu semprot, Erlenmeyer 250 mL, pipet volumetri 25 mL, pipet tetes, corong, piala gelas 250 mL.')
        st.markdown ('**Bahan:**')
        st.write ('Bahan yang digunakan Larutan NaOH 0,1 N, dan kristal asam oksalat.')
        st.header ('d. Prosedur')
        st.write ('Ditimbang teliti ± 630 mg asam oksalat dengan kaca arloji, larutkan ke dalam labu takar 100 mL dan tepatkan sampai tanda garis, lalu homogenkan. Larutan dipipet sebanyak 25 ml ke dalam Erlenmeyer 250 mL, tambahkan 2 tetes indikator PP kemudian dititar dengan larutan NaOH 0,1N sampai larutan berubah warna menjadi merah muda. Percobaan dilakukan 3 kali. Hitung normalitas NaOH.')

        st.title ('2.Standardisasi HCl')
        st.header ('a. Tujuan')
        st.write ('Menstandardisasi larutan HCl 0,1 N dengan baku primer boraks.')
        st.header (' b. Prinsip')
        st.write ( 'Larutan HCI merupakan larutan standar/baku sekunder yang dibakukan dengan larutan boraks dengan indikator SM (Sindur Metil).')
        st.header ('c. Alat dan Bahan')
        st.markdown ('**Alat:** ')
        st.write (' Pada percobaan ini alat yang digunakan adalah Buret makro, statip, Klem buret, Alas titar, Bulb hitam/merah, labu semprot, Erlenmeyer 250 mL, pipet volumetri 25 mL, pipet tetes, corong, piala gelas 250 mL.')
        st.markdown ('**Bahan:**')
        st.write ('Bahan yang digunakan Larutan HCl 0,1 N, dan kristal boraks.')
        st.header (' d. Prosedur')
        st.write ('Ditimbang teliti 1500 mg boraks dengan kaca arloji, larutkan ke dalam labu takar 100 ml. dan tepatkan sampai tanda garis, lalu homogenkan. Larutan dipipet sebanyak 25 mL ke dalamErlenmeyer 250 mL, tambahkan 2 tetes indikator MM kemudian dititar dengan larutan HCI 0.1 N ampai larutan berubah warna menjadi merah jingga (sindur). Dicatat volume serta perubahansaat titik akhir tirasi. Percobaan ini dilakukan 3 kali dan hitung normalitas HCI tiap-tiap ulangan.')
    
    elif pilihan1 == 'Percobaan 3. Standardisasi Larutan KMnO4':
        st.title ('Standardisasi KMnO4')
        st.header (' a. Tujuan')
        st.write ('Menstandardisasi larutan KMnO4 0,1N dengan asam oksalat sebagai bahan baku primer secara permanganometri.')
        st.header ('b. Prinsip')
        st.write ( 'Dalam reaksi KMnO4 dalam suasana asam mengalami reduksi menjadi Mn2+, sedangkan asam oksalat mengalami oksidasi menjadi CO2, dan suhu diatur sampai 70°C. Dalam penitaran ini tidak dipakai indikator, karena kelebihan larutan KMnO4 sedikit saja sudah memberikan warna merah muda pada titik akhir titrasi.')
        st.header ('c. Alat dan Bahan')
        st.markdown ('**Alat:**')
        st.write (' Pada percobaan ini alat yang digunakan adalah Buret makro, statip, Klem buret, Alas titar, Bulb hitam/merah, labu semprot, Erlenmeyer 250 mL, pipet volumetri 25 mL, pipet tetes, corong, piala gelas 50 mL, Labu takar 100 mL.')
        st.markdown ('**Bahan:**')
        st.write ('Bahan yang digunakan Hablur asam oksalat, air suling, Larutan KMnO4 0,1 N dan H2SO4 4N.')
        st.header ('d. Prosedur')
        st.write ('Timbang dengan teliti ± 630 mg hablur asam oksalat, dimasukkan ke labu takar 100 mL dilarutkan dengan air suling lalu ditepatkan sampai tanda tera. Kemudian pipet 25 mL larutan asam oksalat tadi, tambahkan 25 mL H2SO4 4 N panaskan sampai 70°C, lalu titar dengan larutan KMnO4 sampai timbulwarna merah muda. Lakukan duplo. Hitung normalitas KMnO4.')

    else: 
        pilihan1 == 'Percobaan 4. Standardisasi Larutan Tiosulfat'
        st.title ('Standardisasi Larutan Tiosulfat')
        st.header (' a. Tujuan')
        st.write ('Menstandardisasi larutan tio 0,1N dengan potasium dikromat sebagai bahan baku primer secara iodometri.')
        st.header ('b. Prinsip')
        st.write ( 'Natrium tiosulfat distandardasi dengan bahan baku primer K2Cr2O;. Reaksi K2Cr2O7 dengan Kl berlebih dalam suasana asam akan menghasilkan iod. lod yang dibebaskan dititar dengan larutan tio yang normalitasnya telah diketahui, mendekati titik akhir penambahan indikator kanji akan memperjelas warna titik akhir titrasi sampai larutan hijau terang. Jumlah ekivalen K2Cr2O7 setara dengan jumlah ekivalen tio. Kalium dikromat yang digunakan harus murni (baku primer) dan Kl yang dipakai harus bebas iodat.')
        st.header ('c. Alat dan Bahan')
        st.markdown ('**Alat:**')
        st.write (' Buret makro, statip, klem buret, alas titar Bulb hitam/merah, labu semprot, erlenmeyer 250 mL, pipet volumetri 25 mL, pipet tetes, gelas ukur 50 mL, piala gelas 250 mL,labu takar 100 mL, tabung reaksi, rak tabung reaksi.')
        st.markdown ('**Bahan:**')
        st.write ('Hablur K2Cr2O7, air suling, Larutan Tio 0.1 N, HCI 4N, KI 20%, dan Kanji 10%')
        st.header ('d. Prosedur')
        st.write ('Ditimbang dengan teliti 500 mg K2Cr2O7 masukkan ke labu takar 100 mL lalu dilarutkan dan ditepatkan  sampai tanda tera kemudian homogenkan. Dipipet 25 mL larutan K2Cr2O7 tersebut masukkan ke dalam Erlenmeyer ditambahkan 7,5 mL KI 20% dan 25 mL HCI 4 N, kemudian dititrasi dengan larutan tio 0,1 N sampai mendekati titik akhir titrasi (larutan berwarna kuning kehijauan) tambahkan indikator kanji dan titar kembali dengan larutan tio 0,1 N sampai titik akhir titrasi (perubahan warna dari biru tua menjadi hijau muda). Penetapan dilakukan duplo. Hitung normalitas tio.')


#KONTEN UNTUK PERHITUNGAN TITRIMETRI
with Perhitungan_Titrimetri:

    st.header("Perhitungan Titrimetri")
    opsi3 = ('Pilih Opsi','Informasi Umum', 'Perhitungan Normalitas Secara Tidak Langsung', 'Perhitungan Normalitas Secara Langsung', 'Konversi %b/b menjadi %b/v')

    pilihan3 = st.selectbox('Pilih Opsi', opsi3)

    if pilihan3 == 'Pilih Opsi':
         st.write('')

    elif pilihan3 == 'Informasi Umum':
        st.header ('Perbedaan Perhitungan Normalitas Secara Tidak Langsung dan Langsung')
        st.write ('Perhitungan normalitas secara tidak langsung digunakan ketika pada percobaan standardisasi memerlukan pengenceran baku primer secara berulang, sehingga didapatkan nilai pengenceran dari baku primer berupa faktor pengali. Nilai faktor pengali dapat disesuaikan dengan perbandingan volume labu takar dan pipet volumetrik yang digunakan. Sedangkan perhitungan normalitas secara langsung digunakan ketika pada pembuatan larutan baku primer tidak memerlukan pengenceran ke dalam labu takar.')

        st.header ('Nilai Bobot Ekivalen yang Digunakan')
        st.write ('Asam Oksalat : 63 (mg/mgrek)')
        st.write ('Boraks : 191 (mg/mgrek)')
        st.write ('K2Cr2O7 (Kalium Dikromat) : 49 (mg/mgrek)')

    elif pilihan3 == 'Perhitungan Normalitas Secara Tidak Langsung':
        st.header ('Kalkulator Perhitungan Normalitas Secara Tidak Langsung')

        st.image('Rumus Normalitas dengan Fp.jpg')

        Massa_Baku_Primer = st.number_input ('Masukan Nilai Massa (mg)')
        Volume_Titran_mL= st.number_input('Masukan Nilai Volume Titran (mL)')
        Bobot_Ekivalen= st.number_input('Masukan Nilai Bobot Ekivalen (BE)')
        Faktor_Pengali= st.number_input('Masukan Nilai Faktor Pengali (Fp)')

        if Volume_Titran_mL and Bobot_Ekivalen and  Faktor_Pengali !=0:
            Normalitas = (Massa_Baku_Primer) /(Volume_Titran_mL * Bobot_Ekivalen * Faktor_Pengali )

        if st.button('Hitung'):
            st.success(Normalitas)

    elif pilihan3 == 'Perhitungan Normalitas Secara Langsung':
        st.header ('Kalkulator Perhitungan Normalitas Secara Langsung')

        st.image('Rumus Normalitas tanpa Fp.jpg')

        Massa_Baku_Primer = st.number_input ('Masukan Nilai Massa (mg)')
        Volume_Titran_mL= st.number_input('Masukan Nilai Volume Titran (mL)')
        Bobot_Ekivalen= st.number_input('Masukan Nilai Bobot Ekivalen (BE)')
        

        if Volume_Titran_mL and Bobot_Ekivalen !=0:
            Normalitas = (Massa_Baku_Primer) /(Volume_Titran_mL * Bobot_Ekivalen)

        if st.button('Hitung'):
            st.success(Normalitas) 

    else:
        pilihan3 == 'Konversi %b/b menjadi %b/v'
        st.header('Kalkulator Perhitungan Konversi %b/b Menjadi %b/v')

        st.image('Rumus Konversi.jpg')

        Berat_Perberat = st.number_input('Masukan Nilai %b/b')
        Nilai_Berat_Jenis = st.number_input ('Masukan Nilai Berat Jenis (Bj)')

        Berat_Pervolum = (Berat_Perberat) * (Nilai_Berat_Jenis)

        if st.button ('Hitung'):
            st.success(Berat_Pervolum)


#KONTEN UNTUK MATERI PRAKTIK KIMIA ORGANIK
with Materi_Praktik_kimia_Organik:
    
    st.header("Materi Praktik Kimia Organik")
    opsi4 = ('Pilih Materi Praktik Kimia Organik','Percobaan 1. Hidrokarbon', 'Percobaan 2. Alkohol dan Fenol')

    pilihan4 = st.selectbox('Pilih Materi Praktik Kimia Organik:', opsi4)
    if pilihan4 == 'Pilih Materi Praktik Kimia Organik':
         st.write('')

    elif pilihan4 == 'Percobaan 1. Hidrokarbon':

        st.header("Materi Praktik Hidrokarbon")
        opsi5 = ('Pilih Materi Praktik Hidrokarbon','Percobaan 1. Pembuatan dan Uji Kimia Alkana', 'Percobaan 2. Larutan Brom  dalam Karbon Tetraklorida atau Kloroform', 'Percobaan 3. Uji Bayer' , 'Percobaan 4. Pembuatan dan Uji Kimia Alkuna', 'Percobaan 5. Uji Fisika dan Kimia Benzena')

        pilihan5 = st.selectbox('Pilih Percobaan Hidrokarbon:', opsi5) 

        if pilihan5 == 'Pilih Materi Praktik Hidrokarbon':
            st.write('')

        elif pilihan5 == 'Percobaan 1. Pembuatan dan Uji Kimia Alkana':
            st.title ('Pembuatan dan Uji Kimia Alkana')
            st.header (' a. Tujuan')
            st.write ('Dapat membuat dan menguji senyawa kimia alkana dengan reaksi substitusi.')
            st.header ('b. Prinsip')
            st.write ('Suatu senyawa hidrokarbon alifatik yaitu alkana, dihasilkan dari reaksi pencampuran sodalime (CaO+NaOH) dengan natrium asetat, dan dibantu pemanasan api bunsen. Senyawa alkana termasuk hidrokarbon jenuh, tidak reaktif, dan tidak dapat dioksidasi, oleh karena itu reaksi yang digunakan adalah substitusi. Pengujian senyawa alkana ini menggunakan pereaksi I2, KMnO4, dan K2Cr2O7, dimana positifnya uji ini ditandai dengan pemudaran warna dari larutan I2.')
            st.header ('c. Alat dan Bahan')
            st.markdown ('**Alat:**')
            st.write ('Tabung reaksi bertutup selang, tabung reaksi, pipet tetes, dan bunsen.')
            st.markdown ('**Bahan:**')
            st.write ('Campuran sodalime dan natrium asetat, larutan I2, K2Cr2O7, dan KMnO4.')
            st.header ('d. Prosedur')
            st.write ('Tabung reaksi bertutup selang disiapkan, dipastikan dalam keadaan bersih, kering, dan tidak bocor. Campuran sodalime dan natrium asetat dimasukkan ke dalam tabung reaksi bertutup selang.Tabung reaksi sebanyak tiga buah disiapkan dalam keadaan sudah dicuci bersih. Sebanyak 2 mL larutan I2, KMnO4, dan K2Cr2O7 dimasukkan ke dalam masing-masing tabung reaksi.Campuran sodalime dan natrium asetat dipanaskan diatas nyala api bunsen, kemudian ujung selang dicelupkan ke dalam masing-masing larutan uji (I2, KMnO4, dan K2Cr2O7).')


        elif pilihan5 == 'Percobaan 2. Larutan Brom  dalam Karbon Tetraklorida atau Kloroform':
                st.title ('Larutan Brom  dalam Karbon Tetraklorida atau Kloroform')
                st.header ('a. Tujuan')
                st.write ('Dapat mengidentifikasi dan membedakan senyawa hidrokarbon jenuh (ikatan tunggal) dengan senyawa hidrokarbon tidak jenuh (ikatan rangkap).')
                st.header ('b. Prinsip')
                st.write ('Suatu senyawa hidrokarbon  tidak jenuh (ikatan rangkap) direaksikan dengan larutan brom 5% dalam CCl4 atau kloroform, dimana reaksi yang terjadi pada proses ini adalah reaksi adisi, yaitu reaksi pemutusan ikatan rangkap. Pengujian ini dinyatakan positif ditandai dengan memudarnya warna brom.')
                st.header ('c. Alat dan Bahan')
                st.markdown ('**Alat:**')
                st.write ('Tabung reaksi, dan pipet tetes.')
                st.markdown ('**Bahan:**')
                st.write ('Heksana, minyak tanah, dan larutan brom 5% dalam CCl4 atau kloroform.')
                st.header ('d. Prosedur')
                st.write ('Sampel uji dimasukkan ke dalam tabung reaksi sebanyak 1 drop. Larutan brom 5% dalam CCl4 atau kloroform ditambahkan tetes per tetes sampai warna brom tidak berubah. Perubahan yang terjadi diamati dan dicatat.')

        elif pilihan5 == 'Percobaan 3. Uji Bayer':
                st.title ('Uji Bayer')
                st.header (' a. Tujuan')
                st.write ('Dapat mengidentifikasi adanya senyawa hidrokarbon tidak jenuh dalam suatu sampel uji.')
                st.header ('b. Prinsip')
                st.write ('Suatu senyawa hidrokarbon yang mengandung ketidakjenuhan direaksikan dengan KMnO4 maka akan terjadi reaksi oksidasi.  Positifnya pengujian ini ditandai dengan memudarnya warna larutan KMnO4. Dari reaksi ini juga akan menghasilkan glikol dan endapan MnO4 (coklat).')
                st.header ('c. Alat dan Bahan')
                st.markdown ('**Alat:**')
                st.write ('Tabung reaksi, dan pipet tetes.')
                st.markdown ('**Bahan:**')
                st.write ('Heksana, minyak tanah, dan larutan KMnO4.')
                st.header ('d. Prosedur')
                st.write ('Sampel uji sebanyak 1 drop dimasukkan ke dalam tabung reaksi. Larutan KMnO4 ditambahkan tetes per tetes ke dalam tabung reaksi berisi sampel uji, dan dihomogenkan.Perubahan yang terjadi diamati.')

        elif pilihan5 == 'Percobaan 4. Pembuatan dan Uji Kimia Alkuna':
                st.title ('Pembuatan dan Uji Kimia Alkuna')
                st.header (' a. Tujuan')
                st.write ('Dapat membuat dan menguji senyawa kimia alkuna.')
                st.header ('b. Prinsip')
                st.write ('Suatu senyawa alkuna diperoleh dari reaksi kalsium karbida dengan aquades, dimana dari reaksi ini akan menghasilkan gas etuna. Etuna yang dihasilkan dapat diuji menggunakan larutan brom, dimana pada pengujian ini terjadi reaksi adisi. Dari reaksi tersebut dihasilkan haloalkana yang ditandai dengan pemudaran warna brom sebagai uji positifnya. Selain itu, alkuna juga bisa diuji menggunakan KMnO4, dimana akan menghasilkan glikol etana, MnO2, dan KOH, ditandai dengan berubahnya warna KMnO4 dan terbentuk endapan berwarna hitam.')
                st.header ('c. Alat dan Bahan')
                st.markdown ('**Alat:**')
                st.write ('Tabung reaksi bertutup selang, tabung reaksi, dan pipet tetes.')
                st.markdown ('**Bahan:**')
                st.write ('Karbit, larutan brom, KMnO4, dan K2Cr2O7.')
                st.header ('d. Prosedur')
                st.write ('Sebanyak 2 gram karbit dimasukkan ke dalam tabung reaksi bertutup selang. Air suling dimasukkan ke dalam tabung reaksi bertutup selang secukupnya sampai terbentuk gas.Larutan brom, KMnO4, dan K2Cr2O7 dimasukkan ke dalam masing-masing tabung reaksi. Ujung selang pada tabung reaksi dicelupkan ke dalam masing-masing tabung reaksi berisi larutan uji secara bergilir. Perubahan yang terjadi diamati.')

        else:
            pilihan5 == 'Percobaan 5. Uji Fisika dan Kimia Benzena'
            st.title ('Uji Fisika dan Kimia Benzena')
            st.header (' a. Tujuan')
            st.write ('Dapat mengetahui dan melakukan uji fisika dan kimia benzena.')
            st.header ('b. Prinsip')
            st.markdown ('**Uji Fisika**')
            st.write('Suatu anggota dari kelompok senyawa aromatik yaitu benzena dapat diuji dengan pengujian fisika. Uji fisika dilakukan dengan cara pembakaran benzena, dimana proses pengujian ini melibatkan pembakaran secara langsung. Proses pembakaran ini dikatakan sempurna jika produk yang dihasilkan CO2 dan H2O. Sedangkan suatu proses pembakaran ini dikatakan tidak sempurna jika menghasilkan jelaga.')
            st.markdown('**Uji Kimia**')
            st.write(' Sutu pengujian kimia benzena dilakukan dengan cara mereaksikan benzena dengan air brom. Pengujian ini dilakukan dengan membandingkan reaksi yang disertai katalis dan tanpa katalis, dimana katalis yang digunakan adalah Fe. Penggunaan katalis ini akan mempercepat reaksi. Positifnya penguian ini ditandai dengan pemudaran warna brom.')
            st.header ('c. Alat dan Bahan')
            st.markdown ('**Alat:**')
            st.write ('Tutup cawan porselen, tabung reaksi, penjepit kayu, pipet tetes, bunsen, dan piala gelas.')
            st.markdown ('**Bahan:**')
            st.write ('Benzena, air brom, katalis besi, dan air suling.')
            st.header ('d. Prosedur')
            st.markdown ('**Uji Fisika**')
            st.write('Sampel uji diteteskan secukupnya diatas tutup cawan porselen. Sampel uji dibakar dengan nyala api langsung. Nyala api yang terbentuk diamati.')
            st.markdown('**Uji Kimia**')
            st.write('Sampel uji sebnayak 4 mL dimasukkan ke dalam tabung reaksi. Air brom sebanyak 2 mL ditambahkan ke dalam tabung reaksi  isi sampel uji, dan dihomogenkan. Logam Fe ditambahkan seujung spatula ke dalam tabung reaksi isi sampel uji, dan dikocok. Perubahan yang terjadi diamati.')

    else:
        pilihan4 == 'Percobaan 2. Alkohol dan Fenol'

        st.header("Materi Praktik Alkohol dan Fenol")

        opsi6 = ('Pilih Materi Praktik Alkohol dan Fenol','Percobaan 1. Uji Kelarutan Alkohol', 'Percobaan 2. Pembentukan Senyawa Beraroma', 'Percobaan 3. Uji Ceric Nitrat' , 'Percobaan 4. Uji Lucas', 'Percobaan 5. Uji Jones', 'Percobaan 6. Uji Iodoform', 'Percobaan 7. Uji kelarutan dan Keasaman Fenol')

        pilihan6 = st.selectbox('Pilih Percobaan Alkohon dan Fenol:', opsi6) 

        if pilihan6 == 'Pilih Materi Praktik Alkohol dan Fenol':
            st.write('')

        elif pilihan6 == 'Percobaan 1. Uji Kelarutan Alkohol' :
            st.title ('Uji Kelarutan Alkohol')
            st.header (' a. Tujuan')
            st.write ('Dapat mengetahui tingkat kelarutan macam-macam alkohol di dalam pelarut polar (air suling).')
            st.header ('b. Prinsip')
            st.write ('Suatu senyawa polar yaitu alkohol dilarutkan ke dalam pelarut polar (air suling) untuk mengetahui tingkat kelarutannya. Setiap alkohol memilki tingkat kepolaran yang berbeda, tergantung pada jenisnya, gugus –OH, dan panjang rantai karbonnya. Semakin panjang rantai karbon yang dimiliki, maka alkohol akan bersifat non-polar. Hal ini dikarenakan sifat hidrofobik yang dimiliki oleh alkohol akan mengalahkan sifat hidrofil gugus hidroksil (-OH).')
            st.header ('c. Alat dan Bahan')
            st.markdown ('**Alat:**')
            st.write ('Tabung reaksi, dan pipet tetes.')
            st.markdown ('**Bahan:**')
            st.write ('Etanol, 1-butanol, 2-butanol, t-butil alkohol, amil alkohol, gliserol, dan air suling.')
            st.header ('d. Prosedur')
            st.write ('Air suling sebanyak 1 drop dimasukkan ke dalam tabung reaksi Sampel uji dimasukkan ke dalam tabung reaksi berisi air suling tetes per tetes, sambil dihomogenkan. Kelarutan sampel uji diamati.') 
            st.markdown ('**Keterangan:**')
            st.write ('1-5: 2 fasa (tidak larut)')
            st.write ('<20: 2 fasa (sukar larut)')
            st.write ('20 : 1 fasa (mudah larut)')

        elif pilihan6 == 'Percobaan 2. Pembentukan Senyawa Beraroma' :
            st.title ('Pembentukan Senyawa Beraroma')
            st.header (' a. Tujuan')
            st.write ('Dapat mengetahui proses pembentukkan dan pembuatan senyawa beraroma dengan bahan dasar alkohol.')
            st.header ('b. Prinsip')
            st.write ('Suatu senyawa beraroma dapat dibentuk dengan cara mereaksikan alkohol dengan asam asetat, dimana pada reaksi ini akan terbentuk senyawa ester. Proses pembentukkan alkohol menjadi senyawa beraroma (ester) ini disebut dengan proses esterifikasi, dimana pada prosesnya dibantu oleh katalis H2SO4. Terbentuknya senyawa beraroma ini ditandai dengan keluarnya aroma khas.')
            st.header ('c. Alat dan Bahan')
            st.markdown ('**Alat:**')
            st.write ('Tabung reaksi, pipet tetes, piala gelas, kaki tiga, kawat kasa, dan bunsen.')
            st.markdown ('**Bahan:**')
            st.write ('Etanol, amil alkohol, asam asetat, asam sulfat, asam sulfat (H2SO4) pekat, dan air suling.')
            st.header ('d. Prosedur')
            st.write ('Piala gelas diisikan air kran kemudian dipanaskan. Sampel uji sebanyak 1 drop dimasukkan ke dalam tabung reaksi. Sebanyak 1 drop asam asetat ditambahkan ke dalam tabung reaksi berisi sampel uji. Sebanyak 1 drop asam sulfat (H2SO4) pekat ditambahkan ke dalam tabung reaksi, kemudian dihomogenkan. Tabung reaksi berisi sampel uji dipanaskan di dalam penangas selama 1-2 menit. Sampel uji yang telah dipanaskan dituangkan ke dalam piala glass berisi air kran, kemudian amati aroma khas yang keluar.')

        elif pilihan6 == 'Percobaan 3. Uji Ceric Nitrat' :
            st.title ('Uji Ceric Nitrat')
            st.header ('a. Tujuan')
            st.write ('Dapat mengetahui dan melakukan uji ceric nitrat terhadap senyawa yang memiliki gugus (-OH) hidroksil yang dimiliki oleh senyawa alkohol dan fenol.')
            st.header ('b. Prinsip')
            st.write ('Suatu sampel yang memiliki gugus (-OH) hidroksil seperti pada senyawa alkohol dan fenol direaksikan dengan pereaksi ceric nitrat, dimana pada reaksi ini akan membentuk senyawa kompleks. Alkohol yang memiliki 1 sampai 10 atom karbon, baik itu primer, sekunder, maupun tersier, akan bereaksi dengan ceric nitart. Reaksi yang terjadi merupakan reaksi substitusi. Percobaan ini dikatakan positif jika dari reaksi tersebut terjadi perubahan warna dari kuning menjadi merah ceri, dimana perbandingan hasil uji posistif ini dilihat dari warna awal pereaksi dengan warna akhir pereaksi setelah direaksikan dengan sampel.')
            st.header ('c. Alat dan Bahan')
            st.markdown ('**Alat:**')
            st.write ('Tabung reaksi dan pipet tetes.')
            st.markdown ('**Bahan:**')
            st.write ('1-butanol, 2-butanol, t-butil alkohol, fenol, dan pereaksi ceric nitrat.')
            st.header ('d. Prosedur')
            st.write ('Masing-masing sampel uji dimasukkan ke dalam tabung reaksi sebanyak 1 drop. Sebanyak 5 tetes pereaksi ceric nitrat ditambahkan ke dalam tabung reaksi, keudian dihomogenkan. Perubahan pada sampel uji diamati, dan dicatat.')

        elif pilihan6 == 'Percobaan 4. Uji Lucas':
            st.title ('Uji Lucas')
            st.header (' a. Tujuan')
            st.write ('Dapat melakukan uji lanjutan untuk membedakan antara alkohol primer, sekunder, dan tersier menggunakan pereaksi lucas yang dilihat berdasarkan kecepatan reaksi untuk membentuk emulsi putih.')
            st.header ('b. Prinsip')
            st.write ('Suatu senyawa alkohol primer, sekunder, dan tersier direaksikan dengan peeaksi lucas (HCl-ZnCl2), dimana pada pengujian ini akan terjadi reaksi oksidasi. Hasil uji positif pada percobaan ini ditandai dengan terbentuknya emulsi putih, dimana emulsi putih ini akan terbentuk pad alkohol sekunder dan tersier.')
            st.header ('c. Alat dan Bahan')
            st.markdown ('**Alat:**')
            st.write ('Tabung reaksi, pipet tetes, kaki tiga, bunsen dan piala gelas.')
            st.markdown ('**Bahan:**')
            st.write ('1-butanol, 2-butanol, dan t-butil alkohol, dan pereaksi lucas.')
            st.header ('d. Prosedur')
            st.write ('Piala gelas diisi air secukupnya, kemudian dipanaskan diatas bunsen. Sampel uji dimasukkan ke dalam tabung reaksi sebnayak 1 drop. Sebanyak 1 drop pereaksi lucas ditambahkan ke dalam tabung reaksi berisi sampel uji, kemudian dihomogenkan. Sampel uji dipanaskan selama 1-2 menit, kemudian perubahan yang terjadi diamati.')

        elif pilihan6 == 'Percobaan 5. Uji Jones' :
            st.title ('Uji Jones')
            st.header ('a. Tujuan')
            st.write ('Dapat melakukan uji lanjutan untuk membedakan antara alkohol primer, sekunder, dan tersier menggunakan pereaksi jones.')
            st.header ('b. Prinsip')
            st.write ('Suatu senyawa alkohol primer, sekunder, dan tersier direaksikan dengan peeaksi jones (CrO3-H2SO4), dimana pada pengujian ini akan terjadi reaksi oksidasi. Hasil uji positif pada percobaan ini ditandai dengan terbentuknya suspensi hijau kebiruan, dimana emulsi putih ini akan terbentuk pada alkohol primer dan sekunder.')
            st.header ('c. Alat dan Bahan')
            st.markdown ('**Alat:**')
            st.write ('Tabung reaksi, pipet tetes, kaki tiga, bunsen dan piala gelas.')
            st.markdown ('**Bahan:**')
            st.write ('1-butanol, 2-butanol, t-butil alkohol, dan pereaksi jones.')
            st.header ('d. Prosedur')
            st.write ('Sampel uji dimasukkan ke dalam tabung reaksi sebnayak 1 drop. Sebanyak 1 drop pereaksi lucas ditambahkan ke dalam tabung reaksi berisi sampel uji, kemudian dihomogenkan. Perubahan yang terjadi saat reaksi berlangsung diamati dan dicatat.')

        elif pilihan6 == 'Percobaan 6. Uji Iodoform' :
            st.title ('Uji Iodoform')
            st.header (' a. Tujuan')
            st.write ('Dapat melakukan uji lanjutan untuk membedakan antara alkohol primer, sekunder, dan tersier menggunakan pereaksi iodoform.')
            st.header ('b. Prinsip')
            st.write ('Suatu senyawa alkohol direaksikan dengan larutan I2 dalam KI dalam suasana basa (penambahan NaOH) dan melalui proses pemanasan. Positifnya hasil pengujian dari larutan ini ditandai dengan terbentuknya endapan kuning.')
            st.header ('c. Alat dan Bahan')
            st.markdown ('**Alat:**')
            st.write ('Tabung reaksi, pipet tetes, kaki tiga, bunsen dan piala gelas.')
            st.markdown ('**Bahan:**')
            st.write ('Etanol, 2-butanol, amil alkohol, NaOH 10%, dan larutan I2 (dalam KI).')
            st.header ('d. Prosedur')
            st.write ('Piala gelas diisi air kran kmeudian dipanaskan diatas bunsen. Sampel uji dimasukkan ke dalam tabung reaksi sebnayak 1 drop. Sebanyak 10 tetes NaOH 10% ditambahkan ke dalam tabung reaksi berisi sampel uji, kemudian dihomogenkan. Larutan I2 (dalam KI) ditambahkan sebnayak 2x sampel ke dalam tabung reaksi, kemudian dihomogenkan. Sampel uji dipanasakan dalam penangas selama 10-15 menit Perubahan yang terjadi saat reaksi berlangsung diamati dan dicatat.')

        else:
            pilihan6 == 'Percobaan 7. Uji kelarutan dan Keasaman Fenol'
            st.title ('Uji kelarutan dan Keasaman Fenol')
            st.header (' a. Tujuan')
            st.write ('Dapat melakukan uji kelarutan dan keasaman fenol.')
            st.header ('b. Prinsip')
            st.write ('Fenol merupakan suatu senyawa yang sedikit larut dalam air (kondisi ruang). Kelarutan fenol dalam air akan bertambah jika temperaturnya dinaikkan. Fenol bersifat asam dibandingkan alkohol. Positifnya hasil uji ini ditandai dengan perubahan larutan menjadi keruh ketika dilarutkan dalam air dan akan memerahkan kertas lakmus biru, dan fenol akan larut ketika dipanaskan.')
            st.header ('c. Alat dan Bahan')
            st.markdown ('**Alat:**')
            st.write ('Tabung reaksi, kertas lakmus, piala gelas, dan pipet tetes.')
            st.markdown ('**Bahan:**')
            st.write ('Air suling dan fenol.')
            st.header ('d. Prosedur')
            st.write ('Piala gelas diisi air kran dan dipanaskan diatas bunsen. Sampel uji sebanyak 1 drop dimasukkan ke dalam tabung reaksi. Air suling sebanyak 1 drop dimasukkan ke dalam tabung reaksi berisi sampel uji, kemudian dihomogenkan. Kelarutan pada fenol diamati dan dicatat. Sampel uji dipanaskan dan diamati kelarutannya. Keasamaan sampel diuji menggunakan kertas lakmus dengan meneteskan sampel uji diatas lakmus.')
