```python
from flask import Blueprint, request, jsonify
from backend.database.models.brand import Brand

brands = Blueprint('brands', __name__)

@brands.route('/api/brands/', methods=['GET'])
def get_brands():
    brands = Brand.query.all()
    return jsonify([brand.serialize() for brand in brands]), 200

@brands.route('/api/brands/<int:brand_id>', methods=['GET'])
def get_brand(brand_id):
    brand = Brand.query.get(brand_id)
    if brand is None:
        return jsonify({'message': 'Brand not found'}), 404
    return jsonify(brand.serialize()), 200

@brands.route('/api/brands/', methods=['POST'])
def create_brand():
    data = request.get_json()
    new_brand = Brand(name=data['name'], industry=data['industry'], values=data['values'])
    db.session.add(new_brand)
    db.session.commit()
    return jsonify(new_brand.serialize()), 201

@brands.route('/api/brands/<int:brand_id>', methods=['PUT'])
def update_brand(brand_id):
    data = request.get_json()
    brand = Brand.query.get(brand_id)
    if brand is None:
        return jsonify({'message': 'Brand not found'}), 404
    brand.name = data['name']
    brand.industry = data['industry']
    brand.values = data['values']
    db.session.commit()
    return jsonify(brand.serialize()), 200

@brands.route('/api/brands/<int:brand_id>', methods=['DELETE'])
def delete_brand(brand_id):
    brand = Brand.query.get(brand_id)
    if brand is None:
        return jsonify({'message': 'Brand not found'}), 404
    db.session.delete(brand)
    db.session.commit()
    return jsonify({'message': 'Brand deleted'}), 200
```