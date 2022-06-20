import math
import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np #berfungsi untuk memproses komputasi numerik


#ENKRIPSI Hill cipher
def ENKRIPSI_HillC(msg,key):
    msg = msg.replace(" ", "")

    # jika msg tersebut merupakan angka ganjil, maka menambahkan 0 di akhir
    len_chk = 0
    if len(msg) % 2 != 0:
        msg += "0"
        len_chk = 1

    # msg ke matriks
    row = 2
    col = int(len(msg)/2)
    msg2d = np.zeros((row, col), dtype=int)

    itr1 = 0
    itr2 = 0
    for i in range(len(msg)):
        if i % 2 == 0:
            msg2d[0][itr1] = int(ord(msg[i])-65)
            itr1 += 1
        else:
            msg2d[1][itr2] = int(ord(msg[i])-65)
            itr2 += 1
    # for

    
    key = key.replace(" ", "")

    # key ke matriks 2x2
    key2d = np.zeros((2, 2), dtype=int)
    itr3 = 0
    for i in range(2):
        for j in range(2):
            key2d[i][j] = ord(key[itr3])-65
            itr3 += 1

    # melakukan pengecekan validitas terhadap key
    # kemudian mencari determinan
    deter = key2d[0][0] * key2d[1][1] - key2d[0][1] * key2d[1][0]
    deter = deter % 26

    # cara mencari invers perkalian
    mul_inv = -1
    for i in range(26):
        temp_inv = deter * i
        if temp_inv % 26 == 1:
            mul_inv = i
            break
        else:
            continue
    # for

    if mul_inv == -1:
        # print("Invalid key")
        st.write(" ")
        
    # if
        
    # if
    encryp_text = ""
    itr_count = int(len(msg)/2)
    if len_chk == 0:
        for i in range(itr_count):
            temp1 = msg2d[0][i] * key2d[0][0] + msg2d[1][i] * key2d[0][1]
            encryp_text += chr((temp1 % 26) + 65)
            temp2 = msg2d[0][i] * key2d[1][0] + msg2d[1][i] * key2d[1][1]
            encryp_text += chr((temp2 % 26) + 65)
        # for
    else:
        for i in range(itr_count-1):
            temp1 = msg2d[0][i] * key2d[0][0] + msg2d[1][i] * key2d[0][1]
            encryp_text += chr((temp1 % 26) + 65)
            temp2 = msg2d[0][i] * key2d[1][0] + msg2d[1][i] * key2d[1][1]
            encryp_text += chr((temp2 % 26) + 65)
        # for
    # if else
    
    st.subheader('Ciphertext :')
    st.header(encryp_text)
    expander = st.expander("Detail Hasil Enkripsi")
    expander.write('Plaintext :')
    expander.subheader(msg)
    expander.write('Key :')
    expander.subheader(key)




#DEKRIPSI Hill cipher
def DEKRIPSI_HillC(msg,key):
    msg = msg.replace(" ", "")

    # jika msg tersebut merupakan angka ganjil, maka menambahkan 0 di akhir
    len_chk = 0
    if len(msg) % 2 != 0:
        msg += "0"
        len_chk = 1

    # msg ke matriks
    row = 2
    col = int(len(msg) / 2)
    msg2d = np.zeros((row, col), dtype=int)

    itr1 = 0
    itr2 = 0
    for i in range(len(msg)):
        if i % 2 == 0:
            msg2d[0][itr1] = int(ord(msg[i]) - 65)
            itr1 += 1
        else:
            msg2d[1][itr2] = int(ord(msg[i]) - 65)
            itr2 += 1
    # for

    key = key.replace(" ", "")

    # key  ke matriks 2x2
    key2d = np.zeros((2, 2), dtype=int)
    itr3 = 0
    for i in range(2):
        for j in range(2):
            key2d[i][j] = ord(key[itr3]) - 65
            itr3 += 1
    # for

    # mencari determinan
    deter = key2d[0][0] * key2d[1][1] - key2d[0][1] * key2d[1][0]
    deter = deter % 26

    # mencari invers perkalian
    mul_inv = -1
    for i in range(26):
        temp_inv = deter * i
        if temp_inv % 26 == 1:
            mul_inv = i
            break
        else:
            continue
    # for

    # adjugate matrix
    # swapping
    key2d[0][0], key2d[1][1] = key2d[1][1], key2d[0][0]

    # changing signs pada matriks
    key2d[0][1] *= -1
    key2d[1][0] *= -1

    key2d[0][1] = key2d[0][1] % 26
    key2d[1][0] = key2d[1][0] % 26

    # mengkalikan invers perkalian matriks dengan adjugate matriks
    for i in range(2):
        for j in range(2):
            key2d[i][j] *= mul_inv

    # modulo
    for i in range(2):
        for j in range(2):
            key2d[i][j] = key2d[i][j] % 26

    # cipher to plaintext
    decryp_text = ""
    itr_count = int(len(msg) / 2)
    if len_chk == 0:
        for i in range(itr_count):
            temp1 = msg2d[0][i] * key2d[0][0] + msg2d[1][i] * key2d[0][1]
            decryp_text += chr((temp1 % 26) + 65)
            temp2 = msg2d[0][i] * key2d[1][0] + msg2d[1][i] * key2d[1][1]
            decryp_text += chr((temp2 % 26) + 65)
            # for
    else:
        for i in range(itr_count - 1):
            temp1 = msg2d[0][i] * key2d[0][0] + msg2d[1][i] * key2d[0][1]
            decryp_text += chr((temp1 % 26) + 65)
            temp2 = msg2d[0][i] * key2d[1][0] + msg2d[1][i] * key2d[1][1]
            decryp_text += chr((temp2 % 26) + 65)
            # for
    # if else
    #mencetak decrypt pada hill cipher
    #mencetak hasil akhir Dekripsi
    st.subheader('Plaintext :')
    st.header(decryp_text)
    expander = st.expander("Detail Hasil Dekripsi")
    expander.write('Ciphertext :')
    expander.subheader(msg)
    expander.write('Key :')
    expander.subheader(key)
    



