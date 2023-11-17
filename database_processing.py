import sqlite3
import sys
import threading
import webbrowser

from flask import Flask, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from PyQt5.QtWidgets import QMessageBox
from werkzeug.exceptions import InternalServerError

app = Flask("database")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class text_keyword_table(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, unique=True, nullable=False)
    text_lemma = db.Column(db.String, unique=True, nullable=False)
    text_pos = db.Column(db.String, unique=True, nullable=False)
    keyword = db.Column(db.String, unique=True, nullable=False)


db.create_all()

sys.tracebacklimit = 0  # traceback görüntülenmemesi için
database_connection = sqlite3.connect("database.db")
cursor = database_connection.cursor()
cursor.execute("""SELECT * FROM text_keyword_table""")
database_datas = cursor.fetchall()

new_data_list = []


def new_data_preprocessing(
    new_data,
):  # new_data: Tuple: TEXT, lemma_list, pos_list, sorted_key_words_or_phrases
    new_data_list.append(new_data[0])

    new_data_list.append(" ".join(new_data[1]))

    # Lemma Word + POS Type Word = lemma_pos_text (String)
    lemma_pos_text = ""
    for i, y in zip(new_data[1], new_data[2]):
        lemma_pos_text = lemma_pos_text + str("(" + i + " - " + y + ")") + ", "
    new_data_list.append(lemma_pos_text)

    # sorted_key_words_or_phrases convert to String and Different Format: sorted_key_words_or_phrases_str
    sorted_key_words_or_phrases_str=""
    for i, y in zip(new_data[3], range(len(new_data[3]))):
        sorted_key_words_or_phrases_str = (
            sorted_key_words_or_phrases_str + str(y + 1) + " - " + str(i) + ", "
        )
    new_data_list.append(sorted_key_words_or_phrases_str)


def database_add_record():
    for i, database_data in enumerate(
        (database_datas)
    ):  # Check if there is the same record in the table or not. for/else structure.
        if (
            database_data[1] == new_data_list[0]
            or database_data[2] == new_data_list[1]
            or database_data[3] == new_data_list[2]
            or database_data[4] == new_data_list[3]
        ):
            database_add_error = QMessageBox()
            database_add_error.setIcon(QMessageBox.Critical)
            database_add_error.setText("The same record exists in the database!")
            database_add_error.setWindowTitle("Warning")
            database_add_error.exec_()
            break
    else:
        cursor.execute(
            """INSERT INTO text_keyword_table (text,text_lemma,text_pos, keyword) VALUES
                (?, ?, ?, ?)""",
            new_data_list,
        )
        database_connection.commit()

        database_add = QMessageBox()
        database_add.setIcon(QMessageBox.Information)
        database_add.setText("Added Record to Database")
        database_add.setWindowTitle("Process Completed")
        database_add.exec_()


@app.route("/")
def view_database():
    view_database = text_keyword_table.query.paginate()
    return render_template("database_page.html", view_database=view_database)


app.secret_key = "super secret key"


@app.route("/delete/<int:id>", methods=["POST", "GET"])
def Database_DeleteRow(id):
    try:
        data = text_keyword_table.query.get(id)
        db.session.delete(data)
        db.session.commit()
        return redirect(url_for("view_database"))
    except Exception as e:
        print("Hata: " + str(e))


@app.errorhandler(InternalServerError)
def handle_500(e):
    original = getattr(e, "Error", None)
    return render_template("error_page.html", e=original)


def run():
    webbrowser.open_new_tab("http://127.0.0.1:5000/")
    app.run(debug=False)


def run_threading():
    t1 = threading.Thread(target=run)
    t1.start()
