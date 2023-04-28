from flask import Flask, render_template, redirect, url_for, request, session, abort
from itsdangerous import Signer, BadSignature
from .session_interface import MySessionInterface

app = Flask(__name__)
app.secret_key = b"_78r9er1f3_?"
app.session_interface = MySessionInterface()

def get_current_username():
    # Kullanıcının giriş yapıp yapmadığını tespit eden foonkisyon
    username = ""
    login_auth = False
    if "username" in session:
        username = session["username"]
        login_auth = True
    return username, login_auth


@app.route("/")
def Index():
    #anasayfaya yönlendirir.
    username, login_auth = get_current_username()
    return render_template("index.html", username=username, login_auth=login_auth)


@app.route("/about")
def About():
    # Hakkında kısmı
    username, login_auth = get_current_username()
    return render_template("about.html", username=username, login_auth=login_auth)


@app.route("/contact", methods=['GET', 'POST'])
def Contact():
    #İletişim kısmı

    if request.method == 'POST':
        pass

    username, login_auth = get_current_username()
    return render_template("contact.html", username=username, login_auth=login_auth)


@app.route("/login", methods=['GET', 'POST'])
def Login():
    #Giriş işlemleri
    if request.method == 'POST':
        #session bilgilerini alma burada yapılır
        if request.form:
            if "username" in request.form and "password" == request.form:
                username = request.form["username"]
                password = request.form["password"]

                #kayıtlı kullanıcı doğrulaması
                if username == 'asd' and password == 'asd':
                    session["username"] = username
                    return redirect(url_for("Index"))
                else:
                    return redirect(url_for("Login"))

            #abort(400)

    username, login_auth = get_current_username()
    return render_template("login.html", username=username, login_auth=login_auth)


@app.route("/logout")
def Logout():
    #Giriş yapan kullanıcının çıkış yapmasını sağlar
    if "username" in session:
        del session["username"]
    return redirect(url_for("Index"))
