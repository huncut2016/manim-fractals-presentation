from manim import *

class FractalDimension (Scene):
    def construct (self):
        ts = [
            "A fraktáldimenzió egy olyan arányszám, amely megadja, hogy egy minta részletei hogyan változnak a mérési skála függvényében."
        ]

        for text in ts:
            tex = Tex("\\justifying{" + text + "}").scale(0.8)
            self.play(Write(tex))
            self.wait(6)
            self.play(FadeOut(tex))

        dimensions = [
            "Minkowski-dimenzió / doboz dimenzió",
            "Higuchi dimenzió",
            "Lyapunov dimenzió",
            "Hausdorff dimenzió",
            "Assouad dimenzió"
        ]

        g = VGroup()

        for text in dimensions:
            tex = Tex("\\justifying{" + text + "}").scale(0.7)
            g.add(tex)

        g.scale(1.3).arrange(DOWN, center=False, aligned_edge=LEFT).center()

        self.play(Write(g))
        self.wait(6)
        self.play(FadeOut(g - g[-2]), g[-2].animate.scale(2).center())
        
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
