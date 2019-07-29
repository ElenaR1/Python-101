from flask import Flask, render_template
from form import InputForm
app = Flask(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'



class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])
    
    @app.route("/", methods=['GET', 'POST'])
    def hello():
        form = ReusableForm(request.form)
    
        print form.errors
        if request.method == 'POST':
            name=request.form['name']
            print name
    
        if form.validate():
            # Save the comment here.
            flash('Hello ' + name)
        else:
            flash('All the form fields are required. ')




@app.route("/")
def home():
    #return render_template('home.html', posts=posts)
    return 'Home'

@app.route('/title')
def title():
    title=InputForm()
    return render_template('title_form.html',form=form)


if __name__ == '__name__':
    app.run(debug=True)

