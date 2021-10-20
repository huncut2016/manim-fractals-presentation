from manim import *

from introw import Introw, Topics
from fractals import Fractals
from hausdorff import Hausdorff
from w_i_a_f import What_is_a_fractal
from fractal_dimension import FractalDimension
from lorenz import Lor_eq, Lorenz_attractor
from cellaut import CelluralAutomata
 
class Compile(CelluralAutomata, Introw, Topics, Fractals, Hausdorff, What_is_a_fractal, FractalDimension, Lor_eq, Lorenz_attractor):
    def setup(self):
        Introw.setup(self)
        Topics.setup(self)
        Fractals.setup(self)
        Lor_eq.setup(self)
        Lorenz_attractor.setup(self)
        Hausdorff.setup(self)
        What_is_a_fractal.setup(self)
        FractalDimension.setup(self)
        CelluralAutomata.setup(self)

    def construct(self):
        Introw.construct(self)
        self.wait(3)

        Topics.construct(self)
        self.wait(3)

        Fractals.construct(self)
        self.wait(3)
        
        FractalDimension.construct(self)
        self.wait(3)

        Hausdorff.construct(self)
        self.wait(3)

        What_is_a_fractal.construct(self)
        self.wait(3)

        CelluralAutomata.construct(self)
        self.wait(3)

        Lor_eq.construct(self)
        self.wait(3)

        Lorenz_attractor.construct(self)
        self.wait(3)

