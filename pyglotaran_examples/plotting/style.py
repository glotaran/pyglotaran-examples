from enum import Enum

import matplotlib.colors as colors
import matplotlib.pyplot as plt
from cycler import cycler


class ColorCode(Enum):
    # Name	#Hex
    black = '#000000'
    red = '#ff0000'
    blue = '#0000ff'
    green = '#00ff00'
    magenta = '#ff00ff'
    cyan = '#00ffff'
    yellow = '#ffff00'
    green4 = '#008b00'
    orange = '#ff8c00'
    brown = '#964b00'
    grey = '#808080'
    violet = '#9400d3'
    turquoise = '#40e0d0'
    maroon = '#800000'
    indigo = '#4b0082'

    @staticmethod
    def hex_to_rgb(hex_string):
        rgb = colors.hex2color(hex_string)
        return tuple([int(255*x) for x in rgb])

    @staticmethod
    def rgb_to_hex(rgb_tuple):
        return colors.rgb2hex([1.0*x/255 for x in rgb_tuple])


class LineStyle(Enum):
    solid = '-'
    dashed = '--'
    dotted = '..'
    dashdot = '-.'


class PlotStyle(object):

    def __init__(self):
        self._line_style = [e.value for e in LineStyle]
        self._color_codes = [e.value for e in ColorCode]
        self.SMALL_SIZE = 12
        self.MEDIUM_SIZE = 14
        self.BIGGER_SIZE = 18

    def set_default_fontsize(self):
        plt.rc('font', size=self.SMALL_SIZE)          # controls default text sizes
        plt.rc('axes', titlesize=self.SMALL_SIZE)     # fontsize of the axes title
        plt.rc('axes', labelsize=self.MEDIUM_SIZE)    # fontsize of the x and y labels
        plt.rc('xtick', labelsize=self.SMALL_SIZE)    # fontsize of the tick labels
        plt.rc('ytick', labelsize=self.SMALL_SIZE)    # fontsize of the tick labels
        plt.rc('legend', fontsize=self.SMALL_SIZE)    # legend fontsize
        plt.rc('figure', titlesize=self.BIGGER_SIZE)  # fontsize of the figure title

    def set_default_colors(self):
        plt.rc('axes', prop_cycle=self.cycler)

    @property
    def cycler(self):
        return cycler('color', self._color_codes)

    @property
    def line_cycler(self):
        return cycler('linestyle', self._line_style)
