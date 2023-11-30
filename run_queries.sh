curl -X POST -d '{"text": "this is something a person would write"}' http://localhost:8000/detect
curl -X GET http://localhost:8000/ping
curl -X POST -d '{"text": "this is something a person would write", "is_correct": false, "prediction": 0.8}' http://localhost:8000/feedback