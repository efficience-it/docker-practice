import yaml
import requests
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from requests.exceptions import RequestException

MAX_WORKERS = 10
TIMEOUT = 10
EXCLUDED_DOMAINS = ['github.com']

checked_urls = {}
broken_links = []

def should_skip(url):
    return any(domain in url for domain in EXCLUDED_DOMAINS)

def check_url(url):
    if url in checked_urls:
        return url, checked_urls[url]

    if should_skip(url):
        print(f"⏭️ Skipped (excluded): {url}")
        checked_urls[url] = True  # Treat as valid
        return url, True

    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (compatible; LinkChecker/1.0)"
        }
        response = requests.head(url, headers=headers, allow_redirects=True, timeout=TIMEOUT)
        if response.status_code >= 400:
            response = requests.get(url, headers=headers, allow_redirects=True, timeout=TIMEOUT)
        is_ok = response.status_code < 400
    except RequestException:
        is_ok = False

    checked_urls[url] = is_ok
    return url, is_ok

def extract_urls_from_yaml(file_path):
    urls = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
            if not data or "questions" not in data:
                return urls
            for q in data["questions"]:
                url = q.get("help")
                if isinstance(url, str) and url.startswith("http"):
                    urls.append((str(file_path), url))
    except Exception as e:
        print(f"⚠️ Failed to parse {file_path}: {e}")
    return urls

def main():
    # Gather all URLs
    all_links = []
    for file in Path("data").rglob("*.yaml"):
        all_links.extend(extract_urls_from_yaml(file))

    # Extract unique URLs to check
    unique_urls = sorted(set(url for _, url in all_links))

    print(f"🔍 Checking {len(unique_urls)} unique links using {MAX_WORKERS} threads...\n")
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        results = list(executor.map(check_url, unique_urls))

    # Match broken URLs with their source files
    for file_path, url in all_links:
        if not checked_urls.get(url):
            broken_links.append((file_path, url))

    # Final report
    if broken_links:
        print("\n🚨 Broken links found:")
        for file_path, url in broken_links:
            print(f"- {file_path}: {url}")
        exit(1)
    else:
        print("\n🎉 No broken links found.")
        exit(0)

if __name__ == "__main__":
    main()
