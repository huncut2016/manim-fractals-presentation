from manim import *

class Menger_sponge(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(70 * DEGREES, -45 * DEGREES)
        # self.renderer.camera.light_source.move_to(3*IN))

        self.sponge_size = 4
        self.iteration = 4

        Sponge = ThreeDVMobject()

        Sponge.add(Cube(4, fill_opacity=1, fill_color="#adadad"))
        
        for _ in range(self.iteration-1):
            mark = Sponge.scale(1/3).move_to(UL*self.sponge_size/3+IN*self.sponge_size/3)
            
            self.play(FadeIn(mark), run_time=3, rate_func = smooth)

            pos = [RIGHT,RIGHT,DOWN,DOWN,LEFT,LEFT,UP]
            a = VGroup(mark)
            for i in range(len(pos)):
                a.add(mark.copy().next_to(a[-1],pos[i],buff=0))
            for i in range(5):
                a.add(mark.copy().next_to(a[2*i],OUT,buff=0))
            for i in range(len(pos)):
                a.add(mark.copy().next_to(a[-1],pos[i],buff=0))
            Sponge = a
            self.play(FadeIn(a[1:]),run_time=3)

        self.move_camera(
            phi=90*DEGREES,
            theta=0*DEGREES,
            focal_distance=40,
            rate_func=smooth,
            run_time=3,
            )
        self.move_camera(
            phi=45*DEGREES,
            theta=45*DEGREES,
            focal_distance=30,
            rate_func=smooth,
            run_time=3,
            )
        self.move_camera(
            phi=15*DEGREES,
            theta=60*DEGREES,
            focal_distance=30,
            rate_func=smooth,
            run_time=3,
            )
        self.move_camera(
            phi=30*DEGREES,
            theta=90*DEGREES,
            focal_distance=5,
            rate_func=smooth,
            run_time=3,
            )
        self.wait(3)

        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )

        self.set_camera_orientation(0, -PI / 2)

