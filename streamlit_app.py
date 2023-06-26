import streamlit as st
# import numpy as np
from annotated_text import annotated_text
import tree_search as ts

def create_cube():
    # Create a 2x2 Rubik's cube with all sides initially set to white
    #cube = np.array([['W', 'W'], ['W', 'W']])
    # start top or bottom and go clockwise
    # solved_cube = np.array([['W','B','R'],['W','R','G'],['W','G','O'],['W','O','B'],['Y','R','B'],['Y','G','R'],['Y','O','G'],['Y','B','O']])
    
    # cube = np.array([['W','B','R'],['W','W','W'],['W','W','W'],['W','W','W'],['W','W','W'],['W','W','W'],['W','W','W'],['W','W','W']])
    cube = [['W','B','R'],['W','W','W'],['W','W','W'],['W','W','W'],['W','W','W'],['W','W','W'],['W','W','W'],['W','W','W']]
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

col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)

with col1:
    for i in range(7):
        st.write("")
    color_mapping[(7, 1)] = st.selectbox(
        '0',
        options=color_options,
        index=color_options.index(color_mapping[(7, 1)]),
        label_visibility="collapsed"
    )
    color_mapping[(3, 2)] = st.selectbox(
        '1',
        options=color_options,
        index=color_options.index(color_mapping[(3, 2)]),
        label_visibility="collapsed"
    )
with col2:
    for i in range(7):
        st.write("")
    color_mapping[(4, 2)] = st.selectbox(
        '2',
        options=color_options,
        index=color_options.index(color_mapping[(4, 2)]),
        label_visibility="collapsed"
    )
    color_mapping[(0, 1)] = st.selectbox(
        '3',
        options=color_options,
        index=color_options.index(color_mapping[(0, 1)]),
        label_visibility="collapsed"
    )
with col3:
    color_mapping[(7, 0)] = st.selectbox(
        '4',
        options=color_options,
        index=color_options.index(color_mapping[(7, 0)]),
        label_visibility="collapsed"
    )
    color_mapping[(4, 0)] = st.selectbox(
        '5',
        options=color_options,
        index=color_options.index(color_mapping[(4, 0)]),
        label_visibility="collapsed"
    )
    color_mapping[(4, 1)] = st.selectbox(
        '6',
        options=color_options,
        index=color_options.index(color_mapping[(4, 1)]),
        label_visibility="collapsed"
    )
    color_mapping[(0, 2)] = st.selectbox(
        '7',
        options=color_options,
        index=color_options.index(color_mapping[(0, 2)]),
        label_visibility="collapsed"
    )
    color_mapping[(0, 0)] = st.selectbox(
        '8',
        options=color_options,
        index=color_options.index(color_mapping[(0, 0)]),
        label_visibility="collapsed"
    )
    color_mapping[(3, 0)] = st.selectbox(
        '9',
        options=color_options,
        index=color_options.index(color_mapping[(3, 0)]),
        label_visibility="collapsed"
    )
with col4:
    color_mapping[(6, 0)] = st.selectbox(
        '10',
        options=color_options,
        index=color_options.index(color_mapping[(6, 0)]),
        label_visibility="collapsed"
    )
    color_mapping[(5, 0)] = st.selectbox(
        '11',
        options=color_options,
        index=color_options.index(color_mapping[(5, 0)]),
        label_visibility="collapsed"
    )
    color_mapping[(5, 2)] = st.selectbox(
        '12',
        options=color_options,
        index=color_options.index(color_mapping[(5, 2)]),
        label_visibility="collapsed"
    )
    color_mapping[(1, 1)] = st.selectbox(
        '13',
        options=color_options,
        index=color_options.index(color_mapping[(1, 1)]),
        label_visibility="collapsed"
    )
    color_mapping[(1, 0)] = st.selectbox(
        '14',
        options=color_options,
        index=color_options.index(color_mapping[(1, 0)]),
        label_visibility="collapsed"
    )
    color_mapping[(2, 0)] = st.selectbox(
        '15',
        options=color_options,
        index=color_options.index(color_mapping[(2, 0)]),
        label_visibility="collapsed"
    )
with col5:
    for i in range(7):
        st.write("")
    color_mapping[(5, 1)] = st.selectbox(
        '16',
        options=color_options,
        index=color_options.index(color_mapping[(5, 1)]),
        label_visibility="collapsed"
    )
    color_mapping[(1, 2)] = st.selectbox(
        '17',
        options=color_options,
        index=color_options.index(color_mapping[(1, 2)]),
        label_visibility="collapsed"
    )
with col6:
    for i in range(7):
        st.write("")
    color_mapping[(6, 2)] = st.selectbox(
        '18',
        options=color_options,
        index=color_options.index(color_mapping[(6, 2)]),
        label_visibility="collapsed"
    )
    color_mapping[(2, 1)] = st.selectbox(
        '19',
        options=color_options,
        index=color_options.index(color_mapping[(2, 1)]),
        label_visibility="collapsed"
    )
with col7:
    for i in range(7):
        st.write("")
    color_mapping[(6, 1)] = st.selectbox(
        '20',
        options=color_options,
        index=color_options.index(color_mapping[(6, 1)]),
        label_visibility="collapsed"
    )
    color_mapping[(2, 2)] = st.selectbox(
        '21',
        options=color_options,
        index=color_options.index(color_mapping[(2, 2)]),
        label_visibility="collapsed"
    )
