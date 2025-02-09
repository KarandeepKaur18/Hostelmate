from flask import Flask,render_template,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/student")
def student_sign_up():
    return render_template("student_sign_up.html")

@app.route("/admin")
def admin_sign_up():
    return render_template("admin_sign_up.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/faq")
def faq():
    return render_template("faq.html")

@app.route("/travel")
def travel():
    return render_template("travel.html")




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



if __name__ == '__main__':
    app.run(debug=True)

    


