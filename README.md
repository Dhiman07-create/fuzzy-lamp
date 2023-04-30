# fuzzy-lamp
This repository contains an implementation of booking without app problem statement of Namma Yatri Open Mobility Challenge 2023


This code defines a Flask app that listens for incoming messages on the /whatsapp endpoint. When a user sends a message containing "book ride", the bot asks the user for the pickup location, dropoff location, date, and time of the ride. The bot then makes a request to the Namma Yatri API to book the ride and sends a response to the user indicating whether the ride was booked successfully or not.

Note that you will need to replace "NAMMA_YATRI_API_KEY" in the code with your actual Namma Yatri API key. Additionally, this code may require additional error handling and user validation to be production-ready.
