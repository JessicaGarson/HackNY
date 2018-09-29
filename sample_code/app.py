from flask import Flask

from nasa import nasa_image

app = Flask(__name__)


@app.route('/', methods=['GET'])
def display():
    picture = nasa_image()
    format_pict = '<h1>Nasa Image of the Day</h1> <img src="{}" alt="" style="width:400px; height:400px;">'.format(
        picture)
    return format_pict

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
