from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf

# Initialize Flask app
app = Flask(__name__)

# Load the Keras model
model = tf.keras.models.load_model("group1-shard1of1.bin")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get input data from request
        data = request.get_json()
        input_data = np.array(data["data"]).reshape(1, -1)  # Reshape if needed

        # Get model prediction
        prediction = model.predict(input_data)

        # Convert to list for JSON response
        return jsonify({"prediction": prediction.tolist()})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
