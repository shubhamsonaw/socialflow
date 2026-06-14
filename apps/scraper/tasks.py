import requests
from celery import shared_task


@shared_task
def scrape_website(url):
    print(f"Scraping: {url}")
    
    response = requests.get(url)

    print(response.status_code)

    return response.text