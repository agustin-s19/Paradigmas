from flask import Flask, render_template
from forms import Loginform



app = Flask(__name__)
app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'

@app.route('/')

def home():
    return render_template('home.html')

@app.route("/Registro", methods=["GET", "POST"])
def show_signup_form():
    form =  Loginform()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        next = request.args.get('next', None)
        if next:
            return redirect(next)
        return redirect(url_for('index'))
    return render_template("signup_form.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)