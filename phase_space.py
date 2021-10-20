from manim import *

class PhaseSpace (Scene):
    def construct (self):
        texts = VGroup(Tex('\\justifying {A fizikához nagyon sok helyen kapcsolódnak a fraktálok.}'),
            Tex("\\justifying{ Fázistér: Egy olyan szemléltető alakzat, amely egy rendszer minden állapotát képes ábrázolni}"),
            Tex("\\justifying { Káosz: Dinamikus rendszerek, amelyek látszólag véletlen állapotokat vesznek fel, amíg a háttérben determinisztikus törvények szabályozzák a mozgást. Nagyon érzékenyek a kezdeti feltételekre}"),
            Tex("\\justifying {A kaotikus rendszerek fázistere jellemzően fraktál.}")
        )
        
        texts.center().scale(0.8)

        self.play(FadeIn(texts[0]))
        self.wait(5)
        self.play(ReplacementTransform(texts[0], texts[1]))
        self.wait(5)
        self.play(FadeOut(texts[1]), FadeIn(texts[2]))
        self.wait(5)
        self.play(ReplacementTransform(texts[2], texts[3]))
        self.wait(5)
        self.play(FadeOut(texts[3]))