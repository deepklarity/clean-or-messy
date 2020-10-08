from fastai.vision.all import *
from PIL import Image
import streamlit as st
import numpy as np
from io import BytesIO
from .config import imgWidth, imgHeight

st.title("CleanvsMessy")
st.markdown('''
## Upload the image''',True)
st.set_option('deprecation.showfileUploaderEncoding', False)
file = st.file_uploader(" ")
model = load_learner('model/model_v0.pkl')
st.markdown('''
## Preview of the Image''',True)

if file != None:
    st.image(file, width = imgWidth, height = imgHeight)

if file != None:
    def upload(file):
        image = Image.open(file)
        image_np = np.array(image)
        image_without_alpha = image_np[:, :, :3]
        is_clean, _, probs = model.predict(image_without_alpha)
        prob = float(list(probs.numpy())[1])
        return {"is_image_clean": is_clean, "predictedVal": prob}
    result = upload(file)

    st.write("Is Image Clean? "+result["is_image_clean"])
    st.write("Confidence "+str(result["predictedVal"]))