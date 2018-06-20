# The `run` section

`run` is a value section with nine optional parameters.

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

# Examples

1.  Run forever at 30 frames per second (fps)

    run:
      fps: 30

2.  Run for two seconds at 10 fps

    run:
      seconds: 2
      fps: 10

2.  Run three times

    run:
      max_cycles: 3
