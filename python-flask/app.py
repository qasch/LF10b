from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Service(Resource):
    def get(self):
        return {
            'services': [
                    'Docker',
                    'Debuggen',
                    'Yaml',
                    'Kaffe kochen'
                    ]
                }

api.add_resource(Service, '/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

