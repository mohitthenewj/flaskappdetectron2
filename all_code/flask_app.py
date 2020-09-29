from pull_blob import pull_main
from ffmpeg_main import pre_process
from odmainutil_batch import object_d2
from odmainutil_batch import load_model

import os
import requests
from flask import Flask,request
from flask_caching import Cache





app = Flask(__name__)
app.config['CACHE_TYPE'] = 'simple'

cache = Cache()
cache.init_app(app)

@cache.cached(timeout = 1000000000)
def model():
    return load_model()

@app.route("/", methods=['GET','POST'])
def app_main():

    os.system('rm /app/*mp4')
    message = request.get_json(force=True)
    video_id = message["ID"]
    pull_main(video_id=video_id)
    pre_process(video_id=video_id)
    data = object_d2(video_id= f'{video_id}_', model= model())
    return data


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

