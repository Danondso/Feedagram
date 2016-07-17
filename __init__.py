import os
import json
import urllib
from instagram import InstagramAPI
from flask import Flask, render_template, jsonify, request, current_app
from instagram.bind import InstagramAPIError

app = Flask(__name__)

image_path = '/var/www/feedagram/feedagram/static/images'  # PATH TO IMAGES

json_path = '/var/www/feedagram/feedagram/json'  # PATH TO CREDENTIALS

image_html_path = '../static/images/'  # IMAGE PATH HTML WILL READ


def retrieve_credentials():
    try:
        #print ('Getting credentials')
        path_to_credentials = os.path.join(json_path, 'access_token.json')
        with open(path_to_credentials) as data_file:
            json_payload = json.load(data_file)
        #    print('got credentials')
            return json_payload
    except Exception as e:
        print(e)


def get_instagram_media(access_token, client_secret, id, count):
    try:
        api = InstagramAPI(access_token=access_token, client_secret=client_secret)
        recent_media, _next = api.user_recent_media(user_id=id, count=count)
        metadata = {}
        counter = 0
        for media in recent_media:
       #     counter_id = str(counter)
        #    existing_images = get_json()
        #    if existing_images.counter_id.id != (media.id + '.jpg'):
            file_destination = os.path.join(image_path, str(media.id) + '.jpg' )
            metadata_destination_path = os.path.join(image_html_path, str(media.id) + '.jpg' )
            urllib.request.urlretrieve(media.images['standard_resolution'].url, file_destination)
            metadata[counter] = {'image_name': metadata_destination_path, 'caption': has_caption(media.caption), 'id':(str(media.id) + '.jpg')}
       #     else:
         #       metadata[counter] = {'image_name': existing_images.counter_id.image_name, 'caption': existing_images.counter_id.caption, 'id':existing_images.counter_id.id}
            counter += 1
        write_metadata(metadata)
    except InstagramAPIError as e:
        print (e)


def has_caption(caption):
    return '' if caption is None else caption.text


def write_metadata(metadata):
    media_info = {'metadata': metadata}
    info_path = os.path.join(json_path, 'image_info.json')
    with open(info_path, 'w') as outfile:
        json.dump(media_info, outfile, indent=2)


def get_json():
    image_info = os.path.join(json_path, 'image_info.json')
    try:
        with open(image_info) as image_info_file:
            json_payload = json.load(image_info_file)
            return json_payload
    except Exception as e:
        print(e)


@app.route('/get_image_carousel')
def get_image_metadata():
    try:
        data = retrieve_credentials()
        get_instagram_media(data[0], "", data[1]["id"], 10)
        return jsonify(result=get_json())
    except Exception as e:
        print(e)
    return 'OK'

@app.route('/')
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
