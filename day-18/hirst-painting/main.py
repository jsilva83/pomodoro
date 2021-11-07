import colorgram as col

rgb_colors_in_image = []
colors = col.extract('image.jpg', 30)
for item in colors:
    red = item.rgb.r
    green = item.rgb.g
    blue = item.rgb.b
    rgb_colors_in_image.append((red, green, blue))
print(rgb_colors_in_image)

list_colors = [(224, 156, 75), (30, 105, 150), (14, 53, 90), (163, 17, 43), (228, 209, 96), (170, 92, 30),
               (124, 182, 210), (204, 164, 18), (182, 42, 87), (36, 140, 35), (124, 197, 146), (48, 55, 109),
               (223, 76, 54), (204, 130, 164), (102, 9, 54), (81, 24, 16), (209, 91, 107), (39, 188, 154),
               (147, 213, 172), (1, 82, 120), (143, 207, 223), (83, 72, 39), (229, 181, 157), (95, 101, 166),
               (226, 171, 184), (36, 160, 173)]
