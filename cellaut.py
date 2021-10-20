from manim import *
import numpy as np

class CelluralAutomata (Scene):
    def construct(self):
        self.animate()
        self.play_video()

    def play_video(self):
        t = Title("Szabály 18")
        self.play(FadeIn(t))

        self.wait(35)

        self.play(FadeOut(t))

    def animate(self):
        possibleCells = []

        for i in range(8):
            possibleCells.append([i & 0b001 == 0, i & 0b010 == 0, i & 0b100 == 0])
        
        groups = VGroup()
        numbers = VGroup()
        values = VGroup()

        for index, cells in enumerate(possibleCells):
            g = VGroup()

            for cindex, cell in enumerate(cells):
                sq = Square(1).align_on_border(UP)
                pos = cindex * np.array([sq.width, 0, 0]) + index * DOWN + DOWN

                if cindex == 0:
                    t = Tex(f"$2^{index}$") 
                    t.shift(pos + LEFT*3)
                    numbers.add(t)

                if cindex == 2:
                    val = Square(1).align_on_border(UP)
                    val.shift(pos + RIGHT*2) \
                        .set_stroke(YELLOW, 2, 1)
                    
                    values.add(val)
                
                
                sq.set_stroke(RED, 2, 1) \
                    .shift(pos)

                if (cell):
                    sq.set_fill(WHITE, 1)
                else:
                   sq.set_fill(BLACK, 1)
                g.add(sq)
            
            groups.add(g)
        
        groups.scale(0.7) \
            .center() \
            .shift(LEFT)

        values.scale(0.7) \
            .center() \
            .shift(RIGHT * 3)

        numbers.scale(0.7) \
            .move_to(groups.get_center()) \
            .shift(LEFT*1.5)
        

        counter = 0
        counter_tex = Tex("szabály =", f"{counter}").to_corner(UR)

        self.play(
                Create(groups),
                Create(values),
                Write(numbers),
                Write(counter_tex)
                )


        for i in range(len(values)):
            if np.random.rand() > .5:
                
                sqanim = values[i].animate.set_fill(BLUE, 1)
                rect = SurroundingRectangle(numbers[i])
                counter += 2 ** i
                new_tex = Tex("szabály =", f"{counter}").to_corner(UR)

                self.play(
                    sqanim,
                    Create(rect),
                )

                self.play (
                    FadeIn(new_tex[0]),
                    ReplacementTransform(VGroup(numbers[i].copy(), counter_tex), new_tex[1]),
                    run_time = 3
                )
                counter_tex = new_tex

                self.play(Uncreate(rect))

        self.wait(5)

        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
