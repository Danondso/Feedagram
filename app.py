import os
from instagram import InstagramAPI
import json
import urllib

from flask import Flask, render_template

app = Flask(__name__)

image_path = 'C:/Users/Anony/Documents/GitHub/Feedagram/templates/images'  # PATH TO IMAGES

credentials_path = 'C:/Users/Anony/Documents/GitHub/Feedagram/json'  # PATH TO CREDENTIALS


def retrieveCredentials():
    try:
        path_to_credentials = os.path.join(credentials_path, 'access_token.json')
        with open(path_to_credentials) as data_file:
            json_payload = json.load(data_file)
            return json_payload
    except Exception as e:
        print(e.args)


def getInstagramMedia(access_token, client_secret, id, count):
    try:
        api = InstagramAPI(access_token=access_token, client_secret=client_secret)
        recent_media, next_ = api.user_recent_media(user_id=id, count=count)
        counter = 0
        media_info = {}
        for media in recent_media:
            file_destination = os.path.join(image_path, 'img' + str(counter) + '.jpg')
            urllib.request.urlretrieve(media.images['standard_resolution'].url, file_destination)
            media_info[counter] = {'image_name': file_destination, 'caption': media.caption}
            counter += 1
        with open('image_info.json', 'w') as outfile.:
            json.dump(media_info.to, outfile, indent=2)
    except Exception as e:
        print(e.args)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/static')
def get_jQuery():
    return app.send_static_file("jquery-1.12.3.min.js")


@app.route('/generate_images')
def generate_images():
    data = retrieveCredentials()
    getInstagramMedia(data[0], "", data[1]["id"], 10)


if __name__ == '__main__':
    app.run()
