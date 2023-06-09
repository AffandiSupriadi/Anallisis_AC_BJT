import streamlit as st
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt

st.title("VOLTAGE-DIVIDER BIAS")
st.write("---")
st.header("Mencari Zi, Zo dan Av")
st.image("rang2.png",width=400)
R1 = st.number_input("Masukkan nilai R1 (Ω) = ")
R2 = st.number_input("Masukkan nilai R2 (Ω) = ")
RC = st.number_input("Masukkan nilai RC (Ω) = ")
RE = st.number_input("Masukkan nilai RE (Ω) = ")
VCC = st.number_input("Masukkan nilai VCC (volt) = ")
VBE = st.number_input("Masukkan nilai VBE (volt) = ")
β = st.number_input("Masukkan nilai β = ")
Vi = st.number_input("Masukkan nilai Vi (volt)=")

option = st.selectbox("Pilih nilai ro", ["Tidak Terhingga", "Terhingga"])

if option == "Tidak Terhingga":
    hitung = st.button("Hitung")

    testβRE= β*RE
    test10R2= 10*R2

    if hitung:
        if testβRE > test10R2:
            VB = R2/(R1+R2)*VCC
            VE = VB-VBE
            IE = VE/RE
            re = 0.026 / IE
            X = β * re
            RB = (R1*R2)/(R1+R2)
            Zi = "{:.2e}".format((RB * X)/(RB + X))
            Zi = Zi.replace("e+03"," k")
            st.write("Nilai Zi =",Zi,"Ω")
            Zo = "{:.2e}".format(RC)
            Zo = Zo.replace("e+03"," k")
            st.write("Nilai Zo =",Zo ,"Ω")
            Av = round(-RC/re,0)
            st.write("Nilai Av =",Av)
        elif testβRE < test10R2:
            st.write("βRE < 10R2")
        
        def sinusoidal():
            t = np.linspace(-0.05, 0.05, 1000)
            phase_shift = 180  # Phase shift in degrees
            
            # Calculate the sinusoidal signals
            hasil_Vi = Vi * np.sin(2 * np.pi * 50 * t + np.deg2rad(phase_shift))
            hasil_Vo = -1* Av *Vi * np.sin(2 * np.pi * 50 * t )

            hasil_Vo[hasil_Vo > VCC] = VCC
            hasil_Vo[hasil_Vo < -VCC] = -VCC

            if hitung:
                fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))
                ax1.plot(t, hasil_Vi)
                ax1.set_xlabel('Waktu (s)')
                ax1.set_ylabel('Amplitudo (V)')
                ax1.set_title('Sinyal Vi')
                ax1.grid(True)
                ax1.set_xlim(-0.05, 0.05)

                ax2.plot(t, hasil_Vo)
                ax2.set_xlabel('Waktu (s)')
                ax2.set_ylabel('Amplitudo (V)')
                ax2.set_title('Sinyal Vo')
                ax2.grid(True)
                ax2.set_xlim(-0.05, 0.05)

                plt.tight_layout()
                st.pyplot(fig)

        sinusoidal()


elif option == "Terhingga":
    ro = st.number_input("Masukkan nilai ro (Ω) = ")
    hitung = st.button("Hitung")

    testβRE= β*RE
    test10R2= 10*R2

    if hitung:
        if testβRE > test10R2:
            VB = R2/(R1+R2)*VCC
            VE = VB-VBE
            IE = VE/RE
            re = 0.026 / IE
            X = β * re
            RB = (R1*R2)/(R1+R2)
            Zi = "{:.2e}".format((RB * X)/(RB + X))
            Zi = Zi.replace("e+03"," k")
            st.write("Nilai Zi =",Zi,"Ω")
            Zo = "{:.2e}".format((ro*RC)/(ro+RC))
            Zo = Zo.replace("e+03"," k")
            st.write("Nilai Zo =",Zo ,"Ω")
            Av = round(-((ro*RC)/(ro+RC))/re, 0)
            st.write("Nilai Av =",Av)
        elif testβRE < test10R2:
            st.write("βRE < 10R2")

        def sinusoidal():
            t = np.linspace(-0.05, 0.05, 1000)
            phase_shift = 180  # Phase shift in degrees
            
            # Calculate the sinusoidal signals
            hasil_Vi = Vi * np.sin(2 * np.pi * 50 * t + np.deg2rad(phase_shift))
            hasil_Vo = -1* Av *Vi * np.sin(2 * np.pi * 50 * t )

            hasil_Vo[hasil_Vo > VCC] = VCC
            hasil_Vo[hasil_Vo < -VCC] = -VCC

            if hitung:
                fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))
                ax1.plot(t, hasil_Vi)
                ax1.set_xlabel('Waktu (s)')
                ax1.set_ylabel('Amplitudo (V)')
                ax1.set_title('Sinyal Vi')
                ax1.grid(True)
                ax1.set_xlim(-0.05, 0.05)

                ax2.plot(t, hasil_Vo)
                ax2.set_xlabel('Waktu (s)')
                ax2.set_ylabel('Amplitudo (V)')
                ax2.set_title('Sinyal Vo')
                ax2.grid(True)
                ax2.set_xlim(-0.05, 0.05)

                plt.tight_layout()
                st.pyplot(fig)

        sinusoidal()



st.write("---")
