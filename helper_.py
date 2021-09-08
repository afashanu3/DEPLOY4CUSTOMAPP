import helper
from flask import Flask, request, Response
import json

application = Flask(__name__)

@application.route('/')
def reading_():
    return 'Reading is fundamental!'

@application.route('/book/new', methods=['POST'])
def add_item():
    # Get item from the POST body
    req_data = request.get_json()
    book = req_data['book']

    # Add item to the list
    res_data = helper.add_to_list(book)

    # Return error if item not added
    if res_data is None:
        response = Response("{'error': 'Item not added - " + book + "'}", status=400 , mimetype='application/json')
        return response

    # Return response
    response = Response(json.dumps(res_data), mimetype='application/json')

    return response

@application.route('/book/finished', methods=['GET'])
def get_item():
    # Get parameter from the URL
    item_name = request.args.get('name')

    # Get items from the helper
    status = helper.get_item(item_name)

    # Return 404 if item not found
    if finished is None:
        response = Response("{'error': 'Item Not Found - %s'}"  % item_name, status=404 , mimetype='application/json')
        return response

    # Return status
    res_data = {
        'finished': finished
    }

    response = Response(json.dumps(res_data), status=200, mimetype='application/json')
    return response

@application.route('/book/update', methods=['PUT'])
def update_status():
    # Get item from the POST body
    req_data = request.get_json()
    book = req_data['book']
    finished = req_data['finished']

    # Update item in the list
    res_data = helper.update_status(book, finished)

    # Return error if the status could not be updated
    if res_data is None:
        response = Response("{'error': 'Error updating item - '" + book + ", " + finished   +  "}", status=400 , mimetype='application/json')
        return response

    # Return response
    response = Response(json.dumps(res_data), mimetype='application/json')

    return response

@application.route('/book/remove', methods=['DELETE'])
def delete_item():
    # Get item from the POST body
    req_data = request.get_json()
    book = req_data['book']

    # Delete item from the list
    res_data = helper.delete_item(book)

    # Return error if the item could not be deleted
    if res_data is None:
        response = Response("{'error': 'Error deleting item - '" + item +  "}", status=400 , mimetype='application/json')
        return response

    # Return response
    response = Response(json.dumps(res_data), mimetype='application/json')

    return response