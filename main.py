# Script for calculation amplitude of the input signal after crossing and refraction from printed
# 3D object. The layers of object have different thickness, refractive index and spaces between the layers.
# The script does not assume multiple reflections between layers with different refractive indices.

import numpy as np
import matplotlib.pyplot as plt

layers_number = int(input('How many layers would you have, please enter the value from 2 to 7? '))
wavelength = float(input('What is wavelength in nm for simulation, please enter the value from 300nm to 1600nm? '))
print('Amplitude of the input signal is default and set to 1.')
Iin = 1
n = []  # refractive index
l = []  # layer thickness
Iout0 = 0
Iout1 = 0
Iout2 = 0
c = 3 * 10 ** 8  # light speed

t = float(input('What is the period of observation in femtosenconds, please enter the value from 5 to 20? '))

print('Printed structures are periodic, there will be needed only 2 dimensions to simulate flat printed structure')
n_fill = (float(input(f'Refractive index of material layer: ')))
n_space = (float(input(f'Refractive index of surrounding space: ')))

for layer in range(0, layers_number):
    match layer % 2:
        case 0:
            n.append(float(n_space))
        case 1:
            n.append(float(n_fill))
    if n[layer] == 0:  # not valid value of refractive index
        n.pop()  # Remove and return an element from the right side of the queue
        n.append(float(input(f'Refractive index cannot be equal to 0, put another value for {layer + 1} layer: ')))

# print(n)  # test

print('Printed structures are periodic, there will be needed only 2 dimensions to simulate flat printed structure')
thickness = (float(input(f'Thickness of printed layers in mm: ')))
spacing = (float(input(f'Spacing between layers in mm: ')))

for layer in range(1, layers_number - 1):
    match layer % 2:
        case 1:
            l.append(float(thickness))
        case 0:
            l.append(float(spacing))

