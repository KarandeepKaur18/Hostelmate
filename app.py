from flask import Flask,render_template,redirect,url_for, flash,request , session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_migrate import Migrate
import os
from datetime import date
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from flask_bcrypt import Bcrypt
import hashlib
import re

app=Flask(__name__) 
basedir = os.path.abspath(os.path.dirname(__file__))

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "app.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SECRET_KEY'] = 'your_secret_key'
UPLOAD_FOLDER = 'static/images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


db = SQLAlchemy(app)
migrate = Migrate(app, db)


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

# Database model

class City(db.Model):
    id  = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(100),nullable = False)
    checkin = db.Column(db.String(20), nullable=False)
    checkout = db.Column(db.String(20), nullable=False)
    guests = db.Column(db.Integer, nullable=False)
    hostel_link = db.Column(db.String(200), nullable=True)
    title = db.Column(db.String(100), nullable=False)  
    image = db.Column(db.String(200), nullable=False)  # Path to image
    image2 = db.Column(db.String(200), nullable=False)  # Path to image
    description = db.Column(db.Text, nullable=False) 


    def __repr__(self):
        return f"City(id={self.id}, city='{self.city}', checkin={self.checkin}, checkout={self.checkout}, guests={self.guests})"


with app.app_context():
    db.drop_all()
    db.create_all()
    print("Table drop and recreate")
    if not City.query.first():
        cities = [
            City(city="Delhi", checkin="2025-03-10", checkout="2025-03-15", guests=3,
                    title="Welcome to Mumbai", image="images/delhi.jpg", image2="images/hostel2.jpg",
                    description="Discover the city of dreams, Mumbai, with its stunning coastline and bustling streets."),
            City(city="Mumbai", checkin="2025-03-10", checkout="2025-03-15", guests=3,
                    title="Welcome to Mumbai", image="images/mumbai.png", image2="images/hostel3.avif",
                    description="Discover the city of dreams, Mumbai, with its stunning coastline and bustling streets."),
            City(city="Mysore", checkin="2025-03-01", checkout="2025-03-05", guests=2,
                    title="Welcome to Delhi", image="images/mysore.png", image2="images/hotel1.jpg",
                    description="Located in Mysore, 4.2 km from Mysore Palace, Leo vishroam provides accommodation with a garden, free private parking and a shared lounge."),
            City(city="Kerela", checkin="2025-04-01", checkout="2025-04-10", guests=4,
                    title="Welcome to Goa", image="images/kerela.png", image2="images/HOSTEL4.jpg",
                    description="Relax on the beaches of Goa and experience its vibrant nightlife."),
            City(city="Alleppey", checkin="2025-04-01", checkout="2025-04-10", guests=4,
                    title="Welcome to Alleppey", image="images/desti1.png", image2="images/delhi_host.webp",
                    description="Relax on the beaches of Goa and experience its vibrant nightlife."),
            City(city="Andaman", checkin="2025-04-01", checkout="2025-04-10", guests=4,
                    title="Welcome to Andaman", image="images/desti2.jpg", image2="images/mysore_host.webp",
                    description="Relax on the beaches of Goa and experience its vibrant nightlife."),
            City(city="Burwa", checkin="2025-04-01", checkout="2025-04-10", guests=4,
                    title="Welcome to Burwa", image="images/burwa.png", image2="images/mumbai_host.webp",
                    description="Relax on the beaches of Goa and experience its vibrant nightlife."),
            City(city="Hampi", checkin="2025-04-01", checkout="2025-04-10", guests=4,
                    title="Welcome to Hampi", image="images/desti3.jpg", image2="images/hotel1.jpg",
                    description="Relax on the beaches of Goa and experience its vibrant nightlife."),
            City(city="Spiti", checkin="2025-04-01", checkout="2025-04-10", guests=4,
                    title="Welcome to Spiti", image="images/spiti.jpg", image2="images/hostel3.avif",
                    description="Relax on the beaches of Goa and experience its vibrant nightlife."),
            City(city="Bhutan", checkin="2025-04-01", checkout="2025-04-10", guests=4,
                    title="Welcome to Bhutan", image="images/bhutan.jpg", image2="images/mumbai_host.webp",
                    description="Relax on the beaches of Goa and experience its vibrant nightlife."),
            City(city="Arunanchal Pradesh", checkin="2025-04-01", checkout="2025-04-10", guests=4,
                    title="Welcome to Arunanchal Pradesh", image="images/ap.jpg", image2="images/delhi_host.webp",
                    description="Relax on the beaches of Goa and experience its vibrant nightlife."),
            City(city="Sikkim", checkin="2025-04-01", checkout="2025-04-10", guests=4,
                    title="Welcome to Sikkim", image="images/sikkim.png", image2="images/hostel2.jpg",
                    description="Relax on the beaches of Goa and experience its vibrant nightlife."),
            City(city="Mysore", checkin="2025-04-01", checkout="2025-04-10", guests=4,
                    title="Welcome to Mysore", image="images/mysore.png", image2="images/mysore_host.webp",
                    description="Relax on the beaches of Goa and experience its vibrant nightlife."),
            City(city="Kolkata", checkin="2025-04-01", checkout="2025-04-10", guests=4,
                    title="Welcome to Kolkata", image="images/kolkata.jpeg", image2="images/HOSTEL4.jpg",
                    description="Relax on the beaches of Goa and experience its vibrant nightlife."),
            City(city="Chennai", checkin="2025-04-01", checkout="2025-04-10", guests=4,
                    title="Welcome to Chennai", image="images/chennai.jpeg", image2="images/delhi_host.webp",
                    description="Relax on the beaches of Goa and experience its vibrant nightlife."),
            City(city="Banglore", checkin="2025-04-01", checkout="2025-04-10", guests=4,
                    title="Welcome to Banglore", image="images/banglore.jpeg", image2="images/HOSTEL4.jpg",
                    description="Relax on the beaches of Goa and experience its vibrant nightlife."),
            City(city="Hyderabad", checkin="2025-04-01", checkout="2025-04-10", guests=4,
                    title="Welcome to Hyderabad", image="images/hyderabad.jpeg", image2="images/hostel2.jpg",
                    description="Relax on the beaches of Goa and experience its vibrant nightlife."),
            City(city="Pune", checkin="2025-04-01", checkout="2025-04-10", guests=4,
                    title="Welcome to Pune", image="images/pune.jpeg", image2="images/hostel2.jpg",
                    description="Relax on the beaches of Goa and experience its vibrant nightlife."),
            
        ]


        db.session.add_all(cities)
        db.session.commit()



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


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    message = db.Column(db.Text, nullable=False)

