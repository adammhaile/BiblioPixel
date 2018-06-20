# Typenames, and the `path` and `alias` sections.

A class section (`animation`, `controls`, `drivers`, or `layout`) has the name
of its Python class in the field `typename`.

**Example 1**:  Simple animation

```
    animation:
      typename: .tests.StripChannelTest
```

For convenience, if the whole class section is a string, it's the `typename`:

**Example 2**:  Same animation as in Example 1

```
    animation: .tests.StripChannelTest
```
