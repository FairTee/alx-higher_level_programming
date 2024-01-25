#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_me that causes the server to respond
curl -s -X POST 0.0.0.0:5000/catch_me -H "accept: text/plain" -H "Content-Type: application/json" -d '{"message": "You got me!"}'
