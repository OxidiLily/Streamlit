from tracemalloc import stop
from streamlit_option_menu import option_menu
import streamlit as st
from halaman import inputData
from multipage import MultiApp
import streamlit.components.v1 as components


def app():
    st.header('Selamat Datang')
    app = MultiApp()
    st.subheader('Sebelum mulai. Silahkan download dataset terlebih dahulu')
    st.write('*Centang box unntuk membuat link')
    cek1 = st.checkbox('Buat Link')
    if cek1:
        st.success('Link Berhasil dibuat')
        col1, col2, col3 = st.columns([4.2, 5, 1.5])
        with col1:
            st.write(' ')
        with col2:
            components.html(
                        """
                        <meta name="viewport" content="width=device-width, initial-scale=1">
                        <!-- Add icon library -->
                        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

                        <style>
                        .btn {
                        background-color: DodgerBlue;
                        border: none;
                        color: white;
                        padding: 12px 30px;
                        cursor: pointer;
                        font-size: 20px;
                        }

                        /* Darker background on mouse-over */
                        .btn:hover {
                        background-color: RoyalBlue;
                        }
                        </style>
                        <a href="https://drive.google.com/drive/folders/1pjunmVTvKixg7yq7H5ArCY8VitVv1pSF" target="_blank">
                        <button class="btn"><i class="fa fa-download"></i> Download Dataset</button></a>
                            """,height=100)
        with col3:
            st.write(' ')
        st.subheader('Apakah anda sudah benar-benar mendownload Dataset pada link?')
        cek2 = st.checkbox('Sudah')
        if cek2:
            app.add_app("Dataset",inputData.app)
            app.run() 

    else:
        st.warning("Perhatian")
        st.header('Web ini hanya bisa memproses file `CSV` yang ada pada Link')
        st.subheader('Harap Download Dataset terlebih dahulu sebelum melanjutkan')
    
        
    # def awal():
    #     if st.write == None :
    #         isi()
    #     else:
           
    #         agree = st.checkbox('Buat Link Download')

    #         if agree:   
    #             st.success('Buat Link Berhasil')
    #             st.header(""" 
    #             Sebelum melanjutkan dataset mohon untuk [Download file CSV disini](https://drive.google.com/drive/folders/1pjunmVTvKixg7yq7H5ArCY8VitVv1pSF?usp=sharing)
    #             """)
    #             st.header('atau')
                # components.html(
                #     """
                #     <meta name="viewport" content="width=device-width, initial-scale=1">
                #     <!-- Add icon library -->
                #     <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

                #     <style>
                #     .btn {
                #     background-color: DodgerBlue;
                #     border: none;
                #     color: white;
                #     padding: 12px 30px;
                #     cursor: pointer;
                #     font-size: 20px;
                #     }

                #     /* Darker background on mouse-over */
                #     .btn:hover {
                #     background-color: RoyalBlue;
                #     }
                #     </style>
                #     <a href="https://drive.google.com/drive/folders/1pjunmVTvKixg7yq7H5ArCY8VitVv1pSF" target="_blank">
                #     <button class="btn"><i class="fa fa-download"></i> Download Dataset</button></a>
                #         """,height=100)
    #             if st.button('Klik untuk melanjutkan'):
    #                 st.header('Pastikan anda telah meng-download file CSV')  
    #                 kon = st.checkbox('Konfirmasi')
    #                 if kon :
    #                     if st.button('Konfirm'):
    #                         isi()
                        
    #         else:
    #             st.button('Klik untuk melanjutkan',disabled=True)
    #             st.header('Aplikasi ini hanya bisa memproses `File CSV` yang ada pada link.') 
    #             st.warning('PERHATIAN')
                               

        
    