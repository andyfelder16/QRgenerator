from flask import Flask, render_template, request
import webbrowser
import mail
import qr

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def home():
    if request.method == 'POST':
        contenido = request.form['contenido']
        email = request.form['email']
        qr.generateQR(contenido)
        mail.enviarMail(email)
        return successPage()
    return render_template('index.html')

@app.route("/success")
def successPage():
    return render_template('success.html')

def open_browser():
      webbrowser.open_new('http://127.0.0.1:2000/')

def start_server():
    #webbrowser.open_new('http://127.0.0.1:2000/')
    open_browser()
    app.run(debug=False, port=2000)

if __name__ == "__main__":
    start_server()
