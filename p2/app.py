from flask import Flask, jsonify, request
import os
import logging

# Create Flask app
app = Flask(__name__)

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Required environment variable
API_ENV = os.getenv("API_ENV")

# Root route and health check
@app.route("/", methods=["GET"])
def home():
    app.logger.info("Home endpoint accessed")

    return jsonify({
        "message": "Mini DevOps API running"
    }), 200


# Example POST route
@app.route("/echo", methods=["POST"])                                       # defines a route that listens for POST requests at /echo 
def echo():
    data = request.json                                                     # retrieves JSON data from request body

    app.logger.info(f"Echo endpoint received data: {data}")                 # logs the received data

    return jsonify({                                                        # returns the received data back to the client
        "received": data                                                    # echoes back the data sent in the request
    }), 200


########################
# Route that checks environment variable
########################
@app.route("/env", methods=["GET"])
def check_env():

    if not API_ENV:
        app.logger.error("API_ENV variable is missing")

        return jsonify({
            "error": "API_ENV environment variable not set"
        }), 500

    return jsonify({
        "API_ENV": API_ENV
    }), 200


########################
# Run Flask app
########################
if __name__ == "__main__":
    app.logger.info("Starting Flask app")

    app.run(
        host="0.0.0.0",
        port=5000
    )