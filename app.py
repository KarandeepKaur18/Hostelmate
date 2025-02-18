from flask import Flask,render_template,redirect,url_for, flash,request , session 
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from flask_bcrypt import Bcrypt
import hashlib
import re

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "app.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SECRET_KEY'] = 'your_secret_key'
UPLOAD_FOLDER = 'static/images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

db = SQLAlchemy(app)


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"  # Redirect to login page if not authenticated


# User Model
class User(db.Model, UserMixin):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    mobile = db.Column(db.String(15), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    profile_picture = db.Column(db.String(100), nullable=True)  # Profile picture column

with app.app_context():
    db.create_all()
# Flask-Login: Load user from session
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Function to check strong password
def is_strong_password(password):
    return (
        len(password) >= 8 and
        re.search(r'[A-Z]', password) and
        re.search(r'[a-z]', password) and
        re.search(r'\d', password) and
        re.search(r'[!@#$%^&*]', password)
    )


# Function to hash password using hashlib
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']



class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, nullable=False)
    book_name = db.Column(db.String(100), nullable=False)
    book_price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, default=1)



class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    message = db.Column(db.Text, nullable=False)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/faq")
def faq():
    return render_template("faq.html")

@app.route("/travel")
def travel():
    return render_template("travel.html")

@app.route('/press')
def press():
    return render_template('press.html')


blog_data = {
    "backpacking-asia": {
        "title": "Backpackers Guide To South East Asia",
        "image": "images/Southeastasia.webp",
        "content": """Southeast Asia is a dream destination for backpackers, offering affordable travel, stunning landscapes, and rich cultures. 
                      From Thailand's vibrant streets to Bali’s serene beaches, this guide will help you navigate the best spots.""",
    },
    "backpacking-laos": {
        "title": "How To Backpack Around Laos",
        "image": "images/Laos.jpg",
        "content": """Laos is a hidden gem in Southeast Asia, known for its breathtaking nature, friendly locals, and budget-friendly travel experiences. 
                      From Luang Prabang's temples to Vang Vieng's adventure sports, here’s what you need to know before you go.""",
    },
    "backpacking-vietnam": {
        "title": "Backpacker's Guide To Travel Around Vietnam",
        "image": "images/veitnam.jpg",
        "content": """Vietnam offers a mix of history, nature, and delicious cuisine. Whether you’re exploring the bustling streets of Hanoi, 
                      cruising in Halong Bay, or trekking in Sapa, this guide will help you make the most of your journey.""",
    },
    "backpacking-europe": {
        "title": "Complete Guide To Backpacking Europe",
        "image": "images/Europe.jpg",
        "content": """Backpacking through Europe is an adventure of a lifetime. With a Eurail pass, budget hostels, and incredible history, 
                      you can explore diverse cultures from Western to Eastern Europe.""",
    },
    "interrail-destinations": {
        "title": "This Year's Best Interrail Destinations",
        "image": "images/iterrail.jpg",
        "content": """Interrailing across Europe is one of the best ways to explore multiple countries affordably. 
                      Here’s a list of the best destinations to include in your trip this year.""",
    },
    "solo-travel-spain": {
        "title": "Solo Travel In Spain",
        "image": "images/Spain.jpg",
        "content": """Spain is a fantastic destination for solo travelers, offering rich culture, great food, and friendly locals. 
                      From Barcelona’s vibrant streets to Andalusia’s scenic landscapes, here’s how to travel solo in Spain.""",
    },
}


@app.route('/travel')
def travel_page():
    return render_template('travel.html')

@app.route('/blog/<blog_id>')
def blog_page(blog_id):
    if blog_id in blog_data:
        return render_template('blog_template.html', blog=blog_data[blog_id])
    return "Blog not found", 404




app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hostel.db'
# db = SQLAlchemy(app)

class TermsAcceptance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    accepted_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    ip_address = db.Column(db.String(45), nullable=False)

@app.route('/terms')
def terms():
    return render_template('terms.html')



@app.route('/career')
def career():
    jobs = [
        {"title": "Software Engineer", "location": "Remote", "type": "Full-time"},
        {"title": "Marketing Specialist", "location": "Delhi,India", "type": "Part-time"},
        {"title": "Customer Support", "location": "Bangalore,India", "type": "Full-time"},
    ]
    return render_template('career.html', jobs=jobs)


# Register Route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        mobile = request.form.get('mobile')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        # Check if fields are empty
        if not all([name, email, mobile, password, confirm_password]):
            flash("⚠ All fields are required!", "warning")
            return redirect(url_for('signup'))

        # Check if passwords match
        if password != confirm_password:
            flash("❌ Passwords do not match!", "danger")
            return redirect(url_for('signup'))

        # Validate strong password
        if not is_strong_password(password):
            flash("⚠ Password must be at least 8 characters, include an uppercase, lowercase, number, and special character (!@#$%^&*).", "warning")
            return redirect(url_for('signup'))

        # Check if user already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash("📧 Email already registered. Please login!", "warning")
            return redirect(url_for('login'))
  # Hash password and save user
        hashed_password = hash_password(password)
        new_user = User(name=name, email=email, mobile=mobile, password=hashed_password)

        try:
            db.session.add(new_user)
            db.session.commit()
            flash("✅ Registration successful! Please login.", "success")
            return redirect(url_for('login'))
        except Exception as e:
            db.session.rollback()
            flash(f"❌ Database Error: {str(e)}", "danger")
            return redirect(url_for('signup'))

    return render_template('sign_up.html')

# Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user and user.password == hash_password(password):
            login_user(user)  # Log in the user
            flash("✅ Login successful!", "success")
            return redirect(url_for('dashboard'))  # Redirect to dashboard
        else:
            flash("❌ Invalid email or password. Try again!", "danger")
            return redirect(url_for('login'))

    return render_template('login.html')

# Dashboard Route (Protected)
@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

# Logout Route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("✅ Logged out successfully!", "info")
    return redirect(url_for('login'))

# Profile Route (Protected)
@app.route("/profile", methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        mobile = request.form.get('mobile')

        if not all([name, email, mobile]):
            flash("⚠ All fields are required!", "warning")
            return redirect(url_for('profile'))

 # Handle profile picture upload
        if 'profile_picture' in request.files:
            file = request.files['profile_picture']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)

                # Update user's profile picture in the database
                current_user.profile_picture = filename
                db.session.commit()  # Commit change

        # Update user details
        current_user.name = name
        current_user.email = email
        current_user.mobile = mobile
        db.session.commit()

        flash("✅ Profile updated successfully!", "success")

    return render_template("profile.html", user=current_user)
# Edit Profile Route (Protected)
@app.route("/edit_profile", methods=['GET', 'POST'])
@login_required
def edit_profile():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        mobile = request.form['mobile']

        # Handle profile picture upload
        if 'profile_picture' in request.files:
            file = request.files['profile_picture']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)

                current_user.profile_picture = filename  # Save filename to the user
                db.session.commit()  # Commit changes

        # Update user details
        current_user.name = name
        current_user.email = email
        current_user.mobile = mobile
        db.session.commit()

        flash("✅ Profile updated successfully!", "success")
        return redirect(url_for('profile'))  # Redirect back to profile page

    return render_template("edit_profile.html", user=current_user)


if __name__ == '__main__':
    app.run(debug=True)

    


