import os
import requests


def scrape_linkedin_profile(linkedin_profile_url: str):
    """scrape inforamtion from LinkedIn profiles,
    Manually scrape the information from the LinkedIn profile
    """

    # api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    # header_dic = {"Authorization" f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}
    #
    # response = requests.get(
    #     api_endpoint, params={"url": linkedin_profile_url}, headers=header_dic
    # )

    api_endpoint = "https://gist.githubusercontent.com/jeetbafna/be58379a446f9b85b6bef7d6732ce8de/raw/f355c9ade1fc6b91602dfedb3f2397ee248fff51/jeetbafna.json"

    response = requests.get(api_endpoint)

    data = response.json()

    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }

    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data