@app.route("/")
def home():
    cities = City.query.all()  # Fetch all cities from the database
    return render_template("index.html", cities=cities)


@app.route("/search", methods=['POST'])
def search():
    if request.method == "POST":
        city_id = request.form.get('city_id')
        checkin = request.form.get("checkin")
        checkout = request.form.get("checkout")
        guests = request.form.get("guests")
        
        city = City.query.get(city_id)
        
        if city:
            return render_template('search.html',
                                   city=city,
                                   checkin=checkin,
                                   checkout=checkout,
                                   guests=guests)
        else:
            return "City not found", 404

    return redirect(url_for('home'))



@app.route("/book")
def book():
    return render_template('book.html')

@app.route("/submit_booking" , methods=['GET','POST'])
def submit_booking():
    username = request.form.get("username")
    email = request.form.get("email")
    phone = request.form.get("phone")
    check_in = request.form.get("check_in")
    check_out = request.form.get("check_out")
    payment_method = request.form['payment_method']
    card_number = request.form['card_number']
    expiry_date = request.form['expiry_date']
    cvv = request.form['cvv']
    
    return render_template('confirmation.html',username=username, email=email, phone=phone,
                           check_in=check_in, check_out=check_out, 
                           payment_method=payment_method, 
                           card_number=card_number, expiry_date=expiry_date,
                           cvv=cvv)

@app.route('/confirmation')
def booking_confirmation():
    return redirect(url_for('index'))


@app.route("/workation")
def workation():
    return render_template('workation.html')

