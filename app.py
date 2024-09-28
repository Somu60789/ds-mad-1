from flask import Flask, render_template, redirect, url_for, flash
from database import db
from models import User, Service, ServiceRequest
from forms import LoginForm, RegisterForm, ServiceRequestForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///household_services.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            # Add login logic (e.g., using Flask-Login)
            return redirect(url_for('dashboard'))
        flash('Login Unsuccessful. Please check username and password')
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, password=form.password.data, role=form.role.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! You can now log in.')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/admin/dashboard')
def dashboard():
    services = Service.query.all()
    return render_template('admin_dashboard.html', services=services)

@app.route('/service_request', methods=['GET', 'POST'])
def service_request():
    form = ServiceRequestForm()
    form.service_id.choices = [(s.id, s.name) for s in Service.query.all()]
    if form.validate_on_submit():
        new_request = ServiceRequest(service_id=form.service_id.data, customer_id=1)  # replace with actual customer id
        db.session.add(new_request)
        db.session.commit()
        flash('Service request created successfully!')
        return redirect(url_for('dashboard'))
    return render_template('service_request.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
