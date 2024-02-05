import os

import openai
from dotenv import load_dotenv
from flask import Flask, jsonify, request, session
from flask_cors import CORS
from requests_oauthlib import OAuth1Session

from function.linkedin_executor import make_post_linkedin
from function.twitter_executor import post_twitter
from main import chatbot, init_chat

load_dotenv()
client = openai

app = Flask(__name__)
CORS(app)
app.secret_key = os.urandom(24)
app.config["TEMP"] = "/temp"

consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")

def create_oauth_session(token=None, token_secret=None, verifier=None):
    return OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=token,
        resource_owner_secret=token_secret,
        verifier=verifier,
    )

@app.route("/")
def home():
    return {"Message": "Hello World"}

@app.route("/chat/init", methods=["GET"])
def init_chat_call():
    messages_str = init_chat()
    return {"messages": messages_str}

@app.route("/chat/generate", methods=["POST"])
def generate_response():
    try:
        response = request.json
        if messages := response.get("messages"):
            if response := chatbot(messages):
                return jsonify({"response": response}), 200
            else:
                return jsonify({"error": "Failed to generate response"}), 500
        else:
            return jsonify({"error": "Missing prompt parameter"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/upload/image", methods=["POST"])
def upload_image():
    file = request.files.get("image")
    if not file:
        return jsonify({"error": "Image is required"}), 400
    filename = file.filename
    file_path = os.path.join(app.config["TEMP"], filename)
    file.save(file_path)
    return jsonify({"response": file_path}), 200

@app.route("/post_linkedin", methods=["POST"])
def call_linkedin():
    try:
        data = request.json
        content = data.get("content")
        image = data.get("image")
        if not content:
            return jsonify({"error": "Missing content for posting on Linkedin"}), 400
        response = make_post_linkedin(content, image) if image else make_post_linkedin(content)
        if response:
            return jsonify({"Response": response}), 200
        else:
            return jsonify({"error": "Internal Server Error"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/twitter/auth/init", methods=["GET"])
def init_twitter_auth():
    request_token_url = "https://api.twitter.com/oauth/request_token?oauth_callback=oob&x_auth_access_type=write"
    oauth = create_oauth_session()
    fetch_response = oauth.fetch_request_token(request_token_url)
    session["resource_owner_key"] = fetch_response.get("oauth_token")
    session["resource_owner_secret"] = fetch_response.get("oauth_token_secret")

    base_authorization_url = "https://api.twitter.com/oauth/authorize"
    authorization_url = oauth.authorization_url(base_authorization_url)
    return jsonify({"authorization_url": authorization_url})

@app.route("/twitter/auth/verify", methods=["POST"])
def complete_twitter_auth():
    verifier = request.json.get("verifier")
    resource_owner_key = session.get("resource_owner_key")
    resource_owner_secret = session.get("resource_owner_secret")

    access_token_url = "https://api.twitter.com/oauth/access_token"
    oauth = create_oauth_session(resource_owner_key, resource_owner_secret, verifier)
    oauth_tokens = oauth.fetch_access_token(access_token_url)

    session["access_token"] = oauth_tokens["oauth_token"]
    session["access_token_secret"] = oauth_tokens["oauth_token_secret"]
    return jsonify({"message": "Authentication successful"})

@app.route("/twitter/post", methods=["POST"])
def post_to_twitter():
    try:
        access_token = session.get("access_token")
        access_token_secret = session.get("access_token_secret")
        if not access_token or not access_token_secret:
            return jsonify({"error": "Authentication required"}), 401
        if tweet_text := request.json.get("text"):
            if response := post_twitter(
                tweet_text, access_token, access_token_secret
            ):
                return jsonify({"response": response}), 200
            else:
                return jsonify({"error": "Failed to generate response"}), 500
        else:
            return jsonify({"error": "Tweet text is required"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
