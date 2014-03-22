from flask import Flask, request, redirect
import twilio.twiml
 
app = Flask(__name__)
 
@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming calls with a simple text message."""
 	
    resp = twilio.twiml.Response()
    output = request.Message.get('Body', None)
    resp.message("Woof. " + output)
    #print(request.value.get('Body', None))


    return str(resp)
 
if __name__ == "__main__":
    app.run(debug=True)