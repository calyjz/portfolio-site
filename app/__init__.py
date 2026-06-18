import os
from flask import Flask, render_template
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

about = [
    "Hi there! I am a fourth year CS student at the University of Alberta. I'm currently interning at AWS, working on ETL pipelines for query optimization. I also interned at AWS last summer, where I modernized backup workflows for critical RDS databases, gaining hands on experience with backend development, cloud infrastructure, and devops.",
    "My interests revolve around site reliability engineering, backend development, cloud computing and distributed systems. I am always looking for new challenges that will use and deepen my knowledge and skillsets.",
]

experience = [
    {
        "company": "Amazon Web Services",
        "start": "May 2026",
        "title": "Software Development Engineer Intern",
        "description": "Incoming summer 2026"
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


@app.route('/')
def index():
    return render_template('index.html', title="Caly Zheng", url=os.getenv("URL"),
                           about=about, experience=experience, projects=projects)
