from flask import Flask
from src.Tags import Tags

app = Flask(__name__)


@app.route('/')
def loadMainPage():
    return 'hello world'


@app.route('/tags')
def loadTagPage():
    tagInfo = Tags()
    return tagInfo.getTagData()


if __name__ == '__main__':
    app.run()
