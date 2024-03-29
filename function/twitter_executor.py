import json
import os

import requests
from dotenv import load_dotenv
from interface.terminal import pretty_print_conversation
from requests_oauthlib import OAuth1Session

load_dotenv()
# In your terminal please set your environment variables by running the following lines of code.
# export 'CONSUMER_KEY'='<your_consumer_key>'
# export 'CONSUMER_SECRET'='<your_consumer_secret>'

consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
# def get_verifier():
#     # Be sure to add replace the text of the with the text you wish to Tweet. You can also add parameters to post polls, quote Tweets, Tweet with reply settings, and Tweet to Super Followers in addition to other features.

# def init_verifier():
#     # Get request token
#     request_token_url = "https://api.twitter.com/oauth/request_token?oauth_callback=oob&x_auth_access_type=write"
#     oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)

#     try:
#         fetch_response = oauth.fetch_request_token(request_token_url)
#     except ValueError:
#         print(
#             "There may have been an issue with the consumer_key or consumer_secret you entered."
#         )

#     resource_owner_key = fetch_response.get("oauth_token")
#     resource_owner_secret = fetch_response.get("oauth_token_secret")
#     # print("Got OAuth token: %s" % resource_owner_key)

#     # Get authorization
#     base_authorization_url = "https://api.twitter.com/oauth/authorize"
#     authorization_url = oauth.authorization_url(base_authorization_url)
#     pretty_print_conversation(messages=None, message="Please go here and authorize: %s" % authorization_url)
#     verifier = input("Paste the PIN here: ")
#     return authorization_url, resource_owner_key, resource_owner_secret
# def attach_verifier(authorization_url, resource_owner_key, resource_owner_secret, verifier):

#     # Get the access token
#     access_token_url = "https://api.twitter.com/oauth/access_token"
#     oauth = OAuth1Session(
#         consumer_key,
#         client_secret=consumer_secret,
#         resource_owner_key=resource_owner_key,
#         resource_owner_secret=resource_owner_secret,
#         verifier=verifier,
#     )
#     oauth_tokens = oauth.fetch_access_token(access_token_url)

#     access_token = oauth_tokens["oauth_token"]
#     access_token_secret = oauth_tokens["oauth_token_secret"]


#     return access_token, access_token_secret
def post_twitter(text, access_token, access_token_secret, pic=None):
    # Make the request
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret,
    )
    payload = {"text": text}
    # Making the request
    response = oauth.post(
        "https://api.twitter.com/2/tweets",
        json=payload,
    )

    if response.status_code != 201:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )

    pretty_print_conversation(
        messages=None, message="Response code: {}".format(response.status_code)
    )

    # Saving the response as JSON
    json_response = response.json()
    # print(json.dumps(json_response, indent=4, sort_keys=True))


def make_post_twitter(text, pic=None):
    url = "https://replyrocket-backend.onrender.com/twitter/post"
    data = {"text": text}
    try:
        if pic is not None:
            with open(pic, "rb") as file:
                files = {"image": file}
                response = requests.post(url, files=files, data=data, timeout=10000)
                if response.status_code == 200:
                    return "Post successful!"
                else:
                    return f"Failed to post. Status code: {response.status_code}"
        else:
            response = requests.post(url, data=data, timeout=10000)
            if response.status_code == 200:
                return "Post successful!"
            else:
                return f"Failed to post. Status code: {response.status_code}"
    except Exception as e:
        return f"An error occurred: {str(e)}"


# if __name__=="__main__":
#     text="Test alert!"
#     print(make_post_twitter(text))
