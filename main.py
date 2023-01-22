from flask import Flask
from flask_restful import Api, Resource
from Regex import exchangecus
app = Flask(__name__)
api = Api(app)
ex13,ex16 ,ex19 = exchangecus() ##get the values from microsoft using the Regex frile function


class ExchangeCu(Resource):
    def get(self):
        return {"exchange2013":ex13,
                "exchange2016":ex16,
                "exchange2019":ex19}


api.add_resource(ExchangeCu, '/exchangecu')
if __name__ == "__main__":
    app.run(debug=True)