#Super Enkripsi
def superEnkripsi(msg,key):

    #enkripsi hill cipher
    msg = msg.replace(" ", "")
    pl = msg

    # jika msg tersebut merupakan angka ganjil, maka menambahkan 0 di akhir
    len_chk = 0
    if len(msg) % 2 != 0:
        msg += "0"
        len_chk = 1

    # msg ke matriks
    row = 2
    col = int(len(msg)/2)
    msg2d = np.zeros((row, col), dtype=int)

    itr1 = 0
    itr2 = 0
    for i in range(len(msg)):
        if i % 2 == 0:
            msg2d[0][itr1] = int(ord(msg[i])-65)
            itr1 += 1
        else:
            msg2d[1][itr2] = int(ord(msg[i])-65)
            itr2 += 1
    # for

    
    key = key.replace(" ", "")

    # key ke matriks 2x2
    key2d = np.zeros((2, 2), dtype=int)
    itr3 = 0
    for i in range(2):
        for j in range(2):
            key2d[i][j] = ord(key[itr3])-65
            itr3 += 1

    # melakukan pengecekan validitas terhadap key
    # kemudian mencari determinan
    deter = key2d[0][0] * key2d[1][1] - key2d[0][1] * key2d[1][0]
    deter = deter % 26

    # cara mencari invers perkalian
    mul_inv = -1
    for i in range(26):
        temp_inv = deter * i
        if temp_inv % 26 == 1:
            mul_inv = i
            break
        else:
            continue
    # for

    if mul_inv == -1:
        # print("Invalid key")
        st.write(" ")
        
    # if
        
    # if

    encryp_text = ""
    itr_count = int(len(msg)/2)
    if len_chk == 0:
        for i in range(itr_count):
            temp1 = msg2d[0][i] * key2d[0][0] + msg2d[1][i] * key2d[0][1]
            encryp_text += chr((temp1 % 26) + 65)
            temp2 = msg2d[0][i] * key2d[1][0] + msg2d[1][i] * key2d[1][1]
            encryp_text += chr((temp2 % 26) + 65)
        # for
    else:
        for i in range(itr_count-1):
            temp1 = msg2d[0][i] * key2d[0][0] + msg2d[1][i] * key2d[0][1]
            encryp_text += chr((temp1 % 26) + 65)
            temp2 = msg2d[0][i] * key2d[1][0] + msg2d[1][i] * key2d[1][1]
            encryp_text += chr((temp2 % 26) + 65)
        # for
    # if else
   
   #encrypt pada Transpossion cipher
    def trans_encrypt(msg):
        hasil = ""


        # track key indices
        k_indx = 0

        msg_len = float(len(msg))
        msg_lst = list(msg)
        key_lst = sorted(list(key))

        # calculate column of the matrix
        col = len(key)
        
        # calculate maximum row of the matrix
        row = int(math.ceil(msg_len / col))

        # add the padding character '_' in empty
        # the empty cell of the matix
        fill_null = int((row * col) - msg_len)
        msg_lst.extend('_' * fill_null)

        # create Matrix and insert message and
        # padding characters row-wise
        matrix = [msg_lst[i: i + col]
                for i in range(0, len(msg_lst), col)]

        # read matrix column-wise using key
        for _ in range(col):
            curr_idx = key.index(key_lst[k_indx])
            hasil += ''.join([row[curr_idx]
                            for row in matrix])
            k_indx += 1

        return hasil

    #dekrip pada transpossion cipher
    def trans_decrypt(hasil):
        msg = ""
        
        # track key indices
        k_indx = 0

        # track msg indices
        msg_indx = 0
        msg_len = float(len(hasil))
        msg_lst = list(hasil)

        # calculate column of the matrix
        col = len(key)
        
        # calculate maximum row of the matrix
        row = int(math.ceil(msg_len / col))

        # convert key into list and sort
        # alphabetically so we can access
        # each character by its alphabetical position.
        key_lst = sorted(list(key))

        # create an empty matrix to
        # store deciphered message
        dec_cipher = []
        for _ in range(row):
            dec_cipher += [[None] * col]

        # Arrange the matrix column wise according
        # to permutation order by adding into new matrix
        for _ in range(col):
            curr_idx = key.index(key_lst[k_indx])

            for j in range(row):
                dec_cipher[j][curr_idx] = msg_lst[msg_indx]
                msg_indx += 1
            k_indx += 1

        # convert decrypted msg matrix into a string
        try:
            msg = ''.join(sum(dec_cipher, []))
        except TypeError:
            raise TypeError("This program cannot",
                            "handle repeating words.")

        null_count = msg.count('_')

        if null_count > 0:
            return msg[: -null_count]

        return msg
    
    #dekripsi hill cipher
    msg = encryp_text .replace(" ", "")

    # jika msg tersebut merupakan angka ganjil, maka menambahkan 0 di akhir
    len_chk = 0
    if len(msg) % 2 != 0:
        msg += "0"
        len_chk = 1

    # msg ke matriks
    row = 2
    col = int(len(msg) / 2)
    msg2d = np.zeros((row, col), dtype=int)

    itr1 = 0
    itr2 = 0
    for i in range(len(msg)):
        if i % 2 == 0:
            msg2d[0][itr1] = int(ord(msg[i]) - 65)
            itr1 += 1
        else:
            msg2d[1][itr2] = int(ord(msg[i]) - 65)
            itr2 += 1
    # for

    key = key.replace(" ", "")

    # key  ke matriks 2x2
    key2d = np.zeros((2, 2), dtype=int)
    itr3 = 0
    for i in range(2):
        for j in range(2):
            key2d[i][j] = ord(key[itr3]) - 65
            itr3 += 1
    # for

    # mencari determinan
    deter = key2d[0][0] * key2d[1][1] - key2d[0][1] * key2d[1][0]
    deter = deter % 26

    # mencari invers perkalian
    mul_inv = -1
    for i in range(26):
        temp_inv = deter * i
        if temp_inv % 26 == 1:
            mul_inv = i
            break
        else:
            continue
    # for

    # adjugate matrix
    # swapping
    key2d[0][0], key2d[1][1] = key2d[1][1], key2d[0][0]

    # changing signs pada matriks
    key2d[0][1] *= -1
    key2d[1][0] *= -1

    key2d[0][1] = key2d[0][1] % 26
    key2d[1][0] = key2d[1][0] % 26

    # mengkalikan invers perkalian matriks dengan adjugate matriks
    for i in range(2):
        for j in range(2):
            key2d[i][j] *= mul_inv

    # modulo
    for i in range(2):
        for j in range(2):
            key2d[i][j] = key2d[i][j] % 26

    # cipher to plaintext
    decryp_text = ""
    itr_count = int(len(msg) / 2)
    if len_chk == 0:
        for i in range(itr_count):
            temp1 = msg2d[0][i] * key2d[0][0] + msg2d[1][i] * key2d[0][1]
            decryp_text += chr((temp1 % 26) + 65)
            temp2 = msg2d[0][i] * key2d[1][0] + msg2d[1][i] * key2d[1][1]
            decryp_text += chr((temp2 % 26) + 65)
            # for
    else:
        for i in range(itr_count - 1):
            temp1 = msg2d[0][i] * key2d[0][0] + msg2d[1][i] * key2d[0][1]
            decryp_text += chr((temp1 % 26) + 65)
            temp2 = msg2d[0][i] * key2d[1][0] + msg2d[1][i] * key2d[1][1]
            decryp_text += chr((temp2 % 26) + 65)
            # for
        
    z = trans_encrypt(encryp_text)

    #mencetak enkripsi text
    #mencetak hasil akhir Enkripsi
    
    
    
    col1, col2 = st.columns(2)
    with col1:
        expander = st.expander("Detail Hasil Enkripsi")
        expander.write('Plaintext :')
        expander.subheader(pl)
        expander.write('Key :')
        expander.subheader(key)
        expander.subheader('Proses Enkripsi `Super Enkripsi`')
        expander.markdown('##### Enkripsi `Hill Cipher` + `Transposisi Kolom` :')
        expander.write('`Ciphertext Hill Cipher :`')
        expander.subheader(encryp_text)
        expander.write('`Ciphertext Transposisi :`')
        expander.subheader(trans_encrypt(encryp_text))
        expander.markdown('##### `Hasil Enkripsi Hill Cipher + Transposisi Kolom :`')
        expander.subheader(trans_encrypt(encryp_text))

    with col2:
        expander = st.expander("Detail Hasil Dekripsi ")
        expander.subheader('Proses Dekripsi `Super Enkripsi`')
        expander.markdown('##### Dekripsi `Hill Cipher` + `Transposisi Kolom` :')
        expander.write('`Ciphertext Transposisi :`')
        expander.subheader(trans_encrypt(encryp_text))
        expander.write('`Plaintext Transposisi :`')
        expander.subheader(trans_decrypt(z))
        expander.write('`Plaintext Hill Cipher :`')
        expander.subheader(decryp_text)
        expander.markdown('##### `Hasil Dekripsi Hill Cipher + Transposisi Kolom :`')
        expander.subheader(decryp_text)




