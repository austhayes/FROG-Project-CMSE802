""" 
Welcome to the FROG package! Here I will display quite a bit of my code utilized throughout my project. 

Imports below:

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import plotly.express as px


"""

For starters we will need to load in the files. The 3 files one should take from the spectrometer in their frequency resolved optical gating (FROG) setup, should consist of a data file (intensities), a wavelengths file, and a time file. Utilizing these, I will load in said files via a function, called loading_files.

"""

def load_files(filename = 'data_1400_afterBS.dat', wave = 'wavelengths_1400_afterBS.dat', time = 'times_1400_afterBS.dat'):
    spec = pd.read_csv(filename, header = None, delimiter =',')

    lam = pd.read_csv(wave, header = None, delimiter =',')

    time = pd.read_csv(time, header = None, delimiter =',')

    return spec, lam, time


"""

Heat map plot 

"""

def heat_map(df, x, y, nbinsx, nbinsy, color_continuous_scale, title_text):
    fig = px.density_heatmap(df, x="Wavelength", y="Intensity", nbinsx=15, nbinsy=20, color_continuous_scale="Viridis")
    fig.update_layout(title_text="Intensity vs. Wavelength (nm)")
    fig.show()

"""
Analysis

"""
def Analysis():
    print("This function will output the analysis of the FROG data")
    """
    Mathematically, the first step, Fourier transform to convert data from the frequency domain to the time domain, and vice versa=. This is a critical next step that will be relied on heavily throughout the rest of the project. Other than this, there is a lot of sort of splitting up of the data that needs to be done. The matlab code does a lot of extra work with the data files that I am not positive is really all that necesssary so I have been spending a bit of time trying to figure out what I need, and how to do this in a clear and concise manner to make sure it is easy to understand, as it is currently, not at all. 

    """

    
    

