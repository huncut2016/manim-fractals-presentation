# Hilbert Curve
# Inspired by TheCodingTrain:
# Coding in the Cabana 3: Hilbert Curve: https://youtu.be/dSK-MW-zuAc

# With some changes and debugging
# https://github.com/Warptron/manimation/blob/main/manimation/hilbert_curve.py
from manim import *


class HilbertCurve(VMobject):
    def __init__(self, order = 1, **kwargs):
        self.order = order
        super().__init__(**kwargs)

        if self.order == 1:
            path_points = [UL, DL, DR, UR]
        else:
            curves = VGroup()
            for i in range(4):
                order = self.order - 1
                curve = HilbertCurve(order=order)

                if i == 0:
                    curve.rotate(PI / 2)
                    curve.flip(axis=RIGHT)
                elif i == 1:
                    curve.rotate(-PI / 2)
                    curve.flip(axis=LEFT)
                curves.add(curve)
            curves.arrange_in_grid(buff=1)

            # Rearrange curves
            curves = VGroup(curves[0], curves[2], curves[3], curves[1])

            # taking only corner points and the last point from the curves
            path_points = [
                p for curve in curves for i, p in enumerate(curve.points)
                if (i % 3 != 0 or i % (len(curve.points) - 1) == 0)
            ]
        self.set_points_as_corners(path_points)

class HilbertScene (Scene):
    def construct(self):
        curve = HilbertCurve(order=1)
        self.play(Create(curve))

        for i in range(2, 5):
            new_curve = HilbertCurve(order=i).scale(1 / i)
            self.wait(2)
            # self.remove(curve)
            self.play(Transform(curve, new_curve))

        self.wait()
        self.play(FadeOut(curve))

