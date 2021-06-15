
# Upload plików i udsostępnianie jako unique URL

from flask import Flask, request, redirect, render_template, \
    send_file, flash, abort
import secrets
from werkzeug.utils import secure_filename
import os
import glob

app = Flask("upload")
app.secret_key = secrets.token_hex(64)
app.config["UPLOAD_FOLDER"] = "upload"
app.config["MAX_CONTENT_LENGTH"] = 16*1024*1024

@app.route("/get/<token>", methods=['GET'])
def download(token):
    """
     http://127.0.0.1:5000/get/h5Qz5VViXNqOQTQW8vKPA
    """
    pattern = f"{app.config['UPLOAD_FOLDER']}/{token}_*"
    items = glob.glob(pattern)
    if len(items)==0:
        return abort(404, description="Nie znaleziono pliku")
    else:
        tmp_file = items[0]
        return send_file(tmp_file, as_attachment=True,
                         attachment_filename=os.path.basename(tmp_file))


@app.route("/", methods=['GET','POST'])
def upload_form():
    if request.method=="GET":
        return render_template("upload.html")
    else:
        if 'file' not in request.files or \
                request.files['file'].filename=="":
            flash("Wybierz plik")
            return redirect(request.url)
        # własciwy upload pliku
        file = request.files['file']
        token = secrets.token_urlsafe(16).replace("_","")
        filename = f"{token}_{secure_filename(file.filename)}"
        file.save( os.path.join(app.config["UPLOAD_FOLDER"], filename) )
        url = f"{request.url_root}get/{token}"
        flash(url)
        return redirect("/")

app.run(debug=True)