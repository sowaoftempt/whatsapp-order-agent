from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def whatsapp_webhook():
    try:
        # Capture raw json payload securely
        data = request.get_json(force=True)
        
        print("\n=================================")
        print(" INCOMING WHATSAPP PAYLOAD LOG")
        print("=================================")
        print(json.dumps(data, indent=4))
        print("=================================\n")
        
        return jsonify({"status": "success", "message": "Payload received"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

if __name__ == '__main__':
    # Force localized hosting on port 5000
    app.run(debug=True, host='127.0.0.1', port=5000)