import numpy as np
from PIL import Image
import svgwrite
import tempfile

def diag(sum_, uv, p1, p2, image, threshold, line_thickness):
    height, width, _ = image.shape
    x1, y1 = int(uv[0] + p1[0]), int(uv[1] + p1[1])
    x2, y2 = int(uv[0] + p2[0]), int(uv[1] + p2[1])

    if x1 < 0 or x1 >= width or y1 < 0 or y1 >= height or x2 < 0 or x2 >= width or y2 < 0 or y2 >= height:
        return sum_

    v1 = image[y1, x1]
    v2 = image[y2, x2]
    if np.linalg.norm(v1 - v2) < threshold:
        dir_ = p2 - p1
        lp = uv - (np.floor(uv) + 0.5)
        dir_ = np.array([-dir_[1], dir_[0]])  # Adjusted rotation direction
        l = np.clip((line_thickness - np.dot(lp, dir_)), 0., 1.)
        sum_ = np.where(l > 0., (1. - l) * sum_ + l * v1, sum_)
    return sum_


# Load the input image
input_image = Image.open('img/wendy.png')
input_data = np.array(input_image)

# Define parameters
LINE_THICKNESS = 0.2
THRESHOLD = 0.5
AA_SCALE = 1.0

# Create a new image for the output
output_data = np.zeros_like(input_data)

# Iterate over the pixels and apply diag function
for i in range(input_data.shape[0]):
    for j in range(input_data.shape[1]):
        uv = np.array([i, j])
        s = input_data[i, j]
        s = diag(s, uv, np.array([-1, 0]), np.array([0, 1]), input_data, THRESHOLD, LINE_THICKNESS)
        s = diag(s, uv, np.array([0, 1]), np.array([1, 0]), input_data, THRESHOLD, LINE_THICKNESS)
        s = diag(s, uv, np.array([1, 0]), np.array([0, -1]), input_data, THRESHOLD, LINE_THICKNESS)
        s = diag(s, uv, np.array([0, -1]), np.array([-1, 0]), input_data, THRESHOLD, LINE_THICKNESS)
        output_data[i, j] = s

# Save the output as a temporary image file
temp_image_path = tempfile.NamedTemporaryFile(suffix=".png").name
output_image = Image.fromarray(output_data.astype(np.uint8))
output_image.save(temp_image_path)

# Create SVG and reference the output image
dwg = svgwrite.Drawing('output.svg', profile='tiny')
dwg.add(dwg.image(temp_image_path, (0, 0), (output_image.width, output_image.height)))
dwg.save()