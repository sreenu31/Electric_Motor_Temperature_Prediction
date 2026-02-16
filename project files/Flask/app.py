import numpy as np
from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

model = joblib.load("model.save")
transform = joblib.load("transform.save")

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/manual')
def manual():
    return render_template('Manual_predict.html')

@app.route('/sensor')
def sensor():
    return render_template('Sensor_predict.html')

@app.route('/y_predict', methods=['POST'])
def y_predict():
    data = [float(x) for x in request.form.values()]
    data = np.array(data).reshape(1, -1)
    data = transform.transform(data)
    prediction = model.predict(data)

    return render_template(
        'Manual_predict.html',
        prediction_text=f"Permanent Magnet Surface Temperature : {prediction[0]:.3f}"
    )

if __name__ == "__main__":
    app.run(debug=True)
