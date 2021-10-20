from manim import *
from hilbert_curve import HilbertScene

class What_is_a_fractal (HilbertScene, Scene):
    def setup (self):
        HilbertScene.setup(self)
    
    def construct(self):
        title = Tex("Mi az a fraktál? \\").scale(1.5).center()

        self.play(FadeIn(title))
        self.wait()
        self.play(FadeOut(title))

        t1 = [
            '\\justifying {"Önhasonló alakzat, Olyan alakzat, amelyet ha nagyítunk, akkor magát kapjuk vissza, stb."}',
            '\\justifying {Ezzek nem jó deffiníciók, nem praktikusak és némelyik gondokhoz vezethet}',
            '\\justifying {Nincsen általánosan elfogadott deffiníció}',
            '\\justifying {Legtöbb helyen elfogadott: Olyan alakzat, amelynek a fraktál dimenziója eltér a topológiai dimenziójától}',
            '\\justifying {Mi ezzel a probléma?}',
            '\\justifying {A térkitöltő görbékre ez nem igaz, ilyen például a Hilbert görgbe}'
        ]

        for text in t1:
            tex = Tex(text).scale(0.8)
            self.play(FadeIn(tex))
            self.wait(5)
            self.play(FadeOut(tex))

        HilbertScene.construct(self)