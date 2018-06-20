# The `animation` section

BiblioPixel comes with a library of animations called BiblioPixelAnimations
which you can reuse without programming.

If you can program, writing animations is quite easy and often the best way to
solve your problem - there are more types of animation than all the other class
types put together.

The `animation` section works together with the `run` section to describe all
timing.

The `animation` section determines how the light colors change over time, while
the `run` section describes more general information - like the frame rate (in
frames per second or fps), or how many times the animation is repeated.


# Each `animation` section is different.

The parameters in the section depend entirely on the type `animation` itself.
Each type of animation has a documentation page - check that for erxamples.

Examples:

1. Display a single animation with no parameters

    animation: BiblioPixelAnimations.matrix.bloom


2. An animation with parameters `scroll`, `color` and `bgcolor`

    animation:
      typename: BiblioPixelAnimations.matrix.Mainframe
      scroll: false
      color: green
      bgcolor: dark gray

Mix four animations together

    animation:

        typename: mixer
        levels: [0.25, 0.25, 0.25, 0.25]
        animations:
            - BiblioPixelAnimations.matrix.ImageAnim
            - BiblioPixelAnimations.matrix.ImageShow
            - BiblioPixelAnimations.matrix.ImageDissolve
            - BiblioPixelAnimations.matrix.ScreenGrab
