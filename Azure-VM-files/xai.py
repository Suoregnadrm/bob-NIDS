import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
import joblib
import shap
from flask import Flask, render_template, jsonify
from scapy.all import rdpcap

app = Flask(__name__)


model = joblib.load("XGB.joblib")

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_packets')
def get_packets():
    packets = rdpcap("capture.pcap")
    packet_data = [str(packet) for packet in packets]
    return jsonify(packet_data)


@app.route('/get_severity')
def get_severity():
    df = pd.read_csv("update_capture_df.csv")

    le = LabelEncoder()
    for column in df.select_dtypes(include=['object']).columns:
        df[column] = le.fit_transform(df[column])

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(df)

    pred = model.predict(X_scaled)

    pred = pred.astype(object)
    replace_dict = {0: "benign", 1: "bruteforce", 2: "ddos", 3: "normal", 4: "sqlattack"}
    for old_value, new_value in replace_dict.items():
        pred[pred == old_value] = new_value
    severity_data = pred.tolist()
    return jsonify(severity_data)

#@app.route('/get_shap')
#def get_shap():
    #df = pd.read_csv("update_capture_df.csv")

    #le = LabelEncoder()
    #for column in df.select_dtypes(include=['object']).columns:
        #df[column] = le.fit_transform(df[column])

    #scaler = StandardScaler()
    #X_scaled = scaler.fit_transform(df)

    #pred = model.predict(X_scaled)
    #explainer = shap.Explainer(model, X_scaled)

    #shap_values = explainer(X_scaled)
    #shap_values_mean = shap_values.values.mean(axis=0)

    #print(shap_values)
    #print(shap_values_mean)
    #return jsonify(shap_values_mean.tolist())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
