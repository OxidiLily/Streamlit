import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import  StandardScaler
import streamlit as st
import mitosheet
import plotly.express as px
import streamlit.components.v1 as components



def app():
    def build_model(df):
        df = df.loc[:100] # FOR TESTING PURPOSE, COMMENT THIS OUT FOR PRODUCTION
        X = df.iloc[:,:-1] # Using all column except for the last column as X
        Y = df.iloc[:,-1] # Selecting the last column as Y

        st.markdown('**Dataset dimension**')
        st.write('X')
        st.info(X.shape)
        st.write('Y')
        st.info(Y.shape)

        st.markdown('**Variable details**:')
        st.write('X variable (20 pertama ditampilkan)')
        st.info(list(X.columns[:20]))    
        st.write('Y variable')
        st.info(Y.name)
        

    def build_model2(df):
        df = df.loc[:100] # FOR TESTING PURPOSE, COMMENT THIS OUT FOR PRODUCTION
        X = df.iloc[:,:-1] # Using all column except for the last column as X
        Y = df.iloc[:,-1] # Selecting the last column as Y

        st.markdown('**Dataset dimension**')
        st.write('X')
        st.info(X.shape)
        st.write('Y')
        st.info(Y.shape)

        st.markdown('**Variable details**:')
        st.write('X variable (20 pertama ditampilkan)')
        st.info(list(X.columns[:20]))    
        st.write(X)
        st.write('Y variable')
        st.info(Y.name)
        st.write(Y)

        st.subheader('Untuk Klasifikasi Dataset')
        metric = st.selectbox(
        "Metric",
        ('minkowski','euclidean'), disabled = True)
        params =  st.number_input('Masukkan angka max 1000',min_value=1,max_value=1000)
        p = st.number_input('Masukkan angka max 100',min_value=1,max_value=100)
        ts =  st.number_input('Masukkan angka test size max 1,00',min_value= 0.01,max_value=1.0,value=0.01)
        rs = st.number_input('Masukkan angka random state max 10',min_value=0,max_value=10)
        
        if st.button('Tekan Untuk Proses Dataset'):
            
            # Menggunakan MITO
            mitosheet.sheet()
                        
            st.subheader('Hasil Proses Dataset')
            # Imported healthcare-dataset-stroke-data.csv
            healthcare_dataset_stroke_data = pd.read_csv(r'healthcare-dataset-stroke-data.csv')
            
            # Filtered bmi
            healthcare_dataset_stroke_data = healthcare_dataset_stroke_data[healthcare_dataset_stroke_data['bmi'].notnull()]

            # Filtered avg_glucose_level
            healthcare_dataset_stroke_data = healthcare_dataset_stroke_data[healthcare_dataset_stroke_data['avg_glucose_level'].notnull()]
            st.write(healthcare_dataset_stroke_data)

            a = healthcare_dataset_stroke_data.iloc[:,[2,8,9]]
            b = healthcare_dataset_stroke_data.iloc[:,-1]
            st.subheader('Dataset yang digunakan')
            st.write(a)

            x_train, x_test, y_train, y_test = train_test_split(a, b, test_size =ts, random_state = rs)
            sc = StandardScaler()
            x_train = sc.fit_transform(x_train)
            x_test = sc.transform(x_test)

            classifier = KNeighborsClassifier(n_neighbors = params, metric = metric, p = p)
            classifier.fit(x_train,y_train)
            y_pred = classifier.predict(x_test)
            cm = confusion_matrix(y_test, y_pred)

            acc = accuracy_score(y_test,y_pred)
            st.write(f'Akurasi = ',acc)
            
            st.subheader('Graph ')
            st.write('Arahkan cursor ke kebagian pojok kanan atas atau ke area Graph pada hasil Graph untuk melihat lebih detail')
            
            # Filter the dataframe so that it does not crash the browser
            dataset_stroke_data_filtered = healthcare_dataset_stroke_data.head(1000)

            # Construct the graph and style it. Further customize your graph by editing this code.
            # See Plotly Documentation for help: https://plotly.com/python/plotly-express/
            fig = px.histogram(dataset_stroke_data_filtered, x=['age', 'avg_glucose_level', 'bmi'], y='stroke')
            fig.update_layout(
                title='age, avg_glucose_level, bmi, stroke (first 1000 rows) histogram', 
                xaxis = dict(
                    rangeslider = dict(
                        visible=True, 
                        thickness=0.05
                    )
                ), 
                yaxis = dict(

                ), 
                barmode='group', 
                paper_bgcolor='#FFFFFF', 
                showlegend=True
            )
            
            fig.show(renderer="iframe")
            
            st.write(fig)
            # pca = PCA(2)
            # x_projected = pca.fit_transform(a)
            # x1 = x_projected[:,0]
            # x2 = x_projected[:,1]
            # fig = plt.figure()
            # plt.scatter(x1,x2,c=b,alpha=0.8, cmap='viridis')
            # plt.xlabel('Principal Component 1')
            # plt.ylabel('Principal Component 2')
            # plt.colorbar()
            # st.pyplot(fig)

    st.sidebar.header('WELCOME')
    
    st.sidebar.warning('PERHATIAN')
    st.sidebar.write(""" 
    Sebelum memasukkan data mohon untuk [Download file CSV disini](https://drive.google.com/drive/folders/1pjunmVTvKixg7yq7H5ArCY8VitVv1pSF?usp=sharing)""")

    st.sidebar.subheader('Hanya bisa memproses file CSV yang terdapat pada link di atas')
    st.subheader('Dataset')

    #---------------------------------#
    # Sidebar - Collects user input features into dataframe
    
    uploaded_file = st.file_uploader("Upload your input CSV file", type=["csv"])
    if uploaded_file is not None:
        df= pd.read_csv(uploaded_file)
        st.markdown('**Dataset**')
        st.write(df)
        build_model2(df)
    else:
        st.info('Menunggu CSV file di upload.')
        if st.button('Tekan Untuk Contoh Dataset'):
            # Diabetes dataset
            diabetes = load_diabetes()
            X = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
            Y = pd.Series(diabetes.target, name='response')
            df = pd.concat( [X,Y], axis=1 )

            st.markdown('Contoh menggunakan `Dataset Diabetes`.')
            st.write(df.head(5))

            # Boston housing dataset
            # boston = load_boston()
            # #X = pd.DataFrame(boston.data, columns=boston.feature_names)
            # #Y = pd.Series(boston.target, name='response')
            # X = pd.DataFrame(boston.data, columns=boston.feature_names).loc[:100] # FOR TESTING PURPOSE, COMMENT THIS OUT FOR PRODUCTION
            # Y = pd.Series(boston.target, name='response').loc[:100] # FOR TESTING PURPOSE, COMMENT THIS OUT FOR PRODUCTION
            # df = pd.concat( [X,Y], axis=1 )

            # st.markdown('The Boston housing dataset is used as the example.')
            # st.write(df.head(5))

            build_model(df)

