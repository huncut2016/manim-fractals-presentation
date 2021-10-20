from manim import *
from collections.abc import Callable
from typing import Union
import numpy as np
from rich.console import group

class ComplexDot (Dot):
    def __init__(self, z = 0+0j, c = 0+0j, **kwargs):
        self.c = c
        self.z = z
        super().__init__(self, **kwargs)

class Mandelbrot(Scene):
    def label_pos (self,
    tracker: Union[ValueTracker, ComplexValueTracker],
    labeled: Mobject, 
    pos: np.ndarray = UP,
    buff: float = 0.1) -> Callable:
            def label_updater (m: DecimalNumber):
                m.next_to(labeled, pos, buff)
                m.set_value(tracker.get_value())

            return label_updater
# --------------------------------------

    def real(self):
        line = NumberLine(
            x_range=[-5, 5, 1],
            length=10,
            color=WHITE,
            include_numbers=False,
            label_direction=UP,            
            # include_tip=True,
        ).center()

        dotTracker = ValueTracker(0)

            
        dot1 = Dot(line.n2p(0), color=RED) \
            .add_updater(lambda m: m.move_to(line.n2p(dotTracker.get_value())))
        
        label1 = DecimalNumber(0 ,
            show_ellipsis=False,
            num_decimal_places=2,
            include_sign=False,
            font_size=30).add_updater(self.label_pos(tracker = dotTracker, labeled = dot1, buff=0.3))
        
        self.play(Create(line))
        self.add(dot1,label1)

        self.play(dotTracker.animate.set_value(3))
        self.wait()
        self.play(dotTracker.animate.set_value(-2))
        self.wait()
        self.play(dotTracker.animate.set_value(0))

        self.wait()
        
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )

    def play_text (self, text: Union[Tex, MathTex, Text, VGroup], big_wait: float = 3):
        self.play(Write(text))
        self.wait(3)
        self.play(FadeOut(text))
        self.wait()

    def imag (self):
        imag1 = MathTex("\\sqrt{-1} \\notin \\mathbb{R}").center()
        self.play_text(imag1)

        text1 = Tex("\\justifying {Mi a megoldás?}").center()
        self.play_text(text1)

        text2 = Tex("\\justifying {Nevezzünk el egy képzetes(imaginárius) számot, amelynek ez lesz az értéke. Hívjuk $i$-nek}").center().scale(0.8)
        self.play_text(text2, big_wait=1)

        text3 = MathTex("\\sqrt{-1} = i")
        self.play_text(text3, big_wait=1)

        text4 = Tex("\\justifying {Bővítsük az eddigi számok halmazát olyan számokkal, amelyek felírhatóak a $a + bi \\hspace{1mm} \\vert \\hspace{2.5mm} a,b \\in \\mathbb{R}; \\hspace{2.5mm} i = \\sqrt{-1}$ formulával}").center().scale(0.8)
        self.play_text(text4)

        text5 = Tex("\justifying {Nevezzük el azt az új halmazt komplex számoknak és legyen a jele $\mathbb{C}$}").center().scale(0.8)
        self.play_text(text5)

    
    def complex_plane (self):
        plane = ComplexPlane().add_coordinates()

        self.play(
            Create(plane)
        )
        self.wait(4)

        axes = plane.get_axes()

        self.play(axes[1].animate.set_color(YELLOW))
        self.play(Wiggle(axes[1], scale_value = 3, run_time=3))#, FadeToColor(axes[1], YELLOW))
        self.play(FadeToColor(axes[1], WHITE))

        complex_tracker = ComplexValueTracker(0 + 0j)    
        
        dot1 = Dot(plane.n2p(0 + 0j), color=YELLOW).add_updater(lambda m: m.move_to(plane.n2p(complex_tracker.get_value())))
        label1 = DecimalNumber(0 + 0j, 
            show_ellipsis=False,
            num_decimal_places=2,
            include_sign=False,
            font_size=30 ).add_updater(self.label_pos(tracker=complex_tracker, labeled=dot1))

        self.add(complex_tracker, dot1, label1)
        self.play(complex_tracker.animate.set_value(1 + 1j))
        self.wait()

        self.play(complex_tracker.animate.set_value(-1 + -1j))
        self.wait()
        
        self.play(complex_tracker.animate.set_value(0 + 0j))
        self.wait()

        self.play(complex_tracker.animate.set_value(-1 + 1j))
        self.wait()

        self.play(complex_tracker.animate.set_value(1 + 0j))
        self.wait()

        label1.clear_updaters()
        dot1.clear_updaters()

        def label_updater (m: DecimalNumber):
            m.move_to(dot1, UP)
            m.set_value(plane.p2n(dot1.get_center()))

        label1.add_updater(label_updater)

        cir = Circle().set_color(ORANGE)
        
        self.play(
            Create(cir),
            MoveAlongPath(dot1, cir),
            rate_func = linear,
            run_time = 5
        )

        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
    
    def mandelbrot (self):
        text1 = Tex("\\justifying {$z_0 = 0 \\\\ z_{n+1} = {z_n}^{2} + c$}")
        text2 = Tex("\\justifying {${\\displaystyle MandelbrotSet=\\left\\{c\\in \\mathbb {C} \\ \\mid \\ z_{n}\\not \\rightarrow \\infty \\right\\}}$}") 
        
        self.play_text(VGroup(text1, text2).arrange(DOWN))
        
        
        plane = ComplexPlane(
            x_range = [-2, 1, 0.25], 
            y_range = [-1, 1, 0.25],
            x_length= round(config.frame_width)-1,
            y_length = round(config.frame_height)-1).add_coordinates()

        self.play(Create(plane))
        self.wait()

        c = -0.2 + 0.4j
        c_var = Variable(c, Tex("c"), tracker=ComplexValueTracker).to_corner(UL).shift(DOWN)
        c_tracker = c_var.tracker

        z = 0+0j
        z_var = Variable(z, Tex("z"), tracker=ComplexValueTracker).to_corner(UL)
        z_tracker = z_var.tracker

        dot1 = Dot(plane.n2p(c), color=YELLOW) \
            .add_updater(lambda m: m.move_to(plane.n2p(z_tracker.get_value())))

        tracer = TracedPath(dot1.get_center)
    
        self.add(z_var, c_var, dot1, tracer)

        max_iter = 10

        for _ in range(max_iter):
            z = z**2 + c
            self.play(z_tracker.animate.set_value(z))

        self.remove(tracer)
        dot1.move_to(plane.n2p(-0.2 + 0.4j))

        self.play(FadeOut(z_var), c_var.animate.shift(UP), FadeOut(dot1))
        self.wait()
        self.play(FadeIn(dot1))

        dot1.clear_updaters()

        self.first = True
        self.prev = Circle()

        def dot_updater (m):
            m.move_to(plane.n2p(c_tracker.get_value()))
            self.remove(self.prev)
            # print(self.static_mobjects)

            z = 0 + 0j
            c = c_tracker.get_value()

            temp_dot = Dot(plane.n2p(c))
            temp_tracer = TracedPath(temp_dot.get_center)
            temp_tracer.update_path(temp_dot, 0)

            for _ in range(20):
                if abs(z) > 7: break 
                z = z**2 + c

                temp_dot.move_to(plane.n2p(z))
                temp_tracer.update_path(temp_dot, 0)

            self.add(temp_tracer)
            self.prev = temp_tracer

        dot1.add_updater(dot_updater)
        self.play(c_tracker.animate(run_time=5, rate_function = linear).set_value(-0.2 + 1j))
        self.wait()
        self.play(c_tracker.animate(run_time=5, rate_function = linear).set_value(-0.2 + -1j))
        self.wait()
        self.play(c_tracker.animate(run_time=5, rate_function = linear).set_value(0.5 + 0.5j))
        self.wait()
        self.play(c_tracker.animate(run_time=5, rate_function = linear).set_value(0.0 + 0.0j))
        self.wait()
        self.clear()
        self.wait()

    def mandelbrotGrid (self):
        plane = ComplexPlane(
            x_range = [-2, 1, 0.25], 
            y_range = [-1, 1, 0.25],
            x_length= round(config.frame_width)-1,
            y_length = round(config.frame_height)-1).add_coordinates()

        self.add(plane)

        dotsGroup = VGroup()

        for x in np.arange(-2, 1, 0.05):
            for y in np.arange(-1, 1, 0.05):
                d = Dot(plane.n2p(complex(x, y)), DEFAULT_DOT_RADIUS / 1.5,)
                d.c = complex(x, y)
                d.z = 0+0j
                dotsGroup.add(d)



        self.play(FadeIn(dotsGroup))

        for _ in range(20):
            animations = []
            
            for m in dotsGroup:
                if abs(m.z) > 6:
                    dotsGroup.remove(m)
                    self.remove(m)
                else:
                    m.z = m.z ** 2 + m.c 
                
                anim = m.animate.move_to(plane.n2p(m.z))
                animations.append(anim)
            self.play(*animations)
            self.wait()

        endG = VGroup()

        for m in dotsGroup:
            newM = m.copy().move_to(plane.n2p(m.c))
            endG.add(newM)

        self.play(Transform(dotsGroup, endG))

        self.wait(5)

    def what_is_complex(self):
        self.real()
        self.imag()
        self.complex_plane()
        self.mandelbrot()
        self.mandelbrotGrid()

    def construct(self):
        self.what_is_complex()