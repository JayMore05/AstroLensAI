import streamlit as st

from modules.preprocessing import preprocess_image
from modules.detection import extract_features

st.set_page_config(
    page_title="AstroLensAI",
    page_icon="🌌",
    layout="wide"
)

st.title("🌌 AstroLensAI")
st.subheader("AI Powered Astronomy Image Classification")

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Menu",
    ["Home", "About"]
)

if page == "Home":

    st.header("Upload Astronomy Image")

    uploaded = st.file_uploader(
        "Upload JPG / PNG",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded is not None:

        st.image(uploaded, use_container_width=True)

        if st.button("Analyze"):

            image = preprocess_image(uploaded)

            features = extract_features(image)

            st.success("Image Processed Successfully")

            names = [
                "Mean Red",
                "Mean Green",
                "Mean Blue",
                "Std Red",
                "Std Green",
                "Std Blue",
                "Brightness"
            ]

            st.subheader("Extracted Features")

            for name, value in zip(names, features):
                st.write(f"**{name}:** {value:.4f}")

else:

    st.header("About")

    st.write("AstroLensAI - AI Powered Astronomy Image Classification")