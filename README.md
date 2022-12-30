# polynomial-interpolation
Finds the interpolating polynomial of least degree that goes through a set of points given as input. An example usage with the points `(1, 1)`, `(2, 3)`, and `(3, 6)` given as input yields the following:

```
Provide points as input in the form x,y.
You must provide at least one point.
All points must have a unique x-coordinate.
To end entry of points, simply leave the field blank.

Give a point: 1, 1
Give a point: 2, 3
Give a point: 3, 6
Give a point: 

Equation of the interpolating polynomial (up to 3 decimal places per coefficient):
y = 0.5x^2 + 0.5x^1 + 0.0
Answer using "Y" or "N" for "yes" and "no", respectively:
Show a graph of the polynomial with your points? n
```

This is done using the Vandermonde matrix, solving the matrix equation
```math
\begin{bmatrix}
1 & \cdots & x_1^{n-1} \\
\vdots & \ddots & \vdots \\
1 & \cdots & x_n^{n-1}
\end{bmatrix}\begin{bmatrix}
c_0 \\ \vdots \\ c_{n-1}
\end{bmatrix} = \begin{bmatrix}
y_1 \\ \vdots \\ y_n
\end{bmatrix}
```
to fit the polynomial $c_{n-1}x^{n-1} + \ldots + c_0$ to a set of $n$ points.
