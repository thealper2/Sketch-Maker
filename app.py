import streamlit as st
import imageio
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage.filters import gaussian_filter
from PIL import Image

st.sidebar.title("Sketch Maker")
uploaded_file = st.sidebar.text_input("Image File Path")

if st.sidebar.button("Make"):
	img = imageio.imread(uploaded_file)
	gray = np.dot(img[..., :3], [0.299, 0.587, 0.114])

	inverted = (255 - gray)

	blurred = gaussian_filter(inverted, sigma=5)

	dodged = blurred * 255 / (255 - gray)
	dodged[dodged > 255] = 255
	dodged[gray == 255] = 255

	sketch = dodged.astype("uint8")

	plt.imsave("sketch.png", sketch, cmap="gray", vmin=0, vmax=255)

	image = Image.open("sketch.png")
	st.title("Result")
	st.image(image)
