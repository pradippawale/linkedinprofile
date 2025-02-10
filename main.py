from salesforce_connector import get_leads, update_lead
from linkedin_scraper import search_linkedin_profile

def main():
    """Fetch leads, search LinkedIn, and update Salesforce."""
    leads = get_leads()  # Fetch Leads from Salesforce
    for lead in leads:
        name = lead["Name"]
        company = lead["Company"]
        
        print(f"🔍 Searching LinkedIn for: {name} at {company}")
        linkedin_url = search_linkedin_profile(name, company)
        
        if linkedin_url:
            update_lead(lead["Id"], linkedin_url)
            print(f"✅ Updated Salesforce for {name} with {linkedin_url}")
        else:
            print(f"❌ No profile found for {name}.")

if __name__ == "__main__":
    main()