with col8:
    for i in range(7):
        st.write("")
    color_mapping[(7, 2)] = st.selectbox(
        '22',
        options=color_options,
        index=color_options.index(color_mapping[(7, 2)]),
        label_visibility="collapsed"
    )
    color_mapping[(3, 1)] = st.selectbox(
        '23',
        options=color_options,
        index=color_options.index(color_mapping[(3, 1)]),
        label_visibility="collapsed"
    )



# Update the cube with the selected colors
for i in range(8):
    for j in range(3):
        cube[i][j] = color_mapping[(i, j)]

st.write("Rubik's Cube:")
# Render the 2D representation of the cube
annotated_text(("", "", "#FFF"), ("", "", "#FFF"), ("", "", "#FFF"), (cube[7][0], "", color_hex[color_options.index(cube[7][0])]), (cube[6][0], "", color_hex[color_options.index(cube[6][0])]))
annotated_text(("", "", "#FFF"), ("", "", "#FFF"), ("", "", "#FFF"), (cube[4][0], "", color_hex[color_options.index(cube[4][0])]), (cube[5][0], "", color_hex[color_options.index(cube[5][0])]))

annotated_text((cube[7][1], "", color_hex[color_options.index(cube[7][1])]), 
               (cube[4][2], "", color_hex[color_options.index(cube[4][2])]), 
               (cube[4][1], "", color_hex[color_options.index(cube[4][1])]),
               (cube[5][2], "", color_hex[color_options.index(cube[5][2])]), 
               (cube[5][1], "", color_hex[color_options.index(cube[5][1])]), 
               (cube[6][2], "", color_hex[color_options.index(cube[6][2])]),
               (cube[6][1], "", color_hex[color_options.index(cube[6][1])]), 
               (cube[7][2], "", color_hex[color_options.index(cube[7][2])]))

annotated_text((cube[3][2], "", color_hex[color_options.index(cube[3][2])]), 
               (cube[0][1], "", color_hex[color_options.index(cube[0][1])]), 
               (cube[0][2], "", color_hex[color_options.index(cube[0][2])]),
               (cube[1][1], "", color_hex[color_options.index(cube[1][1])]), 
               (cube[1][2], "", color_hex[color_options.index(cube[1][2])]), 
               (cube[2][1], "", color_hex[color_options.index(cube[2][1])]),
               (cube[2][2], "", color_hex[color_options.index(cube[2][2])]), 
               (cube[3][1], "", color_hex[color_options.index(cube[3][1])]))

annotated_text(("", "", "#FFF"), ("", "", "#FFF"), ("", "", "#FFF"), (cube[0][0], "", color_hex[color_options.index(cube[0][0])]), (cube[1][0], "", color_hex[color_options.index(cube[1][0])]))
annotated_text(("", "", "#FFF"), ("", "", "#FFF"), ("", "", "#FFF"), (cube[3][0], "", color_hex[color_options.index(cube[3][0])]), (cube[2][0], "", color_hex[color_options.index(cube[2][0])]))

#the index of the list is the piece
# solved_cube = np.array([['W','B','R'],['W','R','G'],['W','G','O'],['W','O','B'],['Y','R','B'],['Y','G','R'],['Y','O','G'],['Y','B','O']])
solved_cube = [['W','B','R'],['W','R','G'],['W','G','O'],['W','O','B'],['Y','R','B'],['Y','G','R'],['Y','O','G'],['Y','B','O']]

def get_piece(corner):
    for idx,piece in enumerate(solved_cube):
        if set(piece) == set(corner):
            if corner[0]=='W' or corner[0]=='Y':
                orientation = 0
            elif corner[2]=='W' or corner[2]=='Y':
                orientation = 2
            elif corner[1]=='W' or corner[1]=='Y':
                orientation = 1
            return [idx,orientation]
    return [8,8]

prog_cube=[]
for corner in cube:
    prog_cube.append(get_piece(corner))

# fed it into the other python script to solve it
if st.button('Solve!'):
    mixed_cube = ts.Cube(scramble=prog_cube)
    depth, moves = ts.solve_cube(mixed_cube)
    st.write(f'Found a solution of depth {depth} which is the following: {moves}')

moves_dic = {
    "r":"Rp.png",
    "R":"R.png",
    "R2":"2R.png",
    "u":"Up.png",
    "U":f"U.png",
    "U2":"2U.png",
    "b":"Bp.png",
    "B":"B.png",
    "B2":"2B.png"
}

move_arr = moves.split()

send_img_count = 0
def send_img():
    try:
        img = moves_dic[move_arr[send_img_count]]
        send_img_count += 1
        return img
    except:
        return None

dr1, dr2, dr3, dr4, dr5, dr6 = st.columns(6)

with dr1:
    st.image(send_img())
with dr2:
    st.image(send_img())
with dr3:
    st.image(send_img())
with dr4:
    st.image(send_img())
with dr5:
    st.image(send_img())
with dr6:
    st.image(send_img())
with dr1:
    st.image(send_img())
with dr2:
    st.image(send_img())
with dr3:
    st.image(send_img())
with dr4:
    st.image(send_img())
with dr5:
    st.image(send_img())
with dr6:
    st.image(send_img())
