from flask import Flask, request, jsonify
from salesforce_connector import update_lead
from linkedin_scraper import search_linkedin_profile

app = Flask(__name__)

@app.route('/')
def home():
    return "🚀 Flask API is running!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    lead_id = data.get('leadId')
    name = data.get('name')
    company = data.get('company')

    if not lead_id or not name or not company:
        return jsonify({"error": "Missing required data"}), 400

    print(f"🔍 Searching LinkedIn for: {name} at {company}")
    linkedin_url = search_linkedin_profile(name, company)

    if linkedin_url:
        print(f"✅ Found LinkedIn URL: {linkedin_url}")
        update_lead(lead_id, linkedin_url)  # Update Salesforce
        return jsonify({"message": "Lead updated successfully", "linkedin_url": linkedin_url}), 200
    else:
        print("❌ No profile found")
        return jsonify({"message": "LinkedIn profile not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
