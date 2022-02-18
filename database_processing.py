from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import InternalServerError
import sqlite3
import webbrowser
import threading
from PyQt5.QtWidgets import QMessageBox
import sys

sys.tracebacklimit = 0  # traceback görüntülenmemesi için

vt = sqlite3.connect("veritabani.db")
im = vt.cursor()
im.execute("""SELECT * FROM metin__anahtar__tablo""")
veriler = (
    im.fetchall()
)  # tablodaki verileri fetchall fonksiyonu ile veriler değişkenine alıyorum

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///veritabani.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Metin_Anahtar_Tablo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Metin = db.Column(db.String, unique=True, nullable=False)
    Lemma_metin = db.Column(db.String, unique=True, nullable=False)
    Metin_pos = db.Column(db.String, unique=True, nullable=False)
    Anahtar = db.Column(db.String, unique=True, nullable=False)


db.create_all()

gelen_metin = ""
gelen_metin_lemma_str = ""
gelen_metin_lemma_pos_str = ""
gelen_siralanmis_anahtar_kelimeler_str = ""


def degiskenleri_al(metin, metin_lemma, metin_token_pos, siralanmis_anahtar_kelimeler):
    global gelen_metin
    gelen_metin = metin

    global gelen_metin_lemma_str
    global gelen_metin_lemma_pos_str
    global gelen_siralanmis_anahtar_kelimeler_str

    gelen_metin_lemma_str = " ".join(
        metin_lemma
    )  # metin_lemma listesini boşluğa göre listedeki kelimeleri birleştirip str elde ediyorum.

    for i, y in zip(metin_lemma, metin_token_pos):
        gelen_metin_lemma_pos_str = (
            gelen_metin_lemma_pos_str + str("(" + i + " - " + y + ")") + ", "
        )

    for i, y in zip(
        siralanmis_anahtar_kelimeler, range(len(siralanmis_anahtar_kelimeler))
    ):
        gelen_siralanmis_anahtar_kelimeler_str = (
            gelen_siralanmis_anahtar_kelimeler_str + str(y + 1) + " - " + str(i) + ", "
        )


def veritabani_kayit_ekle():
    for i in range(
        len(veriler)
    ):  # Tabloda aynı kayıt var mı, yok mu kontrolü. for/else yapısı
        if (
            veriler[i][1] == gelen_metin
            or veriler[i][2] == gelen_metin_lemma_str
            or veriler[i][3] == gelen_metin_lemma_pos_str
            or veriler[i][4] == gelen_siralanmis_anahtar_kelimeler_str
        ):
            vrtbni_ekle_hata = QMessageBox()
            vrtbni_ekle_hata.setIcon(QMessageBox.Critical)
            vrtbni_ekle_hata.setText("The same record exists in the database!")
            vrtbni_ekle_hata.setWindowTitle("Warning")
            vrtbni_ekle_hata.exec_()
            break
    else:
        a = Metin_Anahtar_Tablo(
            Metin=gelen_metin,
            Lemma_metin=gelen_metin_lemma_str,
            Metin_pos=gelen_metin_lemma_pos_str,
            Anahtar=gelen_siralanmis_anahtar_kelimeler_str,
        )
        db.session.add(a)
        db.session.commit()
        vrtbni_ekle = QMessageBox()
        vrtbni_ekle.setIcon(QMessageBox.Information)
        vrtbni_ekle.setText("Added Record to Database")
        vrtbni_ekle.setWindowTitle("Process Completed")
        vrtbni_ekle.exec_()


@app.route("/")
def Veritabani_Goruntule():
    Veritabani_Goruntule = Metin_Anahtar_Tablo.query.paginate()
    return render_template(
        "veritabani_sayfasi.html", Veritabani_Goruntule=Veritabani_Goruntule
    )


app.secret_key = "super secret key"


@app.route("/delete/<int:id>", methods=["POST", "GET"])
def Veritabani_SatirSil(id):
    try:
        veri = Metin_Anahtar_Tablo.query.get(id)
        db.session.delete(veri)
        db.session.commit()
        return redirect(url_for("Veritabani_Goruntule"))
    except Exception as e:
        print("Hata: " + str(e))


@app.errorhandler(InternalServerError)
def handle_500(e):
    original = getattr(e, "Hata", None)
    return render_template("hata_sayfasi.html", e=original)


def calistir():
    webbrowser.open_new_tab("http://127.0.0.1:5000/")
    app.run(debug=False)


def calistir_threading():
    t1 = threading.Thread(target=calistir)
    t1.start()
