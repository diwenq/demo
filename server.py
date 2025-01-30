from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")  # 渲染 HTML 文件

@app.route("/static/<path:filename>")
def static_files(filename):
    return app.send_static_file(filename)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
