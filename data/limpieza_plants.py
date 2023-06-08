import pandas as pd
import streamlit as st
import time
from PIL import Image
import re
import base64
import requests
import folium


# Inicializar st.session_state si no existe
if not hasattr(st, 'session_state'):
    st.session_state = {}

dff = pd.read_csv('C:/Users/FX506/Proyect_Plants/data/Plants_To_Plant_2.csv')
df2 = pd.read_csv('C:/Users/FX506/Proyect_Plants/data/Plants_no_img.csv')
dfph = pd.read_csv('C:/Users/FX506/Proyect_Plants/data/Plants_ph.csv')

dff.drop('Unnamed: 0', axis=1, inplace=True)
df2.drop('Unnamed: 0', axis=1, inplace=True)
dfph.drop('Unnamed: 0', axis=1, inplace=True)


def add_bg_from_url(image_url):
    response = requests.get(image_url)
    encoded_string = base64.b64encode(response.content).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url('data:image/png;base64,{encoded_string}');
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def main():
    add_bg_from_url("https://images.pexels.com/photos/6924272/pexels-photo-6924272.jpeg")


if __name__ == "__main__":
    main()



st.sidebar.title('Navigator')

options = st.sidebar.radio('Pages', options=['Home', 'Find your Plant!!!', 'Soil pH Compatibility', 'Plant recognition','Disease detection'])

def page_home():

    image = Image.open('C:/Users/FX506/Proyect_Plants/img/LOGO.png')
    st.image(image, use_column_width=True)

    st.write('\n')

    st.title('Welcome to Plants to Plant')

    st.write('\n')

    st.header('  Are you looking for the perfect plant that fits your lifestyle?')
    col1, col2, col3 = st.columns([5,2,6])

    # Ruta URL del GIF
    gif_url = "https://i.gifer.com/tRt.gif"

    # Mostrar el GIF
    col1.image(gif_url, use_column_width=True)

    st.write('\n')

    col3.markdown('''
            Look no further! Our app is designed to 
            help you find the ideal plant based
            on your preferences.
            We have curated a dataset containing 
            valuable information about various plants,
            including their names, suitable soil pH, plant pH,
            regions they thrive in, genus, family, order,
            placement (indoor, outdoor, or both),
            and watering frequency.''')
    
    col1.subheader('How does it work ?')

    st.write('\n')

    st.markdown('''With our app, you can say goodbye to the hassle of guessing which plant is right for you.
    We have done the hard work of collecting and organizing the data, ensuring that you have all the necessary
    information to keep your plants healthy and thriving. No more buying plants solely for their decorative 
    purposes—our app ensures that you choose plants that you can care for effortlessly.''')
    
    st.header('Take a quick scoope of our plants catalog')

    

def catalog(dataframe):
    # Verificar si el estado 'show_catalog' ya existe en session_state
    if 'show_catalog' not in st.session_state:
        st.session_state.show_catalog = False

    # Verificar si el estado 'show_info' ya existe en session_state
    if 'show_info' not in st.session_state:
        st.session_state.show_info = {}

    # Verificar si el estado 'selected_plant' ya existe en session_state
    if 'selected_plant' not in st.session_state:
        st.session_state.selected_plant = None

    # Crear un botón en Streamlit para mostrar/ocultar el catálogo
    catalog_button = st.button('Catalog')

    # Actualizar el estado 'show_catalog' al hacer clic en el botón
    if catalog_button:
        st.session_state.show_catalog = not st.session_state.show_catalog
        st.session_state.selected_plant = None  # Reiniciar la planta seleccionada al mostrar/ocultar el catálogo

    # Mostrar el catálogo si 'show_catalog' es True
    if st.session_state.show_catalog:
        # Obtener las URL de las imágenes y los nombres de la columna 'Name'
        group_urls = dff['Img url'].tolist()
        group_names = dff['Name'].tolist()

        # Recorrer las URL y los nombres
        if group_urls and group_names:
            for j in range(0, len(group_urls), 4):
                columns = st.columns(4)
                for i, url in enumerate(group_urls[j:j+4]):
                    with columns[i]:
                        st.image(url, use_column_width=True)
                        button_key = f"{group_names[j+i]}_{j+i}"  # Generar una clave única para cada botón
                        if st.button(group_names[j+i], key=button_key):
                            st.session_state.selected_plant = group_names[j+i]  # Actualizar la planta seleccionada
                            st.session_state.show_catalog = False  # Ocultar el catálogo

    # Mostrar la información de la planta seleccionada
    if st.session_state.selected_plant:
        selected_plant_info = dff[dff['Name'] == st.session_state.selected_plant]
        selected_plant_image_url = selected_plant_info['Img url'].values[0]
        st.image(selected_plant_image_url, use_column_width=True)
        st.write(selected_plant_info)


