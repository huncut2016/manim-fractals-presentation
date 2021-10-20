from manim import *


class Sources (Scene):
    def construct(self):

        good_bye = Tex("Köszönöm a figyelmet!").scale(2)

        self.play(Write(good_bye))
        self.play(Unwrite(good_bye))

        sources = Tex("""\\justifying {https://www.youtube.com/watch?v=gB9n2gHsHN4 \\\\[2.5mm]
            https://www.youtube.com/watch?v=-RdOwhmqP5s \\\\[2.5mm]
            https://www.youtube.com/watch?v=RU0wScIj36o \\\\[2.5mm]
            https://www.youtube.com/watch?v=3s7h2MHQtxc\\&t=574s \\\\[2.5mm]
            https://www.youtube.com/watch?v=LqbZpur38nw\\&t=1315s \\\\[2.5mm]
            https://github.com/Warptron/manimation/blob/main/manimation/hilbert\\_curve.py \\\\[2.5mm]
            https://www.youtube.com/watch?v=p2jeFDjdJ-s \\\\[2.5mm]
            https://www.youtube.com/watch?v=JbN1vRmhox0 \\\\[2.5mm]
            https://www.youtube.com/watch?v=Cnd\\_cVdwkk0 \\\\[2.5mm]
            https://www.youtube.com/watch?v=4V5EIlFTqrk \\\\[2.5mm]
            https://www.youtube.com/watch?v=ovJcsL7vyrk\\&t=763s \\\\[2.5mm]
            https://www.youtube.com/watch?v=qhbuKbxJsk8\\&t=27s \\\\[2.5mm]
            https://www.youtube.com/channel/UCxiWCEdx7aY88bSEUgLOC6A \\\\[2.5mm]
            https://github.com/136108Haumea/my-manim/blob/master/old\\%20projects/Sierpinski.py \\\\[2.5mm]
            https://en.wikipedia.org/wiki/Fractal \\\\[2.5mm]
            https://en.wikipedia.org/wiki/Hausdorff\\_dimension \\\\[2.5mm]
            https://en.wikipedia.org/wiki/Fractal\\_dimension \\\\[2.5mm]
            https://en.wikipedia.org/wiki/Space-filling\\_curve \\\\[2.5mm]
            https://www.manim.community/ \\\\[2.5mm]
            https://en.wikipedia.org/wiki/Lorenz\\_system \\\\[2.5mm]
            https://www.youtube.com/watch?v=9gk\\_8mQuerg \\\\[2.5mm]
            https://www.youtube.com/watch?v=I9EO9-izL9E \\\\[2.5mm]
            https://www.youtube.com/watch?v=QBy-ZMrSQpE \\\\[2.5mm]
            https://www.youtube.com/watch?v=QBy-ZMrSQpE \\\\[2.5mm]
            https://www.youtube.com/watch?v=vfteiiTfE0c\\&t=944s \\\\[2.5mm]
            https://www.youtube.com/watch?v=n7JK4Ht8k8M\\&t=13s \\\\[2.5mm]
            https://www.youtube.com/watch?v=zOUD\\_HtvchE}""")

        sources.scale(0.7).to_edge(UP).shift(UP * (sources.get_top()[1] - sources.get_bottom()[1]))

        self.play(sources.animate(run_time=17, rate_func=linear).to_edge(DOWN).shift(DOWN * (sources.get_top()[1] - sources.get_bottom()[1])))

        self.wait(2)
