import numpy as np
from PIL import Image
import io
from flask import send_file
def mani_image(request):
    print("mani_image() called")

    # Get the image and rotation angle from the request
    image_file = request.files.get('image')
    rotation_angle = float(request.form.get('rotation', 0))
    grayscale = request.form.get('grayscale', False)
    print('Rotation angle:', rotation_angle)
    print('Grayscale:', grayscale)
    if image_file:
        # Open the image
        image = Image.open(image_file.stream)

        # Convert the image to a NumPy array
        image_array = np.array(image)
        if rotation_angle != 0:
            image_array = np.rot90(image_array, k=int(-rotation_angle / 90))

        # Apply grayscale if specified
        if grayscale:
            # Convert the image to grayscale by averaging the color channels
            if len(image_array.shape) == 3 and image_array.shape[2] == 3:  # RGB image
                image_array = np.mean(image_array, axis=2).astype(np.uint8)
            elif len(image_array.shape) == 3 and image_array.shape[2] == 4:  # RGBA image
                image_array = np.mean(image_array[:, :, :3], axis=2).astype(np.uint8)

        # Convert the manipulated image back to a PIL image
        if len(image_array.shape) == 2:  # Grayscale image
            rotated_image = Image.fromarray(image_array, mode='L')
        else:
            rotated_image = Image.fromarray(image_array)

        # Save the manipulated image to a bytes buffer
        buffer = io.BytesIO()
        rotated_image.save(buffer, format='PNG')
        buffer.seek(0)

        return send_file(buffer, mimetype='image/png', as_attachment=True, download_name='modified.png')

    return 'No image uploaded', 400
