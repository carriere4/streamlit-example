# import altair as alt
# import numpy as np
# import pandas as pd
# import streamlit as st

# """
# # Welcome to Streamlit!

# Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
# If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
# forums](https://discuss.streamlit.io).

# In the meantime, below is an example of what you can do with just a few lines of code:
# """

# num_points = st.slider("Number of points in spiral", 1, 10000, 1100)
# num_turns = st.slider("Number of turns in spiral", 1, 300, 31)

# indices = np.linspace(0, 1, num_points)
# theta = 2 * np.pi * num_turns * indices
# radius = indices

# x = radius * np.cos(theta)
# y = radius * np.sin(theta)

# df = pd.DataFrame({
#     "x": x,
#     "y": y,
#     "idx": indices,
#     "rand": np.random.randn(num_points),
# })

# st.altair_chart(alt.Chart(df, height=700, width=700)
#     .mark_point(filled=True)
#     .encode(
#         x=alt.X("x", axis=None),
#         y=alt.Y("y", axis=None),
#         color=alt.Color("idx", legend=None, scale=alt.Scale()),
#         size=alt.Size("rand", legend=None, scale=alt.Scale(range=[1, 150])),
#     ))
import streamlit as st
import matplotlib.pyplot as plt

def gartner_quadrant(points):
    # Your Gartner quadrant plotting logic here
    # Use matplotlib to create the quadrant and place points

    # Example: Scatter plot with points
    plt.scatter(points[:, 0], points[:, 1])
    plt.xlabel("X-axis Label")
    plt.ylabel("Y-axis Label")
    plt.title("Gartner Quadrant")
    st.pyplot()

# Sample points data (replace this with your data)
sample_points = [[1, 2], [3, 4], [2, 3], [4, 2]]

# Streamlit app
st.title("Gartner Quadrant Streamlit App")
st.sidebar.header("Settings")

# Sidebar options (customize as needed)
# You can add sliders, input fields, etc., for user interaction
# Example: x_range = st.sidebar.slider("X-axis Range", 0, 10, (0, 10))

# Call the function to plot Gartner quadrant
gartner_quadrant(sample_points)
