import streamlit as st
import mysql.connector
from mysql.connector import Error
from io import BytesIO

st.set_page_config(page_title="Your Foot Doctor", page_icon=":feet:", layout="wide", )

with st.container():
    st.title('YFD')
    st.subheader('Your feet doctor')
    
    
    
# Define database connection
def create_conn():
    conn = None
    try:
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Yash2402@",
            database="yfd2",
            auth_plugin='mysql_native_password'
        )
        return conn
    except Error as e:
        print(e)

# Define function to save image to databas
def save_image_to_database(image, conn):
    cursor = conn.cursor()
    try:
        query = "INSERT INTO images (image) VALUES (%s)"
        cursor.execute(query, (image,))
        conn.commit()
        st.success("Image saved to database")
    except Error as e:
        print(e)
        st.error("Error saving image to database")

# Define Streamlit app
def app():
    st.title("Image uploader")
    st.write("Upload an image and save it to the database")

    # Get user input
    image = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

    # If user has uploaded an image
    if image is not None:
        # Display the image
        st.image(image)

        # Convert the uploaded file to bytes
        # image_bytes = BytesIO(image.read())

        # Save the image to the database
        conn = create_conn()
        save_image_to_database(image, conn)

if __name__ == '__main__':
    app()

