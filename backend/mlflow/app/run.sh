# start up model registry
mlflow ui --host 0.0.0.0 --port 5000 &

# register a baseline model from HF
python registry/load_basic_model.py

# start up API
uvicorn main:app --host 0.0.0.0 --port 5678