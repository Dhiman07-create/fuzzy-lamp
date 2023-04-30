from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import requests
import json

app = Flask(__name__)

@app.route('/whatsapp', methods=['POST'])
def whatsapp():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    
    if 'book ride' in incoming_msg:
        # Get the ride details from the user
        resp.message("Please provide the pickup location, dropoff location, date and time of the ride in the format: \nPickup Location: <location> \nDropoff Location: <location> \nDate: <date> \nTime: <time>")
    elif 'pickup location' in incoming_msg:
        pickup_location = incoming_msg.split(":")[1].strip()
        resp.message("Please provide the dropoff location")
    elif 'dropoff location' in incoming_msg:
        dropoff_location = incoming_msg.split(":")[1].strip()
        resp.message("Please provide the date of the ride")
    elif 'date' in incoming_msg:
        ride_date = incoming_msg.split(":")[1].strip()
        resp.message("Please provide the time of the ride")
    elif 'time' in incoming_msg:
        ride_time = incoming_msg.split(":")[1].strip()
        
        # Make a request to Namma Yatri API to book the ride
        api_key = "NAMMA_YATRI_API_KEY"
        api_url = f"https://api.nammayatri.com/v1/rides/book?key={api_key}"
        payload = {
            "pickup_location": pickup_location,
            "dropoff_location": dropoff_location,
            "ride_date": ride_date,
            "ride_time": ride_time
        }
        response = requests.post(api_url, json=payload)
        response_text = json.loads(response.text)
        if response_text['status'] == 'success':
            resp.message("Your ride has been booked successfully!")
        else:
            resp.message("Sorry, we could not book your ride. Please try again later.")
    else:
        resp.message("Please send 'book ride' to book a ride with Namma Yatri.")
        
    return str(resp)

if __name__ == '__main__':
    app.run(debug=True)
