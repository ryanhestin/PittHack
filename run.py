from flask import Flask, request, redirect
import twilio.twiml
import fetcher
 
app = Flask(__name__)
 
@app.route("/", methods=['GET', 'POST'])
def respond_to_query():
    """Respond to incoming calls with a simple text message."""
 	
    resp = twilio.twiml.Response()
    body = request.values.get('Body')

    if body[0:3] == "help" or body[0:3] == "Help" or body[0:3] == "HELP":
        resp.message("Wikter Commands:\n-Type any series of words to search wikipedia for info\n-Type any search then \"-<0-20>\" to get more info on the topic\n-Type \"@<twitter_handle>\" to get the latest tweet from any twitter handle\n-Type \"@<twitter_handle> -<1-9>\" to get different tweets")
        return str(resp)

    if body[0] == "@":
        results = fetcher.getTweet(body[1:])
    else:
        results = fetcher.getPage(body)

    resp.message(results)

    return str(resp)
 
if __name__ == "__main__":
    app.run(debug=True)