import requests

from bs4 import BeautifulSoup
from celery import shared_task
from datetime import datetime

from .mongo import scraped_pages


@shared_task
def scrape_website(url):

    print(f"Scraping: {url}")

    response = requests.get(
        url,
        timeout=10
    )

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    title = ""

    if soup.title:
        title = soup.title.text.strip()

    text_content = soup.get_text(
        separator=" ",
        strip=True
    )

    preview = text_content[:500]

    links_count = len(
        soup.find_all("a")
    )

    document = {
        "url": url,
        "title": title,
        "status_code": response.status_code,
        "content_preview": preview,
        "links_count": links_count,
        "scraped_at": datetime.utcnow(),
    }

    result = scraped_pages.insert_one(document)

    print(
        f"Saved to MongoDB: {result.inserted_id}"
    )

    return str(result.inserted_id)