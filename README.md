# Snake Oil: Pure Structural Extract

> "They call it fake medicine. I call it the only cure for spaghetti code."

## 0x00: Concept
**Snake Oil** is an experimental library that enforces the strict laws of **Category Theory** onto the untyped wilderness of Python.

We hijack the matrix multiplication operator `@` to represent mathematical composition ($g \circ f$), proving that structure can exist even in a chaotic runtime environment.

## 0x01: Usage (The Prescription)
This is not a utility. It is a philosophy.

```python
# The Pythonic way (Procedural Noise):
# y = f(x)
# z = g(y)  <-- State is exposed.

# The Snake Oil way (Structural Purity):
h = g @ f   <-- Pure composition. Logic exists before data.
result = h(x)
