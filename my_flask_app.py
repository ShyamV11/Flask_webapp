import os
import requests

from flask import Flask, escape, request
from flask import render_template

# +os.getenv('MY_API_KEY')
my_nasa_api_link = 'https://api.nasa.gov/planetary/apod?api_key=O7LkXYg0LDGFiNqR9BFSOkbLQAGvERRtv7T1a8h6'

app = Flask(__name__)

@app.route('/')
def index_page():
    #name = request.args.get("name", "World")
    r = requests.get(my_nasa_api_link) 
    response = r.json()

    copyright_text = 'Image credits: '
    if 'copyright' in response:
        copyright_text += response['copyright']
    else:
        copyright_text += 'Public Domain'
    
    descriptrion_text = response.get('explanation', 'No description')
    title_text = response.get('title', 'No title')

    media_type = response['media_type']
    media_url = response['url']
    


    return render_template('index.html',
        copyright_text=copyright_text,
        descriptrion_text=descriptrion_text,
        title_text=title_text,
        media_type=media_type,
        media_url=media_url)
	
if __name__ == '__main__':
	app.run()
	
