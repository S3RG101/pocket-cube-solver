import streamlit as st
import numpy as np
from annotated_text import annotated_text

def create_cube():
    # Create a 2x2 Rubik's cube with all sides initially set to white
    #cube = np.array([['W', 'W'], ['W', 'W']])
    # start top or bottom and go clockwise
    #solved_cube = np.array([['W','B','R'],['W','R','G'],['W','G','O'],['W','O','B'],['Y','R','B'],['Y','G','R'],['Y','O','G'],['Y','B','O']])
    cube = np.array([['W','B','R'],['W','W','W'],['W','W','W'],['W','W','W'],['W','W','W'],['W','W','W'],['W','W','W'],['W','W','W']])
    return cube

# Create the 2x2 Rubik's cube
cube = create_cube()

# Define the color options
color_options = ['W', 'R', 'B', 'O', 'G', 'Y']
color_hex = ["#FEE","#F00","#00F","#F70","#6C0","#FF0"]

# Set the default colors for each position
color_mapping = {
    (0, 0): 'W',
    (0, 1): 'B',
    (0, 2): 'R',
    (1, 0): 'W',
    (1, 1): 'W',
    (1, 2): 'W',
    (2, 0): 'W',
    (2, 1): 'W',
    (2, 2): 'W',
    (3, 0): 'W',
    (3, 1): 'W',
    (3, 2): 'W',
    (4, 0): 'W',
    (4, 1): 'W',
    (4, 2): 'W',
    (5, 0): 'W',
    (5, 1): 'W',
    (5, 2): 'W',
    (6, 0): 'W',
    (6, 1): 'W',
    (6, 2): 'W',
    (7, 0): 'W',
    (7, 1): 'W',
    (7, 2): 'W',
}

# Render the UI for color input
st.title("2x2 Rubik's Cube Optimal Solver")
st.write("Please orient the cube such that the white, red and blue corner is located as shown")
st.write("Enter the colors for each position on the cube:")

# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "collapsed"

col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)

with col1:
    st.write("")
    st.write("")
    color_mapping[(7, 1)] = st.selectbox(
        'Top Left',
        options=color_options,
        index=color_options.index(color_mapping[(7, 1)])
    )
    color_mapping[(3, 2)] = st.selectbox(
        'Bottom Left',
        options=color_options,
        index=color_options.index(color_mapping[(3, 2)])
    )
with col2:
    st.write("")
    st.write("")
    color_mapping[(4, 2)] = st.selectbox(
        'Top Right',
        options=color_options,
        index=color_options.index(color_mapping[(4, 2)])
    )
    color_mapping[(0, 1)] = st.selectbox(
        'Bottom Right',
        options=color_options,
        index=color_options.index(color_mapping[(0, 1)])
    )

# Update the cube with the selected colors
for i in range(2):
    for j in range(2):
        cube[i][j] = color_mapping[(i, j)]

st.write("Rubik's Cube:")
# Render the 2D representation of the cube
annotated_text((cube[0][0], "", color_hex[color_options.index(cube[0][0])]), (cube[0][1], "", color_hex[color_options.index(cube[0][1])]))
annotated_text((cube[1][0], "", color_hex[color_options.index(cube[1][0])]), (cube[1][1], "", color_hex[color_options.index(cube[1][1])]))
