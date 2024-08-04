Here’s the README in Markdown format:

```markdown
# Image Manipulator Web Application

This project is an open-source web application that allows users to upload an image, apply various manipulations (such as rotation and grayscale), and download the modified image. The backend is built using Flask, and image manipulation is performed using NumPy and Pillow.

## Directory Structure

```
c:/Users/Sujas/Desktop/Coding/Python/RandomStuff/
├── static/
│   ├── images/
│   │   ├── b&w.png
│   │   └── rotate.png
│   ├── features.js
│   ├── script.js
│   └── style.css
├── templates/
│   └── index.html
├── .gitignore
├── image.py
├── index.py
├── README.md
├── requirements.txt
└── vercel.json
```

## Prerequisites

- Python 3.x
- Flask
- Pillow
- NumPy
- Vercel CLI (if deploying on Vercel)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Sujas-Aggarwal/flask-image-manipulator.git
   cd ImageManipulator
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. **Start the Flask application:**

   ```bash
   python index.py
   ```

2. **Open your browser and navigate to:**

   ```
   http://127.0.0.1:5000/
   ```

## Project Structure

- **static/**: Contains static files such as images, JavaScript, and CSS.
  - **images/**: Contains images used in the web application (e.g., buttons for rotation and grayscale).
  - **features.js**: JavaScript for handling image manipulations.
  - **script.js**: Additional JavaScript functions.
  - **style.css**: CSS for styling the web application.
  
- **templates/**: Contains HTML templates.
  - **index.html**: The main HTML template for the web application.
  
- **image.py**: Contains the `mani_image` function for handling image manipulations using NumPy and Pillow.
- **index.py**: The main Flask application file.
- **requirements.txt**: A list of Python dependencies.
- **vercel.json**: Configuration file for deploying the application on Vercel.
- **.gitignore**: Specifies files and directories to be ignored by Git.

## Features

- **Rotate Image**: Rotates the image by 90 degrees each time the rotate button is clicked.
- **Grayscale Image**: Converts the image to grayscale when the grayscale button is clicked.

## Deploying on Vercel

1. **Install Vercel CLI:**

   ```bash
   npm install -g vercel
   ```

2. **Deploy the application:**

   ```bash
   vercel
   ```

   Follow the prompts to complete the deployment.


## Acknowledgements

- This project uses [Flask](https://flask.palletsprojects.com/), [Pillow](https://python-pillow.org/), and [NumPy](https://numpy.org/).
```

Feel Free to add more features to this!

Current Goals are - 
Cropping,
Compression,
Hue,
Saturation,
Brightness