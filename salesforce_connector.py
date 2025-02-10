from simple_salesforce import Salesforce
from config import SALESFORCE_USERNAME, SALESFORCE_PASSWORD, SALESFORCE_SECURITY_TOKEN

# Connect to Salesforce
sf = Salesforce(username=SALESFORCE_USERNAME, password=SALESFORCE_PASSWORD, security_token=SALESFORCE_SECURITY_TOKEN)

def get_leads():
    """Fetch leads missing LinkedIn Profile URLs from Salesforce"""
    query = "SELECT Id, Name, Company FROM Lead WHERE LinkedIn_Profile_URL__c = NULL ORDER BY CreatedDate DESC LIMIT 1"
    leads = sf.query(query)
    return leads['records']

def update_lead(lead_id, linkedin_url):
    """Update Salesforce lead with LinkedIn profile URL"""
    sf.Lead.update(lead_id, {'LinkedIn_Profile_URL__c': linkedin_url})
    print(f"✅ Updated Lead {lead_id} with LinkedIn: {linkedin_url}")


# from simple_salesforce import Salesforce

# # Connect to Salesforce
# sf = Salesforce(username="pawalepradip29@curious-raccoon-aivu8m.com", password="@", security_token="0jNlJ25Xld2QJATsdPjLeXOfX")

# def update_lead(lead_id, linkedin_url):
#     sf.Lead.update(lead_id, {"LinkedIn_Profile_URL__c": linkedin_url})
#     print(f"🔄 Updated Lead {lead_id} with LinkedIn URL: {linkedin_url}")
