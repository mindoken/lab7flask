from __init__ import api
from flask import jsonify
from utils import get_games
from flask_restx import Resource, reqparse

ns = api.namespace('/', description='Steam games')

parser = reqparse.RequestParser()
parser.add_argument('count', type=int, required=True, help="Число игр, которые нужно вывести:")
parser.add_argument('shuffle', type=bool, help="Перемешать игры:")
parser_copy = parser
@ns.route('/get-games/by-count')
class DailyHoroscopeAPI(Resource):
    @ns.doc(parser=parser_copy)
    def get(self):
        args = parser.parse_args()
        count = args.get('count')
        shuffle = args.get('shuffle')
        data = get_games(count,shuffle)
        return jsonify(Games=data,Totalgames=count)