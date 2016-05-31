import os
from instagram import InstagramAPI
# from pip._vendor.requests.packages.urllib3 import request

import json
import urllib

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

image_loaded = False

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
        metadata = {}
        for media in recent_media:
            file_destination = os.path.join(image_path, 'img' + str(counter) + '.jpg')
            urllib.request.urlretrieve(media.images['standard_resolution'].url, file_destination)
            metadata[counter] = {'image_name': file_destination, 'caption': has_caption(media.caption)}
            counter += 1
        write_metadata(metadata)

    except Exception as e:
        print(e.args)
    return


def has_caption(caption):
    if caption is None:
        return ''
    return caption.text


def write_metadata(metadata):
    media_info = {'metadata': metadata}
    with open('image_info.json', 'w') as outfile:
        json.dump(media_info, outfile, indent=2)
    image_loaded = True


@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/static')
def get_jQuery():
    return app.send_static_file("jquery-1.12.4.min.js")


@app.route('/generate_images')
def generate_images():
    data = retrieveCredentials()
    getInstagramMedia(data[0], "", data[1]["id"], 10)
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
