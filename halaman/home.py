from enum import auto
import streamlit as st
from PIL import Image
import streamlit.components.v1 as components

def app():
  
# embed streamlit docs in a streamlit app
    components.html("""
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">

    <style>
    body {
      background-color: #0E1117;
    }
    </style>
    <body>
    <div class="container">
      <div id="myCarousel" class="carousel slide" data-ride="carousel" data-interval="4200">

        <!-- Wrapper for slides -->
        <div class="carousel-inner">
          <div class="item active">
            <img src="https://dinus.ac.id/images/news/cf96a-dscf0092-.jpg" alt="Udinus" style="width:100%;">
          </div>

          <div class="item">
            <img src="https://bob.kemenparekraf.go.id/wp-content/uploads/2021/11/tugu_muda_lawang_sewu_kota_semarang_2019_sam9042-1024x627.jpg" alt="Lawang Sewu" style="width:100%;">
          </div>
        
          <div class="item">
            <img src="https://1.bp.blogspot.com/-PeU32sxbc-I/XvhicmgPQWI/AAAAAAAABMk/S8slvi6wbJoZxp78kFkeQXT5VgdXWkl_gCLcBGAsYHQ/s1600/images%2B%25282%2529.jpeg" alt="Udinus" style="width:100%;">
          </div>
          <div class="item">
            <img src="https://i0.wp.com/bintangmultimedia.com/wp-content/uploads/2020/02/DJI_0522-scaled.jpg?resize=1024%2C576&ssl=1" alt="Tugu Muda" style="width:100%;">
          </div>
        </div>
      </div>
    </div>
    </body>
  """, height=600)


    # bootstrap 4 collapse example
    components.html(
       """
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    
    
    <style>
    .fa {
    padding: 20px;
    font-size: 30px;
    width: 200px;
    text-align: center;
    text-decoration: none;
    margin: 5px 2px;
    }

    .fa:hover {
        opacity: 0.7;
    }

    .fa-facebook {
    background: #3B5998;
    color: white;
    }

    .fa-youtube {
    background: #bb0000;
    color: white;
    }

    .fa-instagram {
    background: #125688;
    color: white;
    }
    </style>
    

    <!-- Perkenalan -->

    <div id="accordion ">
      <div class="card text-bg-dark"  >
        <div class="card-header bg-dark" id="headingOne">
          <h5 class="mb-0">
            <button class="btn btn-link" data-toggle="collapse" data-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne" >
            Perkenalan
            </button>
          </h5>
        </div>
        <div id="collapseOne" class="collapse" aria-labelledby="headingOne" data-parent="#accordion">
          <div class="card-body ">
            <h3>Nama : Tekad Agung Nugroho</h3><br>
            <h3>Nim  : A11.2019.11787</h3>
          </div>
        </div>
      </div>
      <div class="card">
        <div class="card-header bg-dark" id="headingTwo">
          <h5 class="mb-0">
            <button class="btn btn-link collapsed" data-toggle="collapse" data-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
            Media Sosial
            </button>
          </h5>
        </div>
        <div id="collapseTwo" class="collapse show" aria-labelledby="headingTwo" data-parent="#accordion">
          <div class="card-body ">
            
    <h2>Media Sosial</h2>

    <!-- Add font awesome icons -->
    <a href="https://www.facebook.com/profile.php?id=100004792578579" target="_blank" class="fa fa-facebook"></a>
    <a href="https://www.youtube.com/channel/UCxrtQFElAoQnKRWsctp95WA" target="_blank" class="fa fa-youtube"></a>
    <a href="https://www.instagram.com/tekadagungn/" target="_blank" class="fa fa-instagram"></a>
            </div>
            </div>
        </div>
        </div>
        """,height=300)
    
    
    image = Image.open('gambar_udinus.jpg')
    col1, col2, col3 = st.columns([0.2, 5, 0.2])
    with col1:
      st.write(' ')

    with col2:
        st.image(image, use_column_width=True,caption='Universitas Dian Nuswantoro')

    with col3:
      st.write(' ')
    
    