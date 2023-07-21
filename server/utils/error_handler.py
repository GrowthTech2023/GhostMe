# Custom error handling
from flask import jsonify

def handle_error(error):
    response = jsonify({'error': str(error)})
    response.status_code = 500  # Internal Server Error
    return response
