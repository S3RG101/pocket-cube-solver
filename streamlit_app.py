import streamlit as st

def create_cube():
    # Create a 2x2 Rubik's cube with all sides initially set to white
    cube = [['W', 'W'], ['W', 'W']]
    return cube

def render_cube(cube):
    # Render the cube with colors
    st.write('    {}  {}'.format(cube[0][0], cube[0][1]))
    st.write('    {}  {}'.format(cube[1][0], cube[1][1]))


# Create the 2x2 Rubik's cube
cube = create_cube()

# Define the color options
color_options = ['W', 'R', 'B', 'O', 'G', 'Y']

# Set the default color for each position
color_mapping = {(0, 0): 'W', (0, 1): 'W', (1, 0): 'W', (1, 1): 'W'}

# Render the UI for color input
st.title("2x2 Rubik's Cube Color Input")

st.write("Enter the colors for each position on the cube:")

for i in range(2):
    for j in range(2):
        color = st.selectbox(
            f'Position ({i},{j})',
            options=color_options,
            index=color_options.index(color_mapping[(i, j)])
        )
        color_mapping[(i, j)] = color

# Update the cube with the selected colors
for i in range(2):
    for j in range(2):
        cube[i][j] = color_mapping[(i, j)]

# Render the cube
st.write("Rubik's Cube:")
render_cube(cube)



