from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/delete-recording")
def delete_recording():
    return render_template("delete-recording.html")


@app.route("/delete-recording-success")
def delete_recording_success():
    return render_template("delete-recording-success.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0')
