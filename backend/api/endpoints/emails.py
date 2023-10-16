```python
from flask import Blueprint, request, jsonify
from backend.database.models.email import Email
from backend.email_automation.email import send_email

emails = Blueprint('emails', __name__)

@emails.route('/api/emails/', methods=['POST'])
def create_email():
    data = request.get_json()
    new_email = Email(data)
    send_email(new_email)
    return jsonify({'message': 'Email sent successfully'}), 200

@emails.route('/api/emails/<email_id>', methods=['GET'])
def get_email(email_id):
    email = Email.query.get(email_id)
    if not email:
        return jsonify({'message': 'Email not found'}), 404
    return jsonify(email.serialize()), 200

@emails.route('/api/emails/<email_id>', methods=['PUT'])
def update_email(email_id):
    data = request.get_json()
    email = Email.query.get(email_id)
    if not email:
        return jsonify({'message': 'Email not found'}), 404
    email.update(data)
    return jsonify({'message': 'Email updated successfully'}), 200

@emails.route('/api/emails/<email_id>', methods=['DELETE'])
def delete_email(email_id):
    email = Email.query.get(email_id)
    if not email:
        return jsonify({'message': 'Email not found'}), 404
    email.delete()
    return jsonify({'message': 'Email deleted successfully'}), 200
```