# How to write a BiblioPixel Project

A BiblioPixel project is a document that describes the different parts of a
BiblioPixel Lighting System project in a text form that humans can read,
understand and edit.

BiblioPixel projects can be written in YAML or in JSON.  Here are a couple of
examples.

## Example: a project written in YAML

    shape: [32, 32]

    run:
        fps: 60

    animation:
        typename: BiblioPixelAnimations.matrix.ImageAnim
        imagePath: /Users/tom/Documents/giphy-zoom.gif

## Example: the same project in JSON

    shape: [32, 32]

    run:
        fps: 30

    animation:
        typename: BiblioPixelAnimations.matrix.ImageAnim
        imagePath: /Users/tom/Documents/giphy-zoom.gif
