import intersection, qrange
from PIL import Image, ImageDraw

curves = [[[0, 0], [0, 0.5], [0.5, 1], [1, 1]],
          [[0, 0], [0.5, 0], [0.5, 1], [1, 1]],
          [[0, 0], [0.27, 0.17], [0.25, 1], [1, 1]],
          [[0, 0], [0, 0.5], [0.5, 1], [1, 1]],
          [[0, 0], [0.5, 0], [1, 0.5], [1, 1]]
          ]

img = Image.new("RGB", (600, 600), color="black")
pixels = img.load()

color1 = (214, 33, 13)
color2 = (252, 234, 30)

offset = 50

for x in range(600):
    if x < offset:
        t = 0
    elif x > 600 - offset:
        t = 1
    else:
        t = qrange.set_min_max(x, [offset, 600 - offset], [0, 1])
    pointy = intersection.computeIntersections([0, 0.5, 0.5, 1], [0, 0, 1, 1], [t, t], [-5, 5])[0][1]
    for y in range(600):
        pixels[x, y] = (int(color1[0] + (color2[0] - color1[0]) * pointy),
                        int(color1[1] + (color2[1] - color1[1]) * pointy),
                        int(color1[2] + (color2[2] - color1[2]) * pointy),
                        )

img.save("gradient.png")
img.show()