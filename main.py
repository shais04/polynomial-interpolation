import numpy as np
import matplotlib.pyplot as plt
# import matplotlib
# matplotlib.use("Agg")

"""
Given the list of coefficients cf, return a polynomial.
Used in the creation of a graph.
"""
def polynomial(cf):
  return lambda x: sum(cf[i] * pow(x, i) for i in range(len(cf)))

"""
Converts a pair in the form x,y to a list [x,y].
Returns whether to continue asking for points or not.
"""
def str_to_point(pair, pt_list): # returns whether to continue asking for points
  if pair == "":
    if len(pt_list) == 0:
      print("You must enter at least one point.")
      return True
    return False
  try:
    loc = pair.find(",")
    x, y = float(pair[:loc]), float(pair[loc+1:])
    if not x in set(pt[0] for pt in pt_list):
      pt_list.append([x, y])
    else:
      print("Points may not share an x-coordinate.")
    return True
  except:
    print("Unable to create a point from your input: "+pair)
    return True

print("Provide points as input in the form x,y.\nYou must provide at least one point.\nAll points must have a unique x-coordinate.\nTo end entry of points, simply leave the field blank.\n")

# for graphing purposes
min_x = np.inf
max_x = -np.inf

# gather points from input
not_done = True
pts = []
while not_done:
  not_done = str_to_point(input("Give a point: "), pts)
  if pts:
    min_x = min(min_x, pts[-1][0])
    max_x = max(max_x, pts[-1][0])

# construct the Vandermonde matrix, then set up the linear system
num_pts = len(pts)
matrix_A_list = []
vector_b_list = []
for pt in pts:
  vector_b_list.append(pt[1])
  for i in range(num_pts):
    matrix_A_list.append(pow(pt[0], i))
A = np.array(matrix_A_list).reshape((num_pts, num_pts))
b = np.array(vector_b_list)
del(matrix_A_list); del(vector_b_list)
# looking for x in Ax = b, x is the arrays coeffs below
            
# find and display the results
coeffs = np.linalg.solve(A, b)
del(A); del(B)
print("\nEquation of the interpolating polynomial (up to 3 decimal places per coefficient):")
print("y = ", end = "")
for i in range(len(coeffs) - 1, 0, -1):
  c = round(coeffs[i], 3)
  if c:
    print("{}x^{}".format(c, i), end = " + ")
print(round(coeffs[0], 3))

# produce a graph
show = input("Answer using \"Y\" or \"N\" for \"yes\" and \"no\", respectively:\nShow a graph of the polynomial with your points? ")
if show.upper() == "Y":
  diff = max_x - min_x
  min_x -= 0.2 * diff
  max_x += 0.2 * diff
  x_vals = np.linspace(min_x, max_x, num = int(np.ceil(diff) * 15))
  inter_poly = polynomial(coeffs)
  y_vals = inter_poly(x_vals)
  in_x, in_y = [pt[0] for pt in pts], [pt[1] for pt in pts]
  plt.plot(x_vals, y_vals)
  plt.plot(in_x, in_y, "o")
  plt.xlabel("x")
  plt.ylabel("y")
  plt.title("Interpolating polynomial")
  # plt.savefig("graph.png")
  plt.show()