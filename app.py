from flask import Flask,render_template,redirect,url_for, flash,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_migrate import Migrate
import os
from datetime import date
app=Flask(__name__) 
basedir = os.path.abspath(os.path.dirname(__file__))

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "app.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db = SQLAlchemy(app)
migrate = Migrate(app, db)

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
                    title="Welcome to Bhutan", image="images/bhutan.jpg", image2="images/interrail-thumb-jpg",
                    description="Relax on the beaches of Goa and experience its vibrant nightlife."),
            City(city="Arunanchal Pradesh", checkin="2025-04-01", checkout="2025-04-10", guests=4,
                    title="Welcome to Arunanchal Pradesh", image="images/ap.jpg", image2="images/hostel1.jpg",
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
                    title="Welcome to Chennai", image="images/chennai.jpeg", image2="images/hostel.jpg",
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


@app.route("/student")
def student_sign_up():
    return render_template("student_sign_up.html")

@app.route("/admin")
def admin_sign_up():
    return render_template("admin_sign_up.html")

@app.route("/staff")
def staff_sign_up():
    return render_template("staff_sign_up.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/forgot_password")
def forgot_password():
    return render_template("forgot_password.html")

@app.route("/change_password")
def change_password():
    return render_template("change_password.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

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

    


