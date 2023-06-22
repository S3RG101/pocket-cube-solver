import streamlit as st
import numpy as np
from annotated_text import annotated_text

def create_cube():
    # Create a 2x2 Rubik's cube with all sides initially set to white
    cube = np.array([['W', 'W'], ['W', 'W']])
    return cube

def render_cube(cube):
    # Render the 2D representation of the cube
    annotated_text((cube[0][0], "", ""#8ef""))
    st.write(f'{cube[0][0]} ─ {cube[0][1]}')
    st.write('    │       │')
    st.write(f'{cube[1][0]} ─ {cube[1][1]}')


# Create the 2x2 Rubik's cube
cube = create_cube()

# Define the color options
color_options = ['W', 'R', 'B', 'O', 'G', 'Y']

# Set the default colors for each position
color_mapping = {
    (0, 0): 'W',
    (0, 1): 'W',
    (1, 0): 'W',
    (1, 1): 'W',
}

# Render the UI for color input
st.title("2x2 Rubik's Cube Color Input")

st.write("Enter the colors for each position on the cube:")

col1, col2 = st.columns(2)
with col1:
    color_mapping[(0, 0)] = st.selectbox(
        'Top Left',
        options=color_options,
        index=color_options.index(color_mapping[(0, 0)])
    )
    color_mapping[(1, 0)] = st.selectbox(
        'Bottom Left',
        options=color_options,
        index=color_options.index(color_mapping[(1, 0)])
    )
with col2:
    color_mapping[(0, 1)] = st.selectbox(
        'Top Right',
        options=color_options,
        index=color_options.index(color_mapping[(0, 1)])
    )
    color_mapping[(1, 1)] = st.selectbox(
        'Bottom Right',
        options=color_options,
        index=color_options.index(color_mapping[(1, 1)])
    )

# Update the cube with the selected colors
for i in range(2):
    for j in range(2):
        cube[i][j] = color_mapping[(i, j)]

# Render the cube
st.write("Rubik's Cube:")
render_cube(cube)
