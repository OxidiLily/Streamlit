import streamlit as st
import numpy as np #berfungsi untuk memproses komputasi numerik


#ENKRIPSI
def cipher_encryption(msg,key):
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
    #mencetak enkripsi text

    #mencetak hasil akhir Enkripsi
    st.subheader('Ciphertext :')
    st.header(encryp_text)
    expander = st.expander("Detail Hasil Enkripsi")
    expander.write('Plaintext :')
    expander.subheader(msg)
    expander.write('Key :')
    expander.subheader(key)


#DEKRIPSI
def cipher_decryption(msg,key):

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

def app():
    st.write('Ini adalah `Halaman Kriptografi`.')
    st.write('Aplikasi ini dibuat untuk memenuhi tugas `Kriptografi`, algoritma yang digunakan adalah `Hill Cipher` dan `Super Enkripsi`.')
     
    selected = st.selectbox( 'Pilih',
    ('Enkripsi', 'Dekripsi'))
        
    if selected == 'Enkripsi':
        algo = st.selectbox( 'Algoritma',
        ('Hill Chiper', 'Super Enkripsi'))
        st.write('# ENKRIPSI')
        if algo == 'Hill Chiper':
            msg = st.text_input('', placeholder='Masukkan Plaintext').upper()
            key = st.text_input('', placeholder='Enter 4 letter Key String ',max_chars=4).upper()
            if st.button('Enkripsi'):
                cipher_encryption(msg, key)
            else:
                st.subheader('Silahkan input Plaintext dan Key')

    if selected == 'Dekripsi':
        algo = st.selectbox( 'Algoritma',
        ('Hill Chiper', 'Super Enkripsi'))
        st.write('# DEKRIPSI')
        if algo == 'Hill Chiper':
            msg = st.text_input('', placeholder='Masukkan Ciphertext').upper()
            key = st.text_input('', placeholder='Enter 4 letter Key String ',max_chars=4).upper()
            if st.button('Dekripsi'):
                cipher_decryption(msg,key)
            else:
                st.subheader('Silahkan input Ciphertext dan Key')

