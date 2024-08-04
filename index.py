from flask import Flask, request,redirect,render_template
from image import mani_image
app = Flask(__name__)
@app.before_request
def middleware():
    request_path= request.path
    if request_path.startswith('/api'):
        redirect_path = request_path.replace('/api','')
        print('Request Path:',request_path)
        print('Redirect Path:',redirect_path)
        return redirect(redirect_path)
    return None
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload',methods=['POST'])
def upload():
    return mani_image(request)
if __name__ == '__main__':
    app.run(debug=True)