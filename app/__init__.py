import os
import json
from flask import Flask, render_template, url_for
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

about = [
    "Hi there! I am a fourth year CS student at the University of Alberta. I'm currently interning at AWS, working on ETL pipelines for query optimization. I also interned at AWS last summer, where I modernized backup workflows for critical RDS databases, gaining hands on experience with backend development, cloud infrastructure, and devops.",
    "My interests revolve around site reliability engineering, backend development, cloud computing and distributed systems. I am always looking for new challenges that will use and deepen my knowledge and skillsets.",
]

education = [
    {
        "institution": "University of Alberta",
        "start": "Sept 2022",
        "degree": "Bachelor of Science, Computing Science",
        "description": "Expected graduation 2027"
    }
]

experience = [
    {
        "company": "Amazon Web Services",
        "start": "May 2026",
        "title": "Software Development Engineer Intern",
        "description": "Developing S3Tables Datalake with ETL pipelines to optimize query performance"
    },
    {
        "company": "Amazon Web Services",
        "start": "May 2025",
        "title": "Software Development Engineer Intern",
        "description": "Modernized db backup workflows for critical RDS databases"
    },
    {
        "company": "Canadian Space Agency",
        "start": "Sept 2024",
        "title": "Full Stack Developer Intern",
        "description": "Developed an internal booking system, synchronizing events with Microsoft Calendar"
    },
    {
        "company": "Nanostics",
        "start": "May 2024",
        "title": "Software Developer Intern",
        "description": "Created a customizable Python based GUI for training machine learning models on sensitive health data"
    }
]

projects = [
    {
        "title": "1st Place - Production Engineering Hackathon",
        "description": "Productionized a URL shortener, scaling to 1100+ users with Redis caching and Nginx load balancing.",
        "tags": ["reliability", "scalability", "infra"],
        "image": "pehackathon.png",
        "link": "https://github.com/Five-Nines-Cub/MLH-PE-Hackathon-2026"
    },
    {
        "title": "HTTP Load Balancer",
        "description": "A layer 7 load balancer in Go featuring weighted least connections routing, dynamic thread pool autoscaling, and real-time health checking.",
        "tags": ["HTTP", "Go", "concurrency"],
        "image": "loadbalancer.png",
        "link": "https://github.com/calyjz/load-balancer"
    },
    {
        "title": "Map Reduce",
        "description": "Built a MapReduce library in C utilizing POSIX threads and synchronization primitives.",
        "tags": ["distributed systems", "POSIX", "C"],
        "image": "mapreduce.png",
        "link": "https://github.com/calyjz/map-reduce"
    },
    {
        "title": "Branch Predictor",
        "description": "Built a perceptron branch predictor in RISC-V Assembly with binary instrumentation in RARS.",
        "tags": ["CompArch", "ML", "assembly"],
        "image": "branchpredictor.png",
        "link": "https://github.com/calyjz/perceptron-predictor"
    },
    {
        "title": "Project R",
        "description": "A roguelike game with fast-paced combat, replay driven progression, and a handcrafted story.",
        "tags": ["unity", "game dev", "SDLC"],
        "image": "projectr.jpg",
        "link": "https://github.com/calyjz/Project-R"
    },
    {
        "title": "Ada's Team Website",
        "description": "The official website for a women in tech student group, built using React and TailwindCSS.",
        "tags": ["react", "web dev", "full stack"],
        "image": "adasteam.png",
        "link": "https://github.com/adasdevelopers/adas-team-website"
    },
    {
        "title": "Syzygy Events",
        "description": "An Android event lottery app with QR code entry, role based access, real time updates, and waitlisting.",
        "tags": ["android", "testing", "OOP"],
        "image": "syzygyevents.png",
        "link": ""
    }
]


hobbies = [
    {
        "name": "Soccer",
        "description": "I play casually and referee for Alberta Youth Soccer.",
        "image": "soccer.webp"
    },
    {
        "name": "Crocheting",
        "description": "I love bringing ideas to life stitch by stitch especially for handmade gifts.",
        "image": "crochet.webp"
    },
    {
        "name": "Photography",
        "description": "Learning to capture moments with my new digital camera.",
        "image": "photography.png"
    }
]


locations = [
    {"city": "Beijing", "country": "China", "lat": 39.9042, "lng": 116.4074},
    {"city": "Shanghai", "country": "China", "lat": 31.2304, "lng": 121.4737},
    {"city": "Los Angeles", "country": "USA", "lat": 34.0522, "lng": -118.2437},
    {"city": "Chicago", "country": "USA", "lat": 41.8781, "lng": -87.6298},
    {"city": "Philadelphia", "country": "USA", "lat": 39.9526, "lng": -75.1652},
    {"city": "Seattle", "country": "USA", "lat": 47.6062, "lng": -122.3321},
    {"city": "Edmonton", "country": "Canada", "lat": 53.5461, "lng": -113.4938},
    {"city": "Calgary", "country": "Canada", "lat": 51.0447, "lng": -114.0719},
    {"city": "Vancouver", "country": "Canada", "lat": 49.2827, "lng": -123.1207},
    {"city": "Victoria", "country": "Canada", "lat": 48.4284, "lng": -123.3656},
    {"city": "Tofino", "country": "Canada", "lat": 49.1531, "lng": -125.9066},
    {"city": "Toronto", "country": "Canada", "lat": 43.6532, "lng": -79.3832},
    {"city": "Montreal", "country": "Canada", "lat": 45.5017, "lng": -73.5673},
    {"city": "Quebec City", "country": "Canada", "lat": 46.8139, "lng": -71.2080},
    {"city": "Ottawa", "country": "Canada", "lat": 45.4215, "lng": -75.6972},
    {"city": "Halifax", "country": "Canada", "lat": 44.6488, "lng": -63.5752},
    {"city": "Saskatchewan", "country": "Canada", "lat": 50.4452, "lng": -104.6189},
]


@app.context_processor
def inject_nav():
    return {
        'nav_pages': [
            {'name': 'Home', 'url': url_for('index'), 'icon': 'fa-solid fa-house'},
            {'name': 'Hobbies', 'url': url_for('hobbies_page'), 'icon': 'fa-solid fa-heart'},
            {'name': 'Map', 'url': url_for('map_page'), 'icon': 'fa-solid fa-earth-americas'},
        ]
    }


@app.route('/')
def index():
    return render_template('index.html', title="Caly Zheng", url=os.getenv("URL"),
                           about=about, education=education, experience=experience,
                           projects=projects, hobbies=hobbies)


@app.route('/map')
def map_page():
    return render_template('map.html', title="Travel Map", url=os.getenv("URL"),
                           locations=locations, locations_json=json.dumps(locations))


@app.route('/hobbies')
def hobbies_page():
    return render_template('hobbies.html', title="Hobbies", url=os.getenv("URL"),
                           hobbies=hobbies)