def app():
    st.write('Ini adalah `Halaman Kriptografi`.')
    st.write('Aplikasi ini dibuat untuk memenuhi tugas `Kriptografi`, algoritma yang digunakan adalah `Hill Cipher` dan `Super Enkripsi`.')
    st.subheader('Nama Kelompok :')
    st.markdown("* **FATHAN CAHYA PURMIANDARU        A11.2019.11792**")
    st.markdown("* **RIZKY HELMI PUTRA GARDRIANA     A11.2019.11811**")
    st.markdown("* **ANUGRAH WIDIANTO                A11.2019.11777**")
    st.markdown("* **ANA LAZULVA INDAH               A11.2019.11810**")
    st.markdown("* **TEKAD AGUNG NUGROHO             A11.2019.11787**")
   
    algo = st.selectbox( 'Pilih Algoritma',
    ('Hill Chiper', 'Super Enkripsi'))

#Hill
    if algo == 'Hill Chiper':
        selected = st.selectbox( 'Pilih Proses',
        ('Enkripsi', 'Dekripsi'))
        if selected == 'Enkripsi':
            st.write('# Enkripsi')
            col1, col2 = st.columns(2)
            with col1:
                msg = st.text_area('', placeholder='Masukkan Text').upper()
            with col2:
                key = st.text_input('', placeholder='Enter 4 letter Key String ',max_chars=4).upper()
            if st.button('Enkripsi'):
                if len(key) % 4 == 0:
                    ENKRIPSI_HillC(msg,key)
                elif len(key) % 4 != 0:
                    st.error('key harus 4 karakter')

            else:
                st.warning('Silahkan input Text dan Key')

        if selected == 'Dekripsi':
            st.write('# Dekripsi')
            col1, col2 = st.columns(2)
            with col1:
                msg = st.text_area('', placeholder='Masukkan Text').upper()
            with col2:
                key = st.text_input('', placeholder='Enter 4 letter Key String ',max_chars=4).upper()
            if st.button('Dekripsi'):
                if len(key) % 4 == 0:
                    DEKRIPSI_HillC(msg,key)
                elif len(key) % 4 != 0:
                    st.error('key harus 4 karakter')
                

            else:
                st.warning('Silahkan inputText dan Key')

#Super Enkripsi                
    if algo == 'Super Enkripsi':
        selected = st.selectbox( 'Pilih Proses',
        ('Enkripsi & Dekripsi', 'Dekripsi'), disabled = True)
        if selected == 'Enkripsi & Dekripsi':
            st.write('# Enkripsi & Dekripsi')
            col1, col2 = st.columns(2)
            with col1:
                msg = st.text_area('', placeholder='Masukkan Text').upper()
            with col2:
                key = st.text_input('', placeholder='Enter 4 letter Key String ',max_chars=4).upper()
            if st.button('Proses'):
                if len(key) % 4 == 0:
                    superEnkripsi(msg,key)
                elif len(key) % 4 != 0:
                    st.error('key harus 4 karakter')
                
            else:
                st.warning('Silahkan input Text dan Key')