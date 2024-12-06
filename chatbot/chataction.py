# import json
# import urllib.request

# # Read JSON data from the request body
# json_data = '...'

# url = 'https://drishtis.app/drishti_appointmentbot/api/get_chat_action/'

# try:
#     # Encode JSON data
#     encoded_data = json_data.encode('utf-8')

#     # Set headers
#     headers = {'Content-Type': 'application/json', 'Content-Length': len(encoded_data)}

#     # Create request object
#     req = urllib.request.Request(url, data=encoded_data, headers=headers, method='POST')

#     # Open URL
#     with urllib.request.urlopen(req) as response:
#         # Read response data
#         response_data = response.read().decode('utf-8')

#         # Print response data
#         print(response_data)

# except Exception as e:
#     # Print exception message
#     print(f'Error: {e}')


# from flask import Flask, request, jsonify

# app = Flask(__name__)

# @app.route('/apis/chatbot/chataction', methods=['POST'])
# def chat_action():
#     try:
#         request_data = request.json
#         # Process the request data here

#         # Example response
#         response_data = {"message": "Received data successfully"}
#         return jsonify(response_data), 200
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# if __name__ == '__main__':
#     app.run(debug=True)

import json
import urllib.request
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/send_json_data', methods=['POST'])
def send_json_data():
    try:
        # Read JSON data from the request body
        json_data = request.json

        # Encode JSON data
        encoded_data = json.dumps(json_data).encode('utf-8')

        # Specify the URL to send the request
        url = 'https://drishtis.app/drishti_appointmentbot/api/get_chat_action/'

        # Set headers
        headers = {'Content-Type': 'application/json', 'Content-Length': len(encoded_data)}

        # Create request object
        req = urllib.request.Request(url, data=encoded_data, headers=headers, method='POST')

        # Open URL
        with urllib.request.urlopen(req) as response:
            # Read response data
            response_data = response.read().decode('utf-8')
            return jsonify(response_data), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
