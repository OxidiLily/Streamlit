import streamlit as st
from PIL import Image
import streamlit.components.v1 as components

def app():
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
        """,height=300,
)
    image = Image.open('Udinus.jpg')
    

    st.image(image, caption='Universitas Dian Nuswantoro', width=1195)