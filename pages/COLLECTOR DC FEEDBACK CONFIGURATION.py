import streamlit as st
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt


st.title("COMMON-EMITTER FIXED-BIAS CONFIGURATION")
st.write("---")
st.header("Mencari Zi, Zo dan Av")
st.image("rang5.png",width=400)
RF1 = st.number_input("Masukkan nilai RF1 (Ω) = ")
RF2 = st.number_input("Masukkan nilai RF2 (Ω) = ")
RC = st.number_input("Masukkan nilai RC (Ω) = ")
VCC = st.number_input("Masukkan nilai VCC (volt) = ")
VBE = st.number_input("Masukkan nilai VBE (volt) = ")
β = st.number_input("Masukkan nilai β = ")
ro = st.number_input("Masukkan nilai ro (Ω) = ")
Vi = st.number_input("Masukkan nilai Vi (volt)=")

hitung = st.button("Hitung")
test1 = ro
test2 = 10*RC

if hitung:
    IB = (VCC-VBE)/((RF1+RF2)+(β*RC))
    IE = (β + 1)* IB
    re = 0.026 / IE

    X = β * re
    Zi = "{:.2e}".format((RF1 * X)/(RF1 + X))
    Zi = Zi.replace("e+03"," k")
    st.write("Nilai Zi =",Zi,"Ω")
    if test1 >= test2:
        Zo = "{:.2e}".format((RC*RF2)/(RC+RF2))
        Zo = Zo.replace("e+03"," k")
        st.write("Nilai Zo =",Zo ,"Ω")
        Av = round(-((RC*RF2)/(RC+RF2))/re, 0)
        st.write("Nilai Av =",Av)
    elif test1 < test2:
        Zo = "{:.2e}".format((((RC*RF2)/(RC+RF2))*ro)/(((RC*RF2)/(RC+RF2))+ro))
        Zo = Zo.replace("e+03"," k")
        st.write("Nilai Zo =",Zo ,"Ω")
        Av = round(-((((RC*RF2)/(RC+RF2))*ro)/(((RC*RF2)/(RC+RF2))+ro))/re, 0)
        st.write("Nilai Av =",Av)


    def sinusoidal():
        t = np.linspace(-0.05, 0.05, 1000)
        phase_shift = 180  # Phase shift in degrees
        
        # Calculate the sinusoidal signals
        hasil_Vi = Vi * np.sin(2 * np.pi * 50 * t + np.deg2rad(phase_shift))
        hasil_Vo = -1* Av *Vi * np.sin(2 * np.pi * 50 * t)

        hasil_Vo[hasil_Vo > VCC] = VCC
        hasil_Vo[hasil_Vo < -VCC] = -VCC

        if hitung:
            fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))
            ax1.plot(t, hasil_Vi)
            ax1.set_xlabel('Waktu (s)')
            ax1.set_ylabel('Amplitudo (V)')
            ax1.set_title('Sinyal Vi')
            ax1.grid(True)
            ax1.set_xlim(-0.05,0.05)

            ax2.plot(t, hasil_Vo)
            ax2.set_xlabel('Waktu (s)')
            ax2.set_ylabel('Amplitudo (V)')
            ax2.set_title('Sinyal Vo')
            ax2.grid(True)
            ax2.set_xlim(-0.05,0.05)

            plt.tight_layout()
            st.pyplot(fig)

    sinusoidal()

st.write("---")