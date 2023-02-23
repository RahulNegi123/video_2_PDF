import os
from PIL import Image

# Set the path of the folder containing the images
path = r'D:\New Volume E\CAREER\Development\v2pdf\dissimilar_images'



# Set the filename of the output PDF
output_filename = "output.pdf"

# Create a new PDF
pdf = Image.new("RGB", (1, 1), "white")

# Iterate over all images in the folder
for filename in os.listdir(path):
    try:
        # Load the current image
        image = Image.open(os.path.join(path, filename))

        # Add the image to the PDF
        if image.mode != "RGB":
            image = image.convert("RGB")
        pdf = Image.new("RGB", (max(pdf.size[0], image.size[0]), pdf.size[1] + image.size[1]), "white")
        pdf.paste(pdf, (0, 0))
        pdf.paste(image, (0, pdf.size[1] - image.size[1]))
    except Exception as e:
        print(f"Error processing file {filename}: {e}")

# Save the PDF
pdf.save(output_filename, "PDF", resolution=100.0)
