```python
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")
app = Flask(_name_)

@app.route("/whatsapp", methods=['POST'])
def whatsapp():
    msg = request.form.get('Body')
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": msg}]
    )
    reply = response.choices[0].message.content
    twilio_resp = MessagingResponse()
    twilio_resp.message(reply)
    return str(twilio_resp)

if _name_ == "_main_":
    app.run()
