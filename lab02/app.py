from flask import Flask, render_template , request , json 
from cipher.caesar import CaesarCipher

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/caesar")
def caesar():
    return render_template("caesar.html")
@app.route("/encrypt" , methods = ['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyCipher'])
    Caesar = CaesarCipher()
    decrypted_text = Caesar.encrypt(text,key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {decrypted_text}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 5050 , debug = True)