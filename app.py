from flask import Flask, render_template,request,redirect
from random_code import code
from model import add_long_url
from model import get_url

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        long_code = request.form.get("url","").strip()

        if not long_code.startswith(("http://","https://")):
            long_code = "https://" + long_code
        codes = code()

        add_long_url(codes,long_code)
        short_url = f"http://127.0.0.1:5000/{codes}"
        return render_template("index.html", short_url=short_url)
    return render_template("index.html")

@app.route("/<codes>")
def redirect_url(codes):
    long_url = get_url(codes)
    if long_url:
        return redirect(long_url)

    return "url not found",404

if __name__=="__main__":
    app.run(debug=True)


    

