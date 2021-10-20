from manim import *

ts = [
    r"""Hogy néz ki egy fraktál? \\""",
    r"""Mi az a "fraktál dimenzió"? \\""",
    r"""Mi az a Hausdorff dimenzió? \\""",
    r"""Mi az a fraktál? \\""",
    # r"""Milyen fraktálok vannak? \\""",
    # r"""Fraktálok a természetben. \\""",
    r"""Kaotikus rendszerek fázistere és a fraktálok."""
]

class Introw(Scene):
    def construct(self):
        t = Tex(r"""
         Fraktálok fizika előadás \\
               Zoller András
         """)\
        .scale(0.8) \
        .shift(UP)

        self.play(Write(t))
        self.wait()
        self.play(FadeOut(t))

        
        banner = ManimBanner().scale(0.4).center()
        of = ImageMobject("./media/images/of.png", invert=True).move_to(banner.get_center() + DOWN * 2)

        self.play(FadeIn(of), FadeIn(banner))
        self.play(banner.expand())
        self.play(FadeOut(banner), FadeOut(of))

class Topics(Scene):
    def construct(self):

        texs = VGroup()

        for index, text in enumerate(ts):
            t = Tex("\\justifying {" f"${index + 1})$  {text}" + "}")\
                .scale(0.7) \
                .shift(UP * (len(ts) - index))
            texs += t

        self.play(Write(texs.arrange(DOWN, center=False, aligned_edge=LEFT, buff=0.5).shift(LEFT * 4.5 + DOWN * 4), run_time=len(ts)))
        
        self.play(texs[0].animate.scale(2).center(), Unwrite(texs - texs[0]))
        # self.play(texs[0], Unwrite(texs - texs[0]))
        self.wait()

        self.play(FadeOut(texs[0]))
