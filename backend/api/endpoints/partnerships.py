```python
from flask import Blueprint, request, jsonify
from backend.database.models.partnership import Partnership
from backend.matching_algorithm.matching import match_brands

partnerships = Blueprint('partnerships', __name__)

@partnerships.route('/partnerships/', methods=['POST'])
def create_partnership():
    data = request.get_json()
    influencer_id = data.get('influencer_id')
    brand_id = data.get('brand_id')
    partnership = Partnership(influencer_id=influencer_id, brand_id=brand_id)
    partnership.save()
    return jsonify(partnership.to_dict()), 201

@partnerships.route('/partnerships/<int:id>', methods=['GET'])
def get_partnership(id):
    partnership = Partnership.query.get(id)
    if partnership is None:
        return jsonify({'error': 'Partnership not found'}), 404
    return jsonify(partnership.to_dict()), 200

@partnerships.route('/partnerships/<int:id>', methods=['PUT'])
def update_partnership(id):
    data = request.get_json()
    partnership = Partnership.query.get(id)
    if partnership is None:
        return jsonify({'error': 'Partnership not found'}), 404
    partnership.update(data)
    return jsonify(partnership.to_dict()), 200

@partnerships.route('/partnerships/<int:id>', methods=['DELETE'])
def delete_partnership(id):
    partnership = Partnership.query.get(id)
    if partnership is None:
        return jsonify({'error': 'Partnership not found'}), 404
    partnership.delete()
    return jsonify({'message': 'Partnership deleted successfully'}), 200

@partnerships.route('/partnerships/match', methods=['POST'])
def match_partnership():
    data = request.get_json()
    influencer_id = data.get('influencer_id')
    matched_brands = match_brands(influencer_id)
    return jsonify({'matched_brands': matched_brands}), 200
```