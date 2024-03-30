# app.py

from flask import Flask, render_template
from youtube_api import get_videos_by_category

app = Flask(__name__)

@app.route('/')
def index():
    categories = {
        'Film & Animation': get_videos_by_category('1'),
        'Autos & Vehicles': get_videos_by_category('2'),
        'Music': get_videos_by_category('10'),
        # Add more categories as needed
    }
    return render_template('index.html', categories=categories)

if __name__ == '__main__':
    app.run(debug=True)
