import numpy as np
from PIL import Image
import io
from flask import send_file
def mani_image(request):
    print("mani_image() called")

    # Get the image and rotation angle from the request
    image_file = request.files.get('image')
    rotation_angle = float(request.form.get('rotation', 0))
    print('Rotation angle:', rotation_angle)
    if image_file:
        # Open the image
        image = Image.open(image_file.stream)

        # Convert the image to a NumPy array
        image_array = np.array(image)

        # Apply your manipulation here, e.g., rotate the image using NumPy
        rotated_image_array = np.rot90(image_array, k=int(-rotation_angle / 90))

        # Convert the manipulated image back to a PIL image
        rotated_image = Image.fromarray(rotated_image_array)

        # Save the manipulated image to a bytes buffer
        buffer = io.BytesIO()
        rotated_image.save(buffer, format='PNG')
        buffer.seek(0)

        return send_file(buffer, mimetype='image/png', as_attachment=True, download_name='rotated_image.png')

    return 'No image uploaded', 400
