# How to write a BiblioPixel Project

A BiblioPixel project is a text file that describes the different parts of a
BiblioPixel Lighting System project in a form that humans can easily read,
understand and edit.

## Projects are text files written in either [YAML](https://yaml.org) or [JSON](https://json.org)

BiblioPixel projects are data files, written in one of two human-readable
formats, YAML or in JSON.

In this document, we use YAML for most of the examples.

## Examples:

**Example 1:** a very simple project file written in YAML

```
    shape: 50
    animation: BiblioPixelAnimations.strip.Wave
```

**Example 2:** a slightly larger project file, written in JSON

```
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
```

**Example 3:** the same project file, written in YAML

```
    shape: [32, 32]

    run:
      fps: 60

    animation:
      typename: BiblioPixelAnimations.matrix.ImageAnim
      imagePath: /Users/tom/Documents/giphy-zoom.gif
```

## A project file is made up of _sections_, which have _fields_.

In the project files above, there are three sections - `shape`, `run`,
and `animation`.  Sections can have fields - for example, the `run` section
above has the field `fps: 60`.

Project files have nine sections, many of them optional.  The most important
sections are `animation`, `shape`, and `driver`, which appear in almost every
project:

* `animation` describes how your lights are animated
* `shape` shows how your lights are laid out in 1, 2, or 3 dimensions
* `driver` configures the hardware driver that controls the actual lights

_Class sections_ are Python objects.  There are four class sections:
`animation`, `controls`, `drivers` and `layout`.

Each class section has a special _typename_ which defines what the Python object
in that section does, and which fields can be set on it.  Typenames let you
load not just BiblioPixel code, but your own code


Nearly all the excitement in BiblioPixel is in the class sections!  BiblioPixel
comes with a large number of predefined Animations, Controls, Drivers and
Layouts, and you can put them together and customize them simply by writing a
Project, without any programming.

More, if you know a little Python you can extend them or modify a copy, or just
write your own from scratch.


_Value sections_ contain simple things like strings, numbers, lists, or
dictionaries.  The five value sections are `aliases`, `numbers`, `path`, `run`,
and `shape`.

# Fields

Each section has a list of _fields_ - values that you can set.

In Example 2 and 3 above, the `run` section has the field `fps` with value
`60` (fps meaning "frames per second"), and the `animation` section has the
field `imagePath` with value `/Users/tom/Documents/giphy-zoom.gif `.

A value section always has the same fields - for example, the `run` section
always has the `fps` field in any project.

Each class section has a special field named `typename` which is the name
of its Python class.

And then each class section has _different_ fields depending on that
typename.

For example, many animations have no fields at all and do exactly one thing.

An example is the animation with the typename `.tests.StripChannelTest`.


**Example 4**:  An animation that runs a simple test on a strip of 10 pixels

```
    shape: 10
    animation:
      typename: .tests.StripChannelTest
```

On the other hand, the `sequence` animation requires a field `animations`,
a list of animations that are played in sequence.  It also has an optional
field `length` which sets the length of each subsequence.

**Example 5**:  This animation runs four animations, each for two seconds, in a
  loop, and displays the result on a 32x32 pixel display.

```
    shape: [32, 32]

    animation:
        typename: .sequence
        length: 2
        animations:
            - BiblioPixelAnimations.matrix.ImageAnim
            - BiblioPixelAnimations.matrix.ImageShow
            - BiblioPixelAnimations.matrix.ImageDissolve
            - BiblioPixelAnimations.matrix.ScreenGrab
```

# A summary of the sections

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
