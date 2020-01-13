from flask import jsonify, Blueprint, request

from .models import  Link
from url_shortener import  db


api = Blueprint('api', __name__)


@api.route('/generate', methods=['POST'])
def generate_link():
    json_data = request.get_json()
    
    if not json_data:
        return jsonify({
            'message': 'json data containing original url must be parsed',
            'results': None
        })
        
    original_url = json_data['original_link']
    new_link = Link(original_url=original_url)
    
    db.session.add(new_link)
    db.session.commit()
    
    return jsonify({
        'message': 'successful',
        'results': {
                'original_link': original_url,
                'new_link': new_link.short_url
            }
        })
