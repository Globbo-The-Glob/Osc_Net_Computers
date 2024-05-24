from manim import *
import colour as clr


class beast(Scene):
    def construct(self):
        tracker = ValueTracker(0)

        def update_color(obj):
            T = tracker.get_value()
            rgbcolor = [1, 1 - T, 0 + T]
            m_color = rgb_to_color(rgbcolor)
            obj = Circle(color=m_color, radius=0.5)
            

        dot = Circle()
        dot.add_updater(update_color)

        self.add(dot)

        tracker_label = DecimalNumber(
            tracker.get_value(),
            color=WHITE,
            num_decimal_places=8,
            show_ellipsis=True
        )
        tracker_label.add_updater(
            lambda mob: mob.set_value(tracker.get_value())
        )
        self.add(tracker_label)


        self.play(
            tracker.animate.set_value(1),
            run_time=4
        )
        self.wait()