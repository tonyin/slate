from slate import app
from flask import render_template, flash, redirect
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'first': 'Tony'}
    modules = [
        {
            'name': 'sleep',
            'data': [1,2,3,4,5]
        }
    ]
    return render_template(
        'index.html',
        title='Welcome to Slate',
        user=user,
        modules=modules)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('OpenID {0} requesting access..'.format(form.openid.data))
        return redirect('/index')
    return render_template(
        'login.html',
        title='Slate | ' + 'Sign In',
        form=form)

#################
# Error Handlers
#################

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500
