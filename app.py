from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Blog Home."


from mod_admin import admin
app.register_blueprint(admin)


if __name__ == '__main__':
    app.secret_key='secret123'
    app.run(debug=True)
