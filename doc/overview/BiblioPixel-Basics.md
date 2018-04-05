# BiblioPixel Basics

## BiblioPixel in one sentence

A Python command line program named `bp` runs a JSON document called a Project
which contains information about your lighting hardware, how your lights are
laid out, and how you want to animate them.

Details follow!

## JSON

JSON is a simple and very popular way to represent structured data as text.

[Here's](https://www.digitalocean.com/community/tutorials/an-introduction-to-json)
a nice little introduction to JSON, and [here's](https://json.org) the full
specification of the fromat, which isn't very long at all.

## The command line

BiblioPixel does not have a graphical user interface - it is a command line
program where you type commands at the terminal.

On Linux or MacOS, you need to run a program called Terminal comes with the
computer.  On Windows, it's [TBD].

In the documentation, terminal commands will be shown like this:

``````
$ bp color
red: (255, 0, 0)
``````

Everything after a ``$`` means something you type in.   In the above example,
you typed `bp color` and the program responded `red: (255, 0, 0)`.


## The `bp` program

The `bp` program's full name is "the BiblioPixel Project runner".  It is
automatically installed when you install `BiblioPixel`.

Try it now!  Type:

``````
$ bp demo
``````

This runs a demonstration BiblioPixel animation and pops up a web page with a
visualization of that animation.

But wait - this seems to run forever!  How do you stop that program you just
started?

## Control C

While animations can have a specific, limited length, a lot of them go on
indefinitely long.  How can you interrupt `bp` in the middle of running an
animation?

The answer is "control-C".  This keystroke interrupts almost any command line
program, not just `BiblioPixel`.

To send a control-C, hold down the Control key on your keyboard (often marked
CTL) and press the C key  a few times until the program stops running.
