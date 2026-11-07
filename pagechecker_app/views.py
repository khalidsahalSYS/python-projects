from django.http import HttpRequest
from django.shortcuts import render

from bs4 import BeautifulSoup
import requests

from .forms import PageCheckForm


def page_checker(request: HttpRequest):
    form = PageCheckForm(request.POST or None)
    result = None

    if request.method == "POST" and form.is_valid():
        url = form.cleaned_data["url"]

        try:
            response = requests.get(url, timeout=15, allow_redirects=True)
            response_time_ms = round(response.elapsed.total_seconds() * 1000, 2)
            soup = BeautifulSoup(response.text, "html.parser")

            title = soup.title.get_text(strip=True) if soup.title else "No title found"
            meta_description = "No meta description found"
            meta_tag = soup.find("meta", attrs={"name": "description"}) or soup.find(
                "meta", attrs={"property": "description"}
            )
            if meta_tag and meta_tag.get("content"):
                meta_description = meta_tag.get("content", "").strip()

            heading = soup.find("h1")
            heading_text = heading.get_text(strip=True) if heading else "No H1 heading found"

            result = {
                "url": response.url,
                "status_code": response.status_code,
                "status_text": "OK" if response.status_code < 400 else "Error",
                "response_time_ms": response_time_ms,
                "title": title,
                "meta_description": meta_description,
                "heading": heading_text,
                "content_length": len(response.text),
                "is_successful": response.status_code < 400,
            }
        except requests.RequestException as exc:
            form.add_error("url", f"The page could not be loaded: {exc}")

    return render(request, "pagechecker/home.html", {"form": form, "result": result})
