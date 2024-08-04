from flask import Flask, request,redirect,render_template
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

if __name__ == '__main__':
    app.run(debug=True)