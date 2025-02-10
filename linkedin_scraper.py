# from googlesearch import search

# def search_linkedin_profile(name, company):
#     query = f'site:linkedin.com/in "{name}" "{company}"'
#     search_results = search(query, num_results=1)  # Use `num_results` instead of `num`
    
#     for result in search_results:
#         return result  # Return the first search result (LinkedIn profile URL)
    
#     return None  # Return None if no results found
from googlesearch import search

def search_linkedin_profile(name, company):
    query = f'site:linkedin.com/in "{name}" "{company}"'
    search_results = search(query, num_results=1)

    for result in search_results:
        return result  # Return first result

    return None  # No result found
