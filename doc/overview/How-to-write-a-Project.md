# How to write a BiblioPixel Project

A BiblioPixel project is a document that describes the different parts of a
BiblioPixel Lighting System project in a text form that humans can read,
understand and edit.

## Projects are text files written in either [YAML](https://yaml.org) or [JSON](https://json.org)

BiblioPixel projects are data files, written in one of two human-readable
formats, YAML or in JSON.

In this document, we use YAML for our examples, because JSON is simply more
wordy, but many automated tools write JSON and some people prefer it, so we
support it completely.

## Examples:

**Example:** a very simple project file written in YAML

    shape: 50
    animation: BiblioPixelAnimations.strip.Wave

**Example:** a slightly larger project file, written in JSON

    {
        "shape": [32, 32]

        "run": {
            "fps": 60
        },

        "animation": {
            "typename": "BiblioPixelAnimations.matrix.ImageAnim",
            "imagePath": "/Users/tom/Documents/giphy-zoom.gif"
        }
    }

**Example:** the same project file, written in YAML

    shape: [32, 32]

    run:
      fps: 60

    animation:
      typename: BiblioPixelAnimations.matrix.ImageAnim
      imagePath: /Users/tom/Documents/giphy-zoom.gif

## A project file is made up of _sections_, which have _parameters_.

In the project files above, there are three sections - `shape`, `run`,
and `animation`.  Sections can have parameters - for example, the `run` section
above has the parameter `fps: 60`.

Project files have up to ten sections.  The most important sections are
`animation`, `shape`, and `driver` which appear is almost every project:

* `animation` describes how your lights are animated
* `shape` shows how your lights are laid out in 1, 2, or 3 dimensions
* `driver` configures the hardware driver that controls the actual lights

_Class sections_ are Python objects.  There are exactly four class sections:
`animation`, `controls`, `drivers` and `layout`.  Each section has a _type_
which defines what it does and which parameters can be set on it.

Nearly all the excitement in BiblioPixel is in the class sections. BiblioPixel
comes with a large number of predefined animations, controls, drivers and
layouts, and it's quite easy to write your own.

_Value sections_ contain simple things like strings, numbers, lists, or
dictionaries.  In the examples above, `shape` and `run` are value sections.

Value sections always have the same possible parameters in every project.  For
example, the `run` section can always have the `fps` ("frames per second")
parameter.

But class sections have different parameters based on their type.

For example, many animations have no parameters at all and do exactly one
thing.  An example is `bibliopixel.animation.tests.StripChannelTest`, which can
only be used like this:

    # This animation runs a simple test on a strip of 10 pixels

    shape: 10
    animation: bibliopixel.animation.tests.StripChannelTest


On the other hand, the `sequence` animation requires a parameter `animations`,
a list of animations that are played in sequence.  It also has an optional
parameter `length` which sets the length of each subsequence.

    # This animation runs four animations, each for two seconds, in a loop
    # and displays the result on a 32x32 pixel display.

    shape: [32, 32]

    animation:
        typename: sequence
        length: 2
        animations:
            - BiblioPixelAnimations.matrix.ImageAnim
            - BiblioPixelAnimations.matrix.ImageShow
            - BiblioPixelAnimations.matrix.ImageDissolve
            - BiblioPixelAnimations.matrix.ScreenGrab


A class section has a special parameter named `typename` which is the name of
the Python class for that section. The remaining parameters in the class section
are used to construct the actual object.

For example, in the last example above,

    animation:
      typename: BiblioPixelAnimations.matrix.ImageAnim
      imagePath: /Users/tom/Documents/giphy-zoom.gif

results in running Python code like this:

    project.animation = BiblioPixelAnimations.matrix.ImageAnim(
       imagePath='/Users/tom/Documents/giphy-zoom.gif')

For convenience, if a class section is just a string, that string is used as a
`typename`. For example, these two projects mean exactly the same thing:

    animation: BiblioPixelAnimations.matrix.ImageAnim

and

    animation:
      typename: BiblioPixelAnimations.matrix.ImageAnim

# The sections

Here's a quick summary of what each section does.  The documents following this
one go into each section in more detail.


## Class sections

* `driver`: The output driver for the hardware or simulator
* `drivers`: Used if there's more than one driver.  If the `drivers` section is
  non-empty, the `driver` section becomes a template for `drivers`.
* `layout`: How the lights are laid out geometrically.
* `animation`: The class that actually animates the lights.
* `controls`: Classes that use external input to control parts of
  the project.

## Value sections

* `aliases`: Aliases are a shorthand to save typing.
* `numbers`: Select between plain old Python lists and faster, more powerful
numpy lists.
* `path`: `path` is added to the `PYTHONPATH` to allow loading of custom
  libraries.
* `run`: `run` controls how the topmost animation is executed - how fast it
  runs, for how lon or for how many times, etc.
* `shape`: The shape of the layout - `length` for strips, `[width, height]` for
matrices and `[x, y, z]` for cubes.
