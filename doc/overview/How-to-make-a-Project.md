# How to write a BiblioPixel Project

A BiblioPixel project is a document that describes the different parts of a
BiblioPixel Lighting System project in a text form that humans can read,
understand and edit.

## Projects are YAML or JSON

BiblioPixel projects can be written in YAML or in JSON.

In this document, we use YAML for our examples, because JSON is simply more
wordy, but many automated tools write JSON and some people prefer it, so we
support it completely.

## Examples:

Example: a very simple project in YAML

    shape: 50
    animation: BiblioPixelAnimations.strip.Wave

Example: a slightly larger project written in YAML

    shape: [32, 32]

    run:
      fps: 60

    animation:
      typename: BiblioPixelAnimations.matrix.ImageAnim
      imagePath: /Users/tom/Documents/giphy-zoom.gif

Example: the same project in JSON

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

## A project file is divided into class sections and value sections.

In the project files above, there are three sections - `shape`, `run`,
and `animation`.

Project files have a dozen possible sections, but many of these aren't commonly
used.  The most important three sections are `animation`, `shape`, and `driver`
which appear is almost every project.

* `animation` describes how your lights are animated
* `shape` shows how your lights are laid out in 1, 2, or 3 dimensions
* `driver` configures the hardware driver that controls the actual lights

Sections come in two categories - _values_ and _classes_.

_Value sections_ contain simple things like strings, numbers, lists, or
dictionaries.  In the examples above, `shape` and `run` are value sections.

On the other hand, _class sections_ contain actual data types, and you can load
your own code or third party code into a class section.

In the examples above, `animation` is a class section.

A class section is a dictionary (also called a
["map" in YAML](http://yaml.org/spec/1.2/spec.html#id2759963) or
[an "object" in JSON](https://json.org/)).

A dictionary maps _keys_ to _values_ - in
the second example, the class section animation has the keys `typename` and
`imagePath`.

A class section can have a special value with key `typename` which names
an actual Python class to use for that section.  That Python class is given all
the keyed values from the class section to construct an object, which is used by
the project.

For convenience, if a class section is just a string, that string is used as a
`typename`. For example, these two projects mean exactly the same thing:

    animation: BiblioPixelAnimations.matrix.ImageAnim

and

    animation:
      typename: BiblioPixelAnimations.matrix.ImageAnim

## Value sections

* `aliases`
* `numbers`
* `path`
* `run`
* `shape`

## Class sections

* `animation`
* `controls`
* `driver`
* `drivers`
* `layout`
