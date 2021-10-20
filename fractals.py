from manim import *
from sponge import Menger_sponge

class Fractals (Menger_sponge, Scene):
    def setup(self):
        Menger_sponge.setup(self)

    def construct(self):
        self.sierpiński_triangle()
        self.mandelbrot_set()
        self.hun()
        self.sponge()

    def sponge (self):
        title = "Menger szivacs"
        title = Title(title)

        self.play(FadeIn(title))
        self.wait()
        self.play(FadeOut(title))

        Menger_sponge.construct(self)

    def hun (self):
        hun = SVGMobject("hun.svg").set_color(WHITE).scale(1.7)
        title = "Magyarország"
        title = Title(title)

        self.play(FadeIn(title), FadeIn(hun))
        self.wait(5)
        self.play(FadeOut(title), FadeOut(hun))

    
    def mandelbrot_set(self):
        img = ImageMobject("./media/images/mandel.png").shift(DOWN*0.7)
        title = "Mandelbrot halmaz"
        title = Title(title)

        self.play(FadeIn(title), FadeIn(img))
        self.wait(5)
        self.play(FadeOut(title), FadeOut(img))

    def sierpiński_triangle (self) :
        sier = SVGMobject("./sher.svg").set_color(WHITE).scale(2)

        title = "Sierpiński háromszög"
        title = Title(title)
        
        self.play(FadeIn(title), FadeIn(sier))        
        self.wait(5)
        self.play(FadeOut(title), FadeOut(sier))