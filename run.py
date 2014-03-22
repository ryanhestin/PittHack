from flask import Flask, request, redirect
import twilio.twiml
import fetcher
 
app = Flask(__name__)
 
@app.route("/", methods=['GET', 'POST'])
def respond_to_query():
    """Respond to incoming calls with a simple text message."""
 	
    resp = twilio.twiml.Response()
    body = request.values.get('Body')

   	results = fetcher.getPage(body)


    resp.message(results)


    return str(resp)
 
if __name__ == "__main__":
    app.run(debug=True)