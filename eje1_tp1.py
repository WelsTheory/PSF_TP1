import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


#PARTE 1
def senoidal(frecuencia_muestreo, frecuencia, amplitud, muestras, fase):
    n = np.arange(muestras)
    seno = amplitud * np.sin((2 * np.pi* frecuencia * n /frecuencia_muestreo) + fase)
    return (seno + amplitud)/2

def cuadrada(frecuencia_muestreo,frecuencia,amplitud,muestras):
    def_cuadrado = 0.5
    n = np.arange(muestras)
    cuadra = amplitud * signal.square((2*np.pi * frecuencia * n / frecuencia_muestreo),def_cuadrado)
    return (cuadra + amplitud)/2

def triangular(frecuencia_muestreo, frecuencia, amplitud, muestras):
    def_triang = 0.5
    n = np.arange(muestras)
    trian = amplitud * signal.sawtooth((2 * np.pi * frecuencia * n / frecuencia_muestreo), def_triang)
    return (trian + amplitud)/2


if __name__ == '__main__':
    #PARTE 1
    print("TP1 Parte 1")
    sen = senoidal(100000, 250, 1, 1000, 0)
    plt.title("Ejercicio 1 - Senoidal")
    plt.plot(sen)
    plt.grid()
    plt.show()

    cua = cuadrada(100000, 250, 1, 1000)
    plt.title("Ejercicio 1 - Cuadrada")
    plt.plot(cua)
    plt.grid()
    plt.show()

    tri = triangular(100000, 250, 1, 1000)
    plt.title("Ejercicio 1 - Triangular")
    plt.plot(tri)
    plt.grid()
    plt.show()

    #PARTE 2
    fs = 1000
    N = 1000
    fase = 0
    amp = 1

    #PARTE 2.1
    senal1 = senoidal(fs, 0.1*fs, amp, N, fase)
    senal2 = senoidal(fs, 1.1*fs, amp, N, fase)
    plt.title("Ejercicio 2.1 ")
    plt.plot(senal1, label = '0.1 fs')
    plt.plot(senal2, label = '1.1 fs')
    plt.grid()
    plt.legend()
    plt.show()

    #PARTE 2.2
    senal1 = senoidal(fs, 0.49*fs, amp, N, fase)
    senal2 = senoidal(fs, 1.51*fs, amp, N, fase)
    plt.title("Ejercicio 2.2 ")
    plt.plot(senal1, label = '0.49 fs')
    plt.plot(senal2, label = '1.51 fs')
    plt.grid()
    plt.legend()
    plt.show()