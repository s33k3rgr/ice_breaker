import os
import requests
from dotenv import load_dotenv

load_dotenv()

def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """
    Scrape information from LinkedIn profiles,
    Manually scrape the information from the LinkedIn profile
    """

    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/s33k3rgr/f8b30c43ef98d904ae7f111762105933/raw/5e4abb17a7467d34a028dc33c66dcab2980b70a6/vaios-argyropoulos-scraping.json"
        response = requests.get(
            linkedin_profile_url,
            timeout=10,
        )
        #
        data = response.json().get("person")

    else:
        api_endpoint = "http://api.scrapin.io/enrichment/profile"
        params = {
            "apikey": os.environ["SCRAPIN_API_KEY"],
            "linkedInUrl": linkedin_profile_url,
        }
        response = requests.get(
            api_endpoint,
            params=params,
            timeout=10
        )
        data = response.json().get("person")

    
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "","", None) and k not in ["certifications"]
    }

    return data



if __name__ == "__main__":
    print(
        scrape_linkedin_profile(
            linkedin_profile_url="https://www.linkedin.com/in/vaios-argiropoulos-54a496361/",
            mock=True
        )
    )
