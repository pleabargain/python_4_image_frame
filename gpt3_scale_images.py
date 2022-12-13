import argparse
from PIL import Image

# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("img1", help="Image file 1")
parser.add_argument("img2", help="Image file 2")
parser.add_argument("img3", help="Image file 3")
parser.add_argument("img4", help="Image file 4")
args = parser.parse_args()

# Open images and get sizes
img1 = Image.open(args.img1)
img2 = Image.open(args.img2)
img3 = Image.open(args.img3)
img4 = Image.open(args.img4)
w1, h1 = img1.size
w2, h2 = img2.size
w3, h3 = img3.size
w4, h4 = img4.size

# Calculate size of canvas
canvas_width = max(w1+w2, w3+w4)
canvas_height = max(h1+h2, h3+h4)

# Create new image of the calculated size
canvas = Image.new("RGB", (canvas_width, canvas_height))

# Paste images on canvas
canvas.paste(img1, (0, 0))
canvas.paste(img2, (0, h1))
canvas.paste(img3, (w1, 0))
canvas.paste(img4, (w1, h1))

# Save image on disk
canvas.save("canvas.jpg")
