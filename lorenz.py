from manim import *
import numpy as np

x = 0.01
y = 0
z = 0
sigma = 10
beta = 8 / 3
ro = 28
dt = 0.01

def lorenz (t):
    global x, y, z, dt, sigma, beta, ro

    # print(x,y,z)

    dx = dt*(sigma*(y-x))
    dy = dt*(x*(ro - z) - y)
    dz = dt*(x*y - beta*z)

    x += dx
    y += dy
    z += dz

    return np.array([x*0.1,y*0.1,z*0.1])


class Lorenz_attractor (ThreeDScene):
    def construct(self):
        
        global x,y,z

        axes = ThreeDAxes()
        
        graph = axes.get_parametric_curve(lambda t: lorenz(t), t_range = [-20, 20], use_smoothing = False)
        graph.set_color(BLUE).set_stroke(width=1)
        x = 0.0101
        y = 0
        z = 0

        graph2 = axes.get_parametric_curve(lambda t: lorenz(t), t_range = [-20, 20], use_smoothing = False)
        graph2.set_color(RED).set_stroke(width=1)

        x = 0.01001
        y = 0
        z = 0

        graph3 = axes.get_parametric_curve(lambda t: lorenz(t), t_range = [-20, 20], use_smoothing = False)
        graph3.set_color(WHITE).set_stroke(width=1)

        self.set_camera_orientation(phi=60 * DEGREES, theta=60 * DEGREES,  focal_distance = 300, zoom=0.8)

        # ----
        self.begin_ambient_camera_rotation(rate=0.1)

        self.play(Create(graph), Create(graph2), Create(graph3), run_time = 60, rate_func = linear)
        self.wait(20)

        self.stop_ambient_camera_rotation()


class Lor_eq (Scene):
    def construct (self):
        lorenz_formula_tex = Tex("""
        \\begin{flushleft}
        $\\frac{dx}{dt} = \\sigma (y-x)$
        \\\\[5mm]
        $\\frac{dy}{dt} = x(\\rho - z) - y$
        \\\\[5mm]
        $\\frac{dz}{dt} = xy - \\beta z$
        \\end{flushleft}
        """)

        lorenz_formula_tex2 = Tex("""
        \\begin{flushleft}
        $dx = dt(\\sigma (y-x)$)
        \\\\[5mm]
        $dy = dt(x(\\rho - z) - y)$
        \\\\[5mm]
        $dz = dt(xy - \\beta z)$
        \\end{flushleft}
        """)

        self.play(Write(lorenz_formula_tex), runtime_time=2)

        self.wait()

        self.play(ReplacementTransform(lorenz_formula_tex, lorenz_formula_tex2), runtime_time=2)

        self.wait()

        self.play(FadeOut(lorenz_formula_tex2))

