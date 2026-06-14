import streamlit as st
import requests
from PIL import Image

# ==========================================
# Streamlit Page Config
# ==========================================

st.set_page_config(
    page_title="Plant Disease Detection",
    layout="centered"
)

# ==========================================
# Title
# ==========================================

st.title("Plant Disease Detection System")

st.write("Upload a plant leaf image to detect disease.")

# ==========================================
# Upload Image
# ==========================================

uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "jpeg", "png"]
)

# ==========================================
# Prediction
# ==========================================

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )

    # Predict Button
    if st.button("Predict Disease"):

        with st.spinner("Predicting..."):

            files = {
                "file": uploaded_file.getvalue()
            }

            response = requests.post(
                "http://backend:8000/predict",
                files=files
            )

            result = response.json()

            predicted_class = result["predicted_class"]

            confidence = result["confidence"]

            st.success(
                f"Prediction: {predicted_class}"
            )

            st.info(
                f"Confidence: {confidence}%"

            )


