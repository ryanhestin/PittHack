from flask import Flask, request, redirect
import twilio.twiml
import fetcher
 
app = Flask(__name__)
 
@app.route("/", methods=['GET', 'POST'])
def respond_to_query():
    """Respond to incoming calls with a simple text message."""
 	
    resp = twilio.twiml.Response()
    body = request.values.get('Body')

    print(body)

    if '!commands' in body:
        resp.message("Wikter Commands:\n-Type any series of words to search wikipedia for info\n-Type any search then \"-<0-20>\" to page through resulting sentences\n-Type \"@<twitter_handle>\" to get the latest tweet from any twitter handle\n-Type \"@<twitter_handle> -<2-20>\" to earlier tweets\n-Type a math or general knowledge in the form \"<query> -w\" to try WolframAlpha")
        return str(resp)

    if body[0] == "@":
        results = fetcher.getTweet(body[1:])
    elif body[-2:] == "-w":
        results = fetcher.wolframRules(body[:-3].lower())
    else:
        results = fetcher.getPage(body.lower())

    resp.message(results)

    return str(resp)
 
if __name__ == "__main__":
    app.run(debug=True)