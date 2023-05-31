from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user1:salam1@localhost/mydatabase'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    gender = db.Column(db.String(10))
    birthdate = db.Column(db.Date)
    nickname = db.Column(db.String(255), unique=True, nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/kayit', methods=['POST'])
def kayit():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    gender = request.form['gender']
    birthdate = request.form['birthdate']
    nickname = request.form['nickname']

    # Kayıt işlemini gerçekleştirme kodunu buraya ekleyin
    new_user = User(username=username, email=email, password=password, gender=gender, birthdate=birthdate, nickname=nickname)
    db.session.add(new_user)
    db.session.commit()

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
@app.route('/giris', methods=['POST'])
def giris():
    email = request.form['email']
    password = request.form['password']

    # Giriş işlemini gerçekleştirme kodunu buraya ekleyin
    user = User.query.filter_by(email=email, password=password).first()
    if user:
        # Giriş başarılı, kullanıcı ana sayfaya yönlendirilsin
        return redirect('/')
    else:
        # Giriş başarısız, kullanıcıya hata mesajı gösterilsin
        return render_template('index.html')
