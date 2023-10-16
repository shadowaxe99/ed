```python
from flask import Blueprint, request, jsonify
from backend.database.models.analytics import Analytics

analytics_bp = Blueprint('analytics_bp', __name__)

@analytics_bp.route('/analytics/', methods=['GET'])
def get_analytics():
    analytics_data = Analytics.query.all()
    return jsonify([data.serialize() for data in analytics_data]), 200

@analytics_bp.route('/analytics/<int:id>', methods=['GET'])
def get_analytics_by_id(id):
    analytics_data = Analytics.query.get(id)
    if analytics_data is None:
        return jsonify({'message': 'Analytics data not found'}), 404
    return jsonify(analytics_data.serialize()), 200

@analytics_bp.route('/analytics/', methods=['POST'])
def create_analytics():
    data = request.get_json()
    new_analytics = Analytics(**data)
    db.session.add(new_analytics)
    db.session.commit()
    return jsonify(new_analytics.serialize()), 201

@analytics_bp.route('/analytics/<int:id>', methods=['PUT'])
def update_analytics(id):
    data = request.get_json()
    analytics_data = Analytics.query.get(id)
    if analytics_data is None:
        return jsonify({'message': 'Analytics data not found'}), 404
    for key, value in data.items():
        setattr(analytics_data, key, value)
    db.session.commit()
    return jsonify(analytics_data.serialize()), 200

@analytics_bp.route('/analytics/<int:id>', methods=['DELETE'])
def delete_analytics(id):
    analytics_data = Analytics.query.get(id)
    if analytics_data is None:
        return jsonify({'message': 'Analytics data not found'}), 404
    db.session.delete(analytics_data)
    db.session.commit()
    return jsonify({'message': 'Analytics data deleted successfully'}), 200
```