from flask import Flask, render_template


def main():
    app = Flask(__name__)

    @app.route('/')
    def main_page():
        return render_template('index.html')

    app.run()
