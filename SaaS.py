from flask import Flask, request, jsonify

app = Flask(__name__)
platform_applications = []
saas_subscriptions = []

@app.route('/create_application', methods=['POST'])
def create_application():
   try:
      data = request.json
      app_name = data.get('app_name')
      app_type = data.get('app_type')

      if not all([app_name, app_type]):
         raise ValueError("Invalid data. App name and app type are required.")

      new_application = {"app_name": app_name, "app_type": app_type, "provider": "Dee-coding"}
      platform_applications.append(new_application)

      return jsonify({"message": "Application created successfully", "application": new_application})

   except Exception as e:
      return jsonify({"error": str(e)}), 400

@app.route('/list_applications', methods=['GET'])
def list_applications():
   return jsonify({"applications": platform_applications})

@app.route('/subscribe', methods=['POST'])
def subscribe_to_saas():
   try:
      data = request.json
      app_name = data.get('app_name')

      if not app_name:
         raise ValueError("Invalid data. App name is required.")

      subscription = {"app_name": app_name}
      saas_subscriptions.append(subscription)

      return jsonify({"message": "Subscribed successfully", "subscription": subscription})

   except Exception as e:
      return jsonify({"error": str(e)}), 400

@app.route('/unsubscribe', methods=['POST'])
def unsubscribe_from_saas():
   try:
      data = request.json
      app_name = data.get('app_name')

      if not app_name:
         raise ValueError("Invalid data. App name is required.")

      # Remove the subscription if it exists
      saas_subscriptions[:] = [s for s in saas_subscriptions if s.get('app_name') != app_name]

      return jsonify({"message": "Unsubscribed successfully", "app_name": app_name})

   except Exception as e:
      return jsonify({"error": str(e)}), 400

@app.route('/list_subscriptions', methods=['GET'])
def list_saas_subscriptions():
   return jsonify({"subscriptions": saas_subscriptions})

if __name__ == '__main__':
   app.run(debug=True)
