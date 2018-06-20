# The `animation` and the `run` sections

The `animation` and `run` sections work together.

The `animation` section determines how the light colors change over time, while
the `run` section describes more general details - like the frame rate (in
frames per second or fps), or how many times.

BiblioPixel comes with a library of animations called BiblioPixelAnimations
which you can reuse without programming.

If you can program, writing animations is quite easy and often the best way to
solve your problem - there are more types of animation than all the other class
types put together.


# Each `animation` section is different.

The parameters in the section depend entirely on the `animation` itself.

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


# The `run` section

`run` is an optional value section with nine possible parameters.

* `amt` (default `1`): Frame interval - the number of frames between individual
  updates
* `fps` (default `0`): Number of frames per second to display
* `main` (default `None`): If non-empty, then `bp` runs in a background thread,
  and the function named here runs in the foreground
* `max_cycles` (default `0`):  Maximum number of cycles - full repeats of the
  animation - to play back, if set.
* `max_steps` (default `0`): Maximum number of animation steps to play, if set.
* `seconds` (default `None,`): Maximum number of seconds to play, if set.
* `sleep_time` (default `0`): Time to sleep between frames, in seconds.
* `threaded` (default `False`): If True, the animation runs in a separate thread.
* `until_complete` (default `False`): If True, run the animation exactly once.
