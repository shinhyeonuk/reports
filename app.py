import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from scipy import signal

def calculate_response():
    # 전달함수의 분자와 분모 계수 설정
    numerator = [100]
    denominator = [1, 5, 6]

    # 폐루프 전달함수 계산
    sys = signal.TransferFunction(numerator, denominator)

    # 시뮬레이션 설정
    t, y = signal.step(sys)

    # 주파수 응답 계산
    w, mag, phase = signal.bode(sys)

    return t, y, w, mag, phase

def plot_step_response(t, y):
    plt.plot(t, y)
    plt.xlabel('Time')
    plt.ylabel('Output')
    plt.grid(True)
    return plt

def plot_bode_magnitude(w, mag):
    plt.semilogx(w, mag)
    plt.xlabel('Frequency [rad/s]')
    plt.ylabel('Magnitude [dB]')
    plt.grid(True)
    return plt

def plot_bode_phase(w, phase):
    plt.semilogx(w, phase)
    plt.xlabel('Frequency [rad/s]')
    plt.ylabel('Phase [degrees]')
    plt.grid(True)
    return plt

def main():
    st.title("Control System Analysis")

    # 단위 계단 입력의 응답곡선 계산
    t, y, w, mag, phase = calculate_response()

    # 응답곡선 그리기
    st.subheader("Step Response")
    fig_step = plot_step_response(t, y)
    st.pyplot(fig_step)

    # 주파수 응답 그리기
    st.subheader("Bode Plot - Magnitude")
    fig_mag = plot_bode_magnitude(w, mag)
    st.pyplot(fig_mag)

    st.subheader("Bode Plot - Phase")
    fig_phase = plot_bode_phase(w, phase)
    st.pyplot(fig_phase)

if __name__ == "__main__":
    main()