match layers_number:
    case 2:
        # calculating parameters
        r01 = (n[0] - n[1]) / (n[0] + n[1])
        Iout0 = Iin * r01
        Amplitude = Iout0
        print(f'Amplitude of output signal is {abs(Amplitude)}')

        # making a plot, old version
        # x = np.linspace(0, t, 600)  # start,stop,points number
        x = np.arange(0, t * (10 ** (-15)), 10 ** (-18))
        yout = Iout0 * np.cos(x * (2 * np.pi) * (c / (n[0] * (wavelength * (10 ** (-9))))))

        plt.figure(figsize=(10, 4))
        plt.plot(x, yout, linewidth=2)
        plt.xlabel('time[s]', fontweight='bold', fontsize=12)
        plt.ylabel('Amplitude of output signal', fontweight='bold', fontsize=12)
        plt.title('Output refraction signal', fontweight='bold', fontsize=12)
        plt.show()

    case 3:
        # calculating parameters
        r01 = (n[0] - n[1]) / (n[0] + n[1])
        Iout0 = Iin * r01
        t01 = (2 * n[0]) / (n[0] + n[1])
        r12 = (n[1] - n[2]) / (n[1] + n[2])
        t10 = (2 * n[1]) / (n[1] + n[0])
        Iout1 = Iin * t01 * r12 * t10
        Amplitude = Iout0 + Iout1
        print(f'Amplitude of output signal is {abs(Amplitude)}')

        # making a plot

        x = np.arange(0, t * (10 ** (-15)), 10 ** (-18))  # start,stop,points number
        y1 = Iout0 * np.cos(x * (2 * np.pi * (c / (n[0] * (wavelength * (10 ** (-9)))))))
        y2 = Iout1 * np.cos(x * (2 * np.pi * (c / (n[0] * (wavelength * (10 ** (-9)))))) - (
                4 * np.pi * (n[1] * l[0] / (wavelength * (10 ** (-9))))))
        yout = y1 + y2

        plt.plot(x, yout, linewidth=2)
        plt.xlabel('time[s]', fontweight='bold', fontsize=12)
        plt.ylabel('Amplitude of output signal', fontweight='bold', fontsize=12)
        plt.title('Output refraction signal', fontweight='bold', fontsize=12)
        plt.show()
    case 4:
        # calculating parameters
        r01 = (n[0] - n[1]) / (n[0] + n[1])
        Iout0 = Iin * r01
        t01 = (2 * n[0]) / (n[0] + n[1])
        r12 = (n[1] - n[2]) / (n[1] + n[2])
        t10 = (2 * n[1]) / (n[1] + n[0])
        Iout1 = Iin * t01 * r12 * t10
        t12 = (2 * n[1]) / (n[1] + n[2])
        r23 = (n[2] - n[3]) / (n[2] + n[3])
        t21 = (2 * n[2]) / (n[2] + n[1])
        Iout2 = Iin * t01 * t12 * r23 * t21 * t10
        Amplitude = Iout2 + Iout1 + Iout0
        print(f'Amplitude of output signal is {abs(Amplitude)}')

        # making a plot
        x = np.arange(0, t * (10 ** (-15)), 10 ** (-18))  # start,stop,points number
        y1 = Iout0 * np.cos(x * (2 * np.pi * (c / (n[0] * (wavelength * (10 ** (-9)))))))
        y2 = Iout1 * np.cos(x * (2 * np.pi * (c / (n[0] * (wavelength * (10 ** (-9)))))) - (
                4 * np.pi * (n[1] * l[0] / (wavelength * (10 ** (-9))))))
        y3 = Iout2 * np.cos(x * (2 * np.pi * (c / (n[0] * (wavelength * (10 ** (-9)))))) - (
                4 * np.pi * (n[1]*l[0]/(wavelength * (10 ** (-9))))) - (
                4 * np.pi * (n[2]*l[1]/(wavelength * (10 ** (-9))))))
        yout = y1 + y2 + y3

        plt.plot(x, yout, linewidth=2)
        plt.xlabel('time[s]', fontweight='bold', fontsize=12)
        plt.ylabel('Amplitude of output signal', fontweight='bold', fontsize=12)
        plt.title('Output refraction signal', fontweight='bold', fontsize=12)
        plt.show()
    case 5:
        r01 = (n[0] - n[1]) / (n[0] + n[1])
        Iout0 = Iin * r01
        t01 = (2 * n[0]) / (n[0] + n[1])
        r12 = (n[1] - n[2]) / (n[1] + n[2])
        t10 = (2 * n[1]) / (n[1] + n[0])
        Iout1 = Iin * t01 * r12 * t10
        t12 = (2 * n[1]) / (n[1] + n[2])
        r23 = (n[2] - n[3]) / (n[2] + n[3])
        t21 = (2 * n[2]) / (n[2] + n[1])
        Iout2 = Iin * t01 * t12 * r23 * t21 * t10
        t23 = (2 * n[2]) / (n[2] + n[3])
        r34 = (n[3] - n[4]) / (n[3] + n[4])
        t32 = (2 * n[3]) / (n[3] + n[2])
        Iout3 = Iin * t01 * t12 * t23 * r34 * t32 * t21 * t10
        Amplitude = Iout3 + Iout2 + Iout1 + Iout0
        print(f'Amplitude of output signal is {abs(Amplitude)}')

        # making a plot
        x = np.arange(0, t * (10 ** (-15)), 10 ** (-18))  # start,stop,points number
        y1 = Iout0 * np.cos(x * (2 * np.pi * (c / (n[0] * (wavelength * (10 ** (-9)))))))
        y2 = Iout1 * np.cos(x * (2 * np.pi * (c / (n[0] * (wavelength * (10 ** (-9)))))) - (
                4 * np.pi * (n[1] * l[0] / (wavelength * (10 ** (-9))))))
        y3 = Iout2 * np.cos(x * (2 * np.pi * (c / (n[0] * (wavelength * (10 ** (-9)))))) - (
                4 * np.pi * (n[1] * l[0] / (wavelength * (10 ** (-9))))) - (
                4 * np.pi * (n[2] * l[1] / (wavelength * (10 ** (-9))))))
        y4 = Iout3 * np.cos(x * (2 * np.pi * (c / (n[0] * (wavelength * (10 ** (-9)))))) - (
                4 * np.pi * (n[1] * l[0] / (wavelength * (10 ** (-9))))) - (
                4 * np.pi * (n[2] * l[1] / (wavelength * (10 ** (-9))))) - (
                4 * np.pi * (n[3] * l[2] / (wavelength * (10 ** (-9))))))
        yout = y1 + y2 + y3 + y4

        plt.plot(x, yout, linewidth=2)
        plt.xlabel('time[s]', fontweight='bold', fontsize=12)
        plt.ylabel('Amplitude of output signal', fontweight='bold', fontsize=12)
        plt.title('Output refraction signal', fontweight='bold', fontsize=12)
        plt.show()

    case 6:
        r01 = (n[0] - n[1]) / (n[0] + n[1])
        Iout0 = Iin * r01
        t01 = (2 * n[0]) / (n[0] + n[1])
        r12 = (n[1] - n[2]) / (n[1] + n[2])
        t10 = (2 * n[1]) / (n[1] + n[0])
        Iout1 = Iin * t01 * r12 * t10
        t12 = (2 * n[1]) / (n[1] + n[2])
        r23 = (n[2] - n[3]) / (n[2] + n[3])
        t21 = (2 * n[2]) / (n[2] + n[1])
        Iout2 = Iin * t01 * t12 * r23 * t21 * t10
        t23 = (2 * n[2]) / (n[2] + n[3])
        r34 = (n[3] - n[4]) / (n[3] + n[4])
        t32 = (2 * n[3]) / (n[3] + n[2])
        Iout3 = Iin * t01 * t12 * t23 * r34 * t32 * t21 * t10
        t34 = (2 * n[3]) / (n[3] + n[4])
        r45 = (n[4] - n[5]) / (n[4] + n[5])
        t43 = (2 * n[4]) / (n[4] + n[4])
        Iout4 = Iin * t01 * t12 * t23 * t34 * r45 * t43 * t32 * t21 * t10
        Amplitude = Iout4 + Iout3 + Iout2 + Iout1 + Iout0
        print(f'Amplitude of output signal is {abs(Amplitude)}')

        # making a plot
        x = np.arange(0, t * (10 ** (-15)), 10 ** (-18))  # start,stop,points number
        y1 = Iout0 * np.cos(x * (2 * np.pi * (c / (n[0] * (wavelength * (10 ** (-9)))))))
        y2 = Iout1 * np.cos(x * (2 * np.pi * (c / (n[0] * (wavelength * (10 ** (-9)))))) - (
                4 * np.pi * (n[1] * l[0] / (wavelength * (10 ** (-9))))))
        y3 = Iout2 * np.cos(x * (2 * np.pi * (c / (n[0] * (wavelength * (10 ** (-9)))))) - (
                4 * np.pi * (n[1] * l[0] / (wavelength * (10 ** (-9))))) - (
                4 * np.pi * (n[2] * l[1] / (wavelength * (10 ** (-9))))))
        y4 = Iout3 * np.cos(x * (2 * np.pi * (c / (n[0] * (wavelength * (10 ** (-9)))))) - (
                4 * np.pi * (n[1] * l[0] / (wavelength * (10 ** (-9))))) - (
                4 * np.pi * (n[2] * l[1] / (wavelength * (10 ** (-9))))) - (
                4 * np.pi * (n[3] * l[2] / (wavelength * (10 ** (-9))))))
        y5 = Iout4 * np.cos(x * (2 * np.pi * (c / (n[0] * (wavelength * (10 ** (-9)))))) - (
                4 * np.pi * (n[1] * l[0] / (wavelength * (10 ** (-9))))) - (
                4 * np.pi * (n[2] * l[1] / (wavelength * (10 ** (-9))))) - (
                4 * np.pi * (n[3] * l[2] / (wavelength * (10 ** (-9))))) - (
                4 * np.pi * (n[4] * l[3] / (wavelength * (10 ** (-9))))))
        yout = y1 + y2 + y3 + y4 + y5

        plt.plot(x, yout, linewidth=2)
        plt.xlabel('time[s]', fontweight='bold', fontsize=12)
        plt.ylabel('Amplitude of output signal', fontweight='bold', fontsize=12)
        plt.title('Output refraction signal', fontweight='bold', fontsize=12)
        plt.show()
    case 7:
        r01 = (n[0] - n[1]) / (n[0] + n[1])
        Iout0 = Iin * r01
        t01 = (2 * n[0]) / (n[0] + n[1])
        r12 = (n[1] - n[2]) / (n[1] + n[2])
        t10 = (2 * n[1]) / (n[1] + n[0])
        Iout1 = Iin * t01 * r12 * t10
        t12 = (2 * n[1]) / (n[1] + n[2])
        r23 = (n[2] - n[3]) / (n[2] + n[3])
        t21 = (2 * n[2]) / (n[2] + n[1])
        Iout2 = Iin * t01 * t12 * r23 * t21 * t10
        t23 = (2 * n[2]) / (n[2] + n[3])
        r34 = (n[3] - n[4]) / (n[3] + n[4])
        t32 = (2 * n[3]) / (n[3] + n[2])
        Iout3 = Iin * t01 * t12 * t23 * r34 * t32 * t21 * t10
        t34 = (2 * n[3]) / (n[3] + n[4])
        r45 = (n[4] - n[5]) / (n[4] + n[5])
        t43 = (2 * n[4]) / (n[4] + n[4])
        Iout4 = Iin * t01 * t12 * t23 * t34 * r45 * t43 * t32 * t21 * t10
        t45 = (2 * n[4]) / (n[4] + n[5])
        r56 = (n[5] - n[6]) / (n[5] + n[6])
        t54 = (2 * n[5]) / (n[5] + n[5])
        Iout5 = Iin * t01 * t12 * t23 * t34 * t45 * r56 * t54 * t43 * t32 * t21 * t10
        Amplitude = Iout5 + Iout4 + Iout3 + Iout2 + Iout1 + Iout0
        print(f'Amplitude of output signal is {abs(Amplitude)}')

        # making a plot
        x = np.arange(0, t * (10 ** (-15)), 10 ** (-18))  # start,stop,points number
        y1 = Iout0 * np.cos(x * (2 * np.pi * (c / (n[0] * (wavelength * (10 ** (-9)))))))
        y2 = Iout1 * np.cos(x * (2 * np.pi * (c / (n[0] * (wavelength * (10 ** (-9)))))) - (
                4 * np.pi * (n[1] * l[0] / (wavelength * (10 ** (-9))))))
        y3 = Iout2 * np.cos(x * (2 * np.pi * (c / (n[0] * (wavelength * (10 ** (-9)))))) - (
                4 * np.pi * (n[1] * l[0] / (wavelength * (10 ** (-9))))) - (
                4 * np.pi * (n[2] * l[1] / (wavelength * (10 ** (-9))))))
        y4 = Iout3 * np.cos(x * (2 * np.pi * (c / (n[0] * (wavelength * (10 ** (-9)))))) - (
                4 * np.pi * (n[1] * l[0] / (wavelength * (10 ** (-9))))) - (
                4 * np.pi * (n[2] * l[1] / (wavelength * (10 ** (-9))))) - (
                4 * np.pi * (n[3] * l[2] / (wavelength * (10 ** (-9))))))
        y5 = Iout4 * np.cos(x * (2 * np.pi * (c / (n[0] * (wavelength * (10 ** (-9)))))) - (
                4 * np.pi * (n[1] * l[0] / (wavelength * (10 ** (-9))))) - (
                4 * np.pi * (n[2] * l[1] / (wavelength * (10 ** (-9))))) - (
                4 * np.pi * (n[3] * l[2] / (wavelength * (10 ** (-9))))) - (
                4 * np.pi * (n[4] * l[3] / (wavelength * (10 ** (-9))))))
        y6 = Iout5 * np.cos(x * (2 * np.pi * (c / (n[0] * (wavelength * (10 ** (-9)))))) - (
                4 * np.pi * (n[1] * l[0] / (wavelength * (10 ** (-9))))) - (
                4 * np.pi * (n[2] * l[1] / (wavelength * (10 ** (-9))))) - (
                4 * np.pi * (n[3] * l[2] / (wavelength * (10 ** (-9))))) - (
                4 * np.pi * (n[4] * l[3] / (wavelength* (10 ** (-9))))) - (
                4 * np.pi * (n[5] * l[4] / (wavelength* (10 ** (-9))))))
        yout = y1 + y2 + y3 + y4 + y5 + y6

        overlapping = 0.350
        line1 = plt.plot(x, y1, c='red', alpha=overlapping, lw=5)
        line2 = plt.plot(x, y2, c='green', alpha=overlapping, lw=5)
        line3 = plt.plot(x, y3, c='yellow', alpha=overlapping, lw=5)
        line4 = plt.plot(x, y4, c='blue', alpha=overlapping, lw=5)
        line5 = plt.plot(x, y5, c='purple', alpha=overlapping, lw=5)
        line6 = plt.plot(x, y6, c='cyan', alpha=overlapping, lw=5)
        lineout = plt.plot(x, yout, c='black', alpha=overlapping+0.1, lw=5)
        plt.xlabel('time[s]', fontweight='bold', fontsize=12)
        plt.ylabel('Amplitude of output signal', fontweight='bold', fontsize=12)
        plt.title('Output refraction signal', fontweight='bold', fontsize=12)
        plt.show()

    case default:
        print("Not valid layer number, enter the right number of layers, from 2 to 7")
