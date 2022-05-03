import streamlit as st
import matplotlib.pyplot as plt
from math_plot_coords_utils import *
from string_utils import *

plt.style.use('bmh')


def plot_coords(coords, bare_plot=False):
    if bare_plot:
        plt.axis('off')
    plt.margins(x=0.1, y=0.1)
    plt.axes().set_aspect('equal', 'datalim')
    X, Y = zip(*coords)
    fig, ax = plt.subplots()
    plt.plot(X, Y)
    st.pyplot(fig)


st.title("L System")

pattern_l = st.text_input("Enter the pattern of L:")
pattern_r = st.text_input("Enter the pattern of R:")

iterations = st.text_input("Enter the number of repetitions: ")
rotation_angle = st.text_input("Enter the rotation angle: ")

plot_l_system = st.button('Plot L-System')

if plot_l_system and rotation_angle and iterations and pattern_r and pattern_l:
    plot_coords(turtle_to_coords(transform_multiple('L', {
        'L': pattern_l,
        'R': pattern_r
    }, int(iterations)), int(rotation_angle)))
