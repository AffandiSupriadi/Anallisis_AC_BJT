import streamlit as st
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt


st.set_page_config(
    page_title="Bipolar Junction Transistors AC Analysis",
    page_icon="❤️",
)


st.header("Bipolar Junction Transistors AC Analysis")
st.write("by: Affandi Supriadi")
st.write("Dosen Pengampu: Ir. Rustamaji, M.T")
st.sidebar.success("pilih perhitungan yang anda inginkan")
st.write(
    "Saya Affandi Supriadi dengan NRP 11-2021-020 mempersembahkan Aplikasi web perhitungan Analisis AC BJT. Untuk memenuhi tugas dari mata kuliah Elektrinika Analog. Silahkan klik tanda “>” disebelah kiri atas untuk memulai perhitungan."
)
st.write("---")