@app.route("/connect")
def connect():
    return render_template("connect.html")



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
        "content": """
        Southeast Asia is a dream destination for backpackers, offering affordable travel, stunning landscapes, and rich cultures. 
        From Thailand's vibrant streets to Bali’s serene beaches, this guide will help you navigate the best spots.

        **Best Time to Visit:**
        - Dry Season (Nov - April): Best weather, great for beaches and outdoor activities.
        - Rainy Season (May - Oct): Fewer tourists and lower prices, but occasional heavy rains.

        **Budget:**
        - Daily Budget: $20 - $50 (depends on country and travel style)
        - Accommodation: $5-$15 for hostels, $20+ for budget hotels
        - Food: $2-$5 for street food, $10+ for restaurants
        - Transport: Buses, trains, and budget airlines offer affordable options.

        **Top Destinations:** Thailand, Vietnam, Cambodia, Laos, Malaysia, Indonesia.

        **Tips:** Eat local, use overnight buses, and negotiate prices where possible.
        """,
    },
    "backpacking-laos": {
        "title": "How To Backpack Around Laos",
        "image": "images/Laos.jpg",
        "content": """
        Laos is a hidden gem in Southeast Asia, known for its breathtaking nature, friendly locals, and budget-friendly travel experiences. 
        From Luang Prabang's temples to Vang Vieng's adventure sports, here’s what you need to know before you go.

        **Best Time to Visit:**
        - Dry Season (Nov - April): Pleasant weather, best for trekking and sightseeing.
        - Rainy Season (May - Oct): Lush landscapes, but some remote areas may be hard to access.

        **Budget:**
        - Daily Budget: $15 - $40
        - Accommodation: $5-$10 for hostels, $15+ for guesthouses
        - Food: $2-$5 for street food, $8+ for local restaurants
        - Transport: Tuk-tuks, motorbike rentals, and buses.

        **Top Destinations:** Luang Prabang, Vang Vieng, Vientiane, 4000 Islands.

        **Tips:** Rent a motorbike for rural areas, respect local customs, and try Laotian coffee.
        """,
    },
    "backpacking-vietnam": {
        "title": "Backpacker's Guide To Travel Around Vietnam",
        "image": "images/veit.jpg",
        "content": """
        Vietnam offers a mix of history, nature, and delicious cuisine. Whether you’re exploring the bustling streets of Hanoi, 
        cruising in Halong Bay, or trekking in Sapa, this guide will help you make the most of your journey.

        **Best Time to Visit:**
        - North (Oct - April): Cool and dry, best for Hanoi, Sapa, and Halong Bay.
        - South (Nov - April): Dry season, great for Ho Chi Minh City and Mekong Delta.
        - Central (Feb - Aug): Best time for Hoi An, Da Nang, and Hue.

        **Budget:**
        - Daily Budget: $20 - $50
        - Accommodation: $5-$12 for hostels, $20+ for budget hotels
        - Food: $1.50-$5 for street food, $10+ for restaurants
        - Transport: Affordable trains, buses, and motorbike rentals.

        **Top Destinations:** Hanoi, Halong Bay, Hoi An, Ho Chi Minh City, Sapa.

        **Tips:** Try street food, use sleeper buses, and haggle at local markets.
        """,
    },
    "backpacking-europe": {
        "title": "Complete Guide To Backpacking Europe",
        "image": "images/Europe.jpg",
        "content": """
        Backpacking through Europe is an adventure of a lifetime. With a Eurail pass, budget hostels, and incredible history, 
        you can explore diverse cultures from Western to Eastern Europe.

        **Best Time to Visit:**
        - Summer (June - August): Warm weather, lively atmosphere, but higher prices.
        - Shoulder Seasons (April - May, September - October): Fewer crowds and better prices.

        **Budget:**
        - Daily Budget: $40 - $100
        - Accommodation: $15-$40 for hostels, $50+ for budget hotels
        - Food: $5-$15 for budget meals, $20+ for dining out
        - Transport: Eurail passes, budget flights, and buses.

        **Top Destinations:** Paris, Rome, Amsterdam, Prague, Barcelona.

        **Tips:** Use budget airlines, book train passes in advance, and explore free attractions.
        """,
    },
    "interrail-destinations": {
        "title": "This Year's Best Interrail Destinations",
        "image": "images/itterail.jpg",
        "content": """
        Interrailing across Europe is one of the best ways to explore multiple countries affordably. 
        Here’s a list of the best destinations to include in your trip this year.

        **Best Time to Travel:**
        - Spring & Summer (April - September): Best weather and longer daylight hours.

        **Top Destinations:** Paris, Berlin, Prague, Budapest, Vienna.

        **Tips:** Book train passes in advance, travel off-peak for savings, and stay in budget hostels.
        """,
    },
    "solo-travel-spain": {
        "title": "Solo Travel In Spain",
        "image": "images/Spain.jpg",
        "content": """
        Spain is a fantastic destination for solo travelers, offering rich culture, great food, and friendly locals. 
        From Barcelona’s vibrant streets to Andalusia’s scenic landscapes, here’s how to travel solo in Spain.

        **Best Time to Visit:**
        - Spring & Fall (March - May, September - November): Best weather and fewer crowds.

        **Budget:**
        - Daily Budget: $50 - $100
        - Accommodation: $20-$50 for hostels, $60+ for budget hotels
        - Food: $10-$20 for tapas, $30+ for dining out
        - Transport: Trains, buses, and budget airlines.

        **Top Destinations:** Barcelona, Madrid, Seville, Valencia, Granada.

        **Tips:** Learn basic Spanish phrases, eat at local tapas bars, and take free walking tours.
        """,
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




# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hostel.db'
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

@app.route('/bali')
def bali():
    return render_template('bali.html') 

@app.route('/singapur')
def singapur():
    return render_template('singapur.html')

@app.route('/barcelona')
def barcelona():
    return render_template('barcelona.html')


@app.route('/manali')
def manali():
    return render_template('manali.html')

@app.route('/paris')
def paris():
    return render_template('paris.html')

@app.route('/tokyo')
def tokyo():
    return render_template('tokyo.html')

@app.route('/rishikesh')
def rishikesh():
    return render_template('rishikesh.html')

@app.route('/goa')
def goa():
    return render_template('goa.html')


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


        db.session.commit()  # Commit changes

        # Update user details
        current_user.name = name
        current_user.email = email
        current_user.mobile = mobile
        db.session.commit()

        flash("✅ Profile updated successfully!", "success")
        return redirect(url_for('profile'))  # Redirect back to profile page

    return render_template("edit_profile.html", user=current_user)

desti_data = {
    "Alleppey": {
        "title": "Stays at Allenppey",
        "image": "images/desti1.png",
        "image2":"images/destihostel1.jpg",
        "para": """Hostel Alleppey
              Situated right at the scenic Alappuzha Beach, Zostel Alleppey is a happening backpackers' hostel ideal for exploring the town and its backwaters. A white-coloured building surrounded by swaying palm trees invites you to a dreamy beach vacation here.</p>
              """,
        "price" : """ Starting from ₹699 """,
    },

    "Andaman": {
        "title": "Stays at Andaman",
        "image": "images/desti2.jpg",
        "image2":"images/hostel_redirect.webp",
        "para": """Hostel Andaman
              Situated right at the scenic Alappuzha Beach, Zostel Alleppey is a happening backpackers' hostel ideal for exploring the town and its backwaters. A white-coloured building surrounded by swaying palm trees invites you to a dreamy beach vacation here.</p>
              """,
        "price" : """ Starting from ₹699 """,
    },

    "Delhi": {
        "title": "Stays at Delhi",
        "image": "images/delhi.jpg",
        "image2":"images/hosteldelhi.webp",
        "para": """Hostel Delhi
              Situated right at the scenic Alappuzha Beach, Zostel Alleppey is a happening backpackers' hostel ideal for exploring the town and its backwaters. A white-coloured building surrounded by swaying palm trees invites you to a dreamy beach vacation here.</p>
              """,
        "price" : """ Starting from ₹699 """,
    },
    "Mumbai": {
        "title": "Stays at Mumbai",
        "image": "images/mumbai.png",
        "image2":"images/hostelmumbai.jpeg",
        "para": """Hostel Mumbai
              Situated right at the scenic Alappuzha Beach, Zostel Alleppey is a happening backpackers' hostel ideal for exploring the town and its backwaters. A white-coloured building surrounded by swaying palm trees invites you to a dreamy beach vacation here.</p>
              """,
        "price" : """ Starting from ₹699 """,
    },
    "Burwa": {
        "title": "Stays at Burwa",
        "image": "images/burwa.png",
        "image2":"images/burwahostel.jpeg",
        "para": """Hostel Burwa
              Situated right at the scenic Alappuzha Beach, Zostel Alleppey is a happening backpackers' hostel ideal for exploring the town and its backwaters. A white-coloured building surrounded by swaying palm trees invites you to a dreamy beach vacation here.</p>
              """,
        "price" : """ Starting from ₹699 """,
    },
    "Hampi": {
       "title": "Stays at Hampi",
        "image": "images/desti3.jpg",
        "image2":"images/hampihostels.jpeg",
        "para": """Hostel Hampi 
              Situated right at the scenic Alappuzha Beach, Zostel Alleppey is a happening backpackers' hostel ideal for exploring the town and its backwaters. A white-coloured building surrounded by swaying palm trees invites you to a dreamy beach vacation here.</p>
              """,
        "price" : """ Starting from ₹699 """,
    },
}

@app.route('/destination')
def destination():
    return render_template('destination.html')

@app.route('/desti_direct/<desti_id>')
def desti_redirect(desti_id):
    if desti_id in desti_data:
        return render_template('destinationK_redirect.html', desti=desti_data[desti_id])
    return "Blog not found", 404
    # return render_template('destinationK_redirect.html')

@app.route('/desti_direct')
def desti_redirect2():
    return render_template('desti_redirect2.html')



trips_data = {
    "Kerala": {
        "title": "Trips at Kerala",
        "image": "images/desti1.png",
        "image2":"images/keralatour.jpeg",
        "para": """Kerala TOUR PACKAGE 
              Situated right at the scenic Alappuzha Beach, Zostel Alleppey is a happening backpackers' hostel ideal for exploring the town and its backwaters. A white-coloured building surrounded by swaying palm trees invites you to a dreamy beach vacation here.</p>
              """,
        "price" : """ Starting from ₹699 """,
    },

    "Spiti": {
        "title": "Trips at Spiti",
        "image": "images/spiti.jpg",
        "image2":"images/destihostel1.jpg",
        "para": """Spiti TOUR PACKAGE 
              Situated right at the scenic Alappuzha Beach, Zostel Alleppey is a happening backpackers' hostel ideal for exploring the town and its backwaters. A white-coloured building surrounded by swaying palm trees invites you to a dreamy beach vacation here.</p>
              """,
        "price" : """ Starting from ₹699 """,
    },

    "Bhutan": {
        "title": "Trips at Bhutan",
        "image": "images/bhutan.jpg",
        "image2":"images/destihostel1.jpg",
        "para": """Bhutan TOUR PACKAGE
              Situated right at the scenic Alappuzha Beach, Zostel Alleppey is a happening backpackers' hostel ideal for exploring the town and its backwaters. A white-coloured building surrounded by swaying palm trees invites you to a dreamy beach vacation here.</p>
              """,
        "price" : """ Starting from ₹699 """,
    },
    "AP": {
        "title": "Trips at Arunanchal Pradesh",
        "image": "images/mumbai.png",
        "image2":"images/destihostel1.jpg",
        "para": """Trips at Arunanchal Pradesh 
              Situated right at the scenic Alappuzha Beach, Zostel Alleppey is a happening backpackers' hostel ideal for exploring the town and its backwaters. A white-coloured building surrounded by swaying palm trees invites you to a dreamy beach vacation here.</p>
              """,
        "price" : """ Starting from ₹699 """,
    },
    "Sikkim": {
        "title": "Trips at Sikkim",
        "image": "images/sikkim.png",
        "image2":"images/destihostel1.jpg",
        "para": """Skkim TOUR PACKAGE 
              Situated right at the scenic Alappuzha Beach, Zostel Alleppey is a happening backpackers' hostel ideal for exploring the town and its backwaters. A white-coloured building surrounded by swaying palm trees invites you to a dreamy beach vacation here.</p>
              """,
        "price" : """ Starting from ₹699 """,
    },
    "Mysore": {
       "title": "Trips at Mysore ",
        "image": "images/mysore.png",
        "image2":"images/destihostel1.jpg",
        "para": """ostel Alleppey
              Situated right at the scenic Alappuzha Beach, Zostel Alleppey is a happening backpackers' hostel ideal for exploring the town and its backwaters. A white-coloured building surrounded by swaying palm trees invites you to a dreamy beach vacation here.</p>
              """,
        "price" : """ Starting from ₹699 """,
    },
}

@app.route('/trips')
def trips():
    return render_template('trips.html')

@app.route('/trips_redirect/<trips_id>')
def trips_redirect(trips_id):
    if trips_id in trips_data:
        return render_template('trips_redirect.html', trips=trips_data[trips_id])
    return "Blog not found", 404



@app.route('/connect')
def connect_travellers():
    return render_template('connectWithTraveler.html')





if __name__ == '__main__':
    app.run(debug=True)

    
