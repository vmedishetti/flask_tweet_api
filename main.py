from flask import Flask, jsonify, request
import json
app = Flask(__name__)
@app.route('/', methods=['GET'])
def hello_world():
    return "Hello World"
@app.route('/tweets', methods=['GET'])
def get_tweets():
    with open('100tweets.json', 'r', encoding='utf-8') as file:
        tweets = json.load(file)
    return jsonify(tweets)
@app.route('/tweets', methods=['GET'])
def get_filtered_tweets():
    user_name_filter = request.args.get('username', None)

    with open('100tweets.json', 'r', encoding='utf-8') as file:
        tweets = json.load(file)

    if user_name_filter is not None:
        filtered_tweets = [tweet for tweet in tweets if tweet.get('user_name') == user_name_filter]
        return jsonify(filtered_tweets)

    return jsonify(tweets)

    return jsonify(tweets)

@app.route('/tweet/<id_str>', methods=['GET'])
def get_tweet(id_str):
    try:
        with open('100tweets.json', 'r', encoding='utf-8') as file:
            tweets = json.load(file)
        tweet = next((tweet for tweet in tweets if str(tweet.get('id_str', '')) == id_str), None)
        return jsonify(tweet) if tweet else ('', 404)
    except Exception as e:
        return jsonify({"error": str(e)}), 400
if __name__ == '__main__':
    app.run(debug=True)
