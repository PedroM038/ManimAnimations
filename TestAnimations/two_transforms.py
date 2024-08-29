from manim import (
    Circle,
    FadeOut,
    ReplacementTransform,
    Scene,
    Square,
    Transform,
    Triangle,
)


class two_transforms(Scene):
    def transform(self):
        a = Circle()
        b = Square()
        c = Triangle()

        self.play(Transform(a, b))
        self.play(Transform(b, c))
        self.play(FadeOut(a))

    def replacement_transform(self):
        a = Circle()
        b = Square()
        c = Triangle()

        self.play(ReplacementTransform(a, b))
        self.play(ReplacementTransform(b, c))
        self.play(FadeOut(c))

    def construct(self):
        self.replacement_transform()
        self.wait(2)