def Find_your_Plant(dataframe):
    
    st.header('Try this filters to find the most accurate plant for your lifestyle')

    # Filtro de pH
    ph_options = ['', 'Acidic', 'Neutral', 'Alkaline']
    selected_ph = st.selectbox('Select pH:', ph_options)

    # Filtro de placement
    placement_options = ['', 'Outdoor', 'Indoor', 'Both']
    selected_placement = st.selectbox('Select Placement:', placement_options)

    # Filtro de watering frequency
    watering_options = ['', 'regularly', 'periodically', 'occasionally']
    selected_watering = st.selectbox('Select watering needed:', watering_options)

    # Botón "Apply Filters"
    apply_filters = st.button("Apply Filters")

    # Aplicar los filtros cuando se hace clic en el botón
    if apply_filters:
        # Aplicar los filtros al DataFrame df2 (es el df sin columna img url)
        filtered_df = df2  # DataFrame moidificado sin columna img

        # Filtrar por pH
        if selected_ph == 'Acidic':
            filtered_df = filtered_df[filtered_df['Plant pH'] <= 6.5]
        elif selected_ph == 'Neutral':
            filtered_df = filtered_df[filtered_df['Plant pH'].between(6.6, 7.3)]
        elif selected_ph == 'Alkaline':
            filtered_df = filtered_df[filtered_df['Plant pH'] >= 7.4]

        # Filtrar por placement
        if selected_placement == 'Outdoor':
            filtered_df = filtered_df[filtered_df['Placement'] == 'Outdoor']
        elif selected_placement == 'Indoor':
            filtered_df = filtered_df[filtered_df['Placement'] == 'Indoor']
        elif selected_placement == 'Both':
            filtered_df = filtered_df[filtered_df['Placement'] == 'Both']

        # Filtrar por watering frequency
        if selected_watering == 'regularly':
            filtered_df = filtered_df[filtered_df['Watering Frequency'].str.contains('regularly', case=False)]
        elif selected_watering == 'periodically':
            filtered_df = filtered_df[filtered_df['Watering Frequency'].str.contains('periodically', case=False)]
        elif selected_watering == 'occasionally':
            filtered_df = filtered_df[filtered_df['Watering Frequency'].str.contains('occasionally', case=False)]


        progress_bar = st.progress(0)

        for perc_completed in range(100):
            time.sleep(0.03)
            progress_bar.progress(perc_completed+1)
            

        # Mostrar el resultado final
        st.write(filtered_df)

def Soil_page():
    # Crea la interfaz de usuario
    st.title('Compatibility Check of plants by pH')

    st.write('\n')

    st.header('Here, you can check the compatibility of your plants to be planted alongside other green buddies.')

    # Obtiene el valor de pH ingresado por el usuario
    ph_value = st.number_input('Enter the pH value:', min_value=0.0, max_value=14.0, value=7.0)

    def extract_average(value):
        pattern = r'(\d+(\.\d+)?)'
        matches = re.findall(pattern, value)
        if matches:
            numbers = [float(match[0]) for match in matches]
            average = sum(numbers) / len(numbers)
            return average
        else:
            return None

    # Aplica la función extract_average a la columna 'Suitable Soil pH'
    dfph['Suitable Soil pH'] = dfph['Suitable Soil pH'].apply(extract_average)

    # Filtra los datos por el valor de pH ingresado
    compatible_plants = dfph[dfph['Suitable Soil pH'].apply(lambda x: x <= ph_value)]

    # Verifica si hay plantas compatibles antes de mostrar la lista
    if not compatible_plants.empty:
        st.subheader('Compatible Plants:')
        st.write(compatible_plants)
    else:
        st.write('Sorry, it appears that we have no match por that pH.')

def pr():
    st.subheader('Here you can upload a photo of your plant so wee can help you recognize it')

    st.write('\n')

    uploaded_photo = st.file_uploader('Upload Photo')
    #camera_photo = st.camera_input('Take a photo')


    if uploaded_photo is not None:
        progress_bar = st.progress(0)

        for perc_completed in range(100):
            time.sleep(0.05)
            progress_bar.progress(perc_completed + 1)


def disease():

    st.subheader('Upload a photo of your plant to see what kind of disease it may have')

    uploaded_photo = st.file_uploader('Upload Photo')
    #camera_photo = st.camera_input('Take a photo')


    if uploaded_photo is not None:
        progress_bar = st.progress(0)

        for perc_completed in range(100):
            time.sleep(0.05)
            progress_bar.progress(perc_completed + 1)



if options == 'Find your Plant!!!':
    Find_your_Plant(df2)

elif options == 'Home':
    page_home(), catalog(dff)

elif options == 'Soil pH Compatibility':
    Soil_page()

elif options == 'Plant recognition':
    pr()

elif options == 'Disease detection':
    disease()





















