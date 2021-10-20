from manim import *

class Hausdorff(Scene):
    def construct(self):
        hausText = Tex( r""" $\bullet$ Általában fraktáloknál alkalmazandó dimenzió fogalom \\""")
        hausText2 = Tex( "\\justifying {$\\bullet$ Ha a topológiai dimenziótól eltér, az alakzat Haussdorff dimenziója, akkor az alakzat fraktál}")

        huasGoup = VGroup(hausText2, hausText)

        self.play(
            Write(huasGoup.scale(0.75).arrange(DOWN, center=False, aligned_edge=LEFT, buff=0.5).shift(UP), run_time=6),
            )
        self.wait(DEFAULT_WAIT_TIME*4)
        self.play(FadeOut(huasGoup))

        square = Square(1, fill_color=BLUE, fill_opacity=1)
        sideLength = Tex("$1$")
        sideLength2 = Tex("$1$")

        formula1 = Tex("$scale = 1$").move_to(3*LEFT+3*UP)
        self.play(Create(square), Write(formula1))
        self.play(sideLength.animate.move_to(square.get_left() + LEFT / 2), sideLength2.animate.move_to(square.get_top() + UP / 2))
        
        self.wait(2)

        formula2 = Tex("$scale = 2$").move_to(3*LEFT+3*UP)
        self.play(
            square.animate.scale(2).set_color(RED),
            Transform(sideLength, Tex("$2$").move_to(sideLength.get_center() + LEFT / 2)),
            Transform(sideLength2, Tex("$2$").move_to(sideLength2.get_center() + UP / 2)),
            ReplacementTransform(formula1, formula2)
        )
        self.wait(2)

        sq1  = Square(1, color=RED, fill_opacity=1)
        sq2  = Square(1, color=RED, fill_opacity=1)
        sq3  = Square(1, color=RED, fill_opacity=1)
        sq4  = Square(1, color=RED, fill_opacity=1)

        sq1.move_to(square.get_corner(LEFT + UP), aligned_edge=LEFT+UP)
        sq2.move_to(square.get_corner(RIGHT + UP), aligned_edge=RIGHT+UP)
        sq3.move_to(square.get_corner(LEFT + DOWN), aligned_edge=LEFT+DOWN)
        sq4.move_to(square.get_corner(RIGHT + DOWN), aligned_edge=RIGHT+DOWN)

        self.play(
            Create(sq1.set_stroke(WHITE, 3, 1)),
            Create(sq2.set_stroke(WHITE, 3, 1)),
            Create(sq3.set_stroke(WHITE, 3, 1)),
            Create(sq4.set_stroke(WHITE, 3, 1))
        )

        self.play(
            sq1.animate.shift(LEFT+UP).set_color(BLUE).set_stroke(WHITE, 3, 1),
            sq2.animate.shift(RIGHT+UP).set_color(BLUE).set_stroke(WHITE, 3, 1),
            sq3.animate.shift(LEFT+DOWN).set_color(BLUE).set_stroke(WHITE, 3, 1),
            sq4.animate.shift(RIGHT+DOWN).set_color(BLUE).set_stroke(WHITE, 3, 1)
        )

        self.wait(2)

        formula4 = Tex( "$Measure($", # 0
                        "$2$",  # 1
                        "$)$",  # 2
                        "$=$",  # 3
                        "$4$") \
                        .move_to(3*LEFT+2.5*UP)
        # self.add(formula3)

        sqg = VGroup(sq1, sq2, sq3, sq4)

        self.play(
            Write(formula4[:1] + formula4[2])
        )

        self.play(
            ReplacementTransform(formula2.copy(), formula4[1]),
        )

        self.play (
            ReplacementTransform(sqg, formula4[3:])
        )

        self.wait(2)

        self.play(
            Uncreate(VGroup(square, sideLength, sideLength2, formula4, formula2))
        )

        base_formula = Tex( "$scale^{dimension}$",
                            "$= Measure($",
                            "$scale$",
                            "$)$").center()

        self.play(
            Write(base_formula)
        )

        self.wait(2)

        base_formula2 = Tex( "$2^{dimension}$",
                            "$= Measure($",
                            "$2$",
                            "$)$").center()
        self.play(
            ReplacementTransform(base_formula, base_formula2)
        )

        base_formula3 = Tex( "$2^{dimension}$",
                        "$= 4$").center()
        self.wait(2)

        self.play(
            ReplacementTransform(base_formula2, base_formula3)
        )

        base_formula4 = Tex( "$dimension = log_2(4)$").center()

        self.wait(2)
        
        self.play(
            ReplacementTransform(base_formula3, base_formula4)
        )

        self.wait(2)

        base_formula5 = Tex( "$dimension = 2$").center()
        
        self.play(
            ReplacementTransform(base_formula4, base_formula5)
        )

        self.wait(3)

        formula6 = Tex("$log_{scale}(Measure(scale)) = dimension$")

        self.play(
            Unwrite(base_formula5),
            Write(formula6)
        )

        self.wait(5)

        self.play(Unwrite(formula6))
        
        sher = SVGMobject("./sher.svg")
        
        sher_scale = 2

        sher1 = sher.copy().set_color(BLUE)

        begin_scale = Tex("$scale = 1$").shift(UP+LEFT*4.5)
        begin_space = Tex("$Measure(1)$ = ", "$1$").shift(LEFT*4.5)

        self.play(Create(sher1), Write(begin_scale), Write(begin_space[0]))
        self.wait()
        self.play(
            ReplacementTransform(sher1.copy(), begin_space[1])
        )

        self.play(sher1.animate.scale(sher_scale).set_color(RED))
    
        sher2 = sher.copy().set_color(BLUE).scale(sher_scale / 2).move_to(sher1.get_corner(DOWN + LEFT), aligned_edge=DOWN+LEFT)
        sher3 = sher.copy().set_color(BLUE).scale(sher_scale / 2).move_to(sher1.get_corner(DOWN + RIGHT), aligned_edge=DOWN+RIGHT)
        sher4 = sher.copy().set_color(BLUE).scale(sher_scale / 2).move_to(sher1.get_corner(UP), aligned_edge=UP)

        second_scale = Tex("$scale = 2$").shift(UP+LEFT*4.5)
        second_space = Tex("$Measure(2) = $", "$3$").shift(LEFT*4.5)
        
        self.play(FadeIn(sher2),
                  FadeIn(sher3),
                  FadeIn(sher4),
                  sher2.animate.shift(DOWN*1.7+LEFT*1.7),
                  sher3.animate.shift(DOWN*1.7+RIGHT*1.7),
                  sher4.animate.shift(UP*1.7),
                  ReplacementTransform(begin_scale, second_scale),
                  ReplacementTransform(begin_space, second_space[0])
                  )

        self.wait()

        self.play(
            ReplacementTransform(VGroup(sher2, sher3, sher4), second_space[1])
        )

        self.wait()

        formula = Tex( "$log_{scale}($",
                        "$Measure(scale)$",
                        "$) = dimension$").center().shift(UP*3.5)

        self.play (
            Write(formula)
        )
        formula2 = Tex( "$log_{2}($",
                        "3",
                        "$) = dimension$").center().shift(UP*3.5 + DOWN)

        self.play (
            ReplacementTransform(second_scale , formula2[0]),
        )

        self.play (
            ReplacementTransform(second_space , formula2[1]),
            Write(formula2[2])
        )

        self.wait(3)

        self.play (
            Unwrite(formula),
            Uncreate(sher1),
            formula2.animate.center().scale(2)
        )

        self.wait()

        self.play(
            ReplacementTransform(formula2, Tex("$1.58496\\dots \\approx dimension$").center().scale(2))
        )

        self.wait()

        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
