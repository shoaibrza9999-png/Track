with open('/home/jules/Amazon1/app.py', 'r') as f:
    app_content = f.read()

import re

# We will use regex to completely replace the fetch_amazon_price function
old_fetch_pattern = r'# Helper for Scraping.*?def fetch_amazon_price\(url, scraper_api_keys\):.*?return None, None'

new_fetch = """# Helper for Scraping
def extract_asin(url):
    match = re.search(r'/([A-Z0-9]{10})(?:[/?]|$)', url)
    if match:
        return match.group(1)
    return None

def fetch_amazon_paapi_price(url, access_key, secret_key, partner_tag):
    asin = extract_asin(url)
    if not asin:
        return None, None

    try:
        from amazon.paapi import AmazonAPI
        amazon = AmazonAPI(access_key, secret_key, partner_tag, 'IN')
        items = amazon.get_items(item_ids=[asin])
        if not items or len(items) == 0:
            return None, None

        item = items[0]
        title = item.item_info.title.display_value

        # Check offers
        if item.offers and item.offers.listings:
            price_amount = item.offers.listings[0].price.amount
            return title, price_amount

    except Exception as e:
        print(f"PA-API Error for {url}: {e}")

    return None, None

def fetch_amazon_price(url, scraper_api_keys, access_key=None, secret_key=None, partner_tag=None):
    # Try PA-API First
    if access_key and secret_key and partner_tag:
        title, price = fetch_amazon_paapi_price(url, access_key, secret_key, partner_tag)
        if title and price is not None:
            return title, price

    # Fallback to ScraperAPI
    if scraper_api_keys:
        keys = [k.strip() for k in scraper_api_keys.split(',') if k.strip()]
        for key in keys:
            payload = {
                'api_key': key,
                'url': url,
                'country_code': 'in', # specific to Amazon India as per prompt
                'render': 'true' # rendering JS can help fetch dynamic prices on Amazon
            }
            try:
                r = requests.get('https://api.scraperapi.com/', params=payload, timeout=30)
                if r.status_code == 200:
                    soup = BeautifulSoup(r.text, 'html.parser')
                    # Look for common Amazon price elements
                    title_el = soup.select_one('#productTitle')
                    title = title_el.text.strip() if title_el else "Unknown Product"

                    # Try finding `.a-price-whole`
                    price_el = soup.select_one('.a-price-whole')
                    if price_el:
                        price_text = price_el.text.strip().replace(',', '').replace('₹', '')
                        try:
                            price = float(price_text)
                            return title, price
                        except ValueError:
                            pass

                    # Try finding `.a-offscreen` which is common for prices now
                    price_el = soup.select_one('.apexPriceToPay .a-offscreen, .priceToPay .a-offscreen')
                    if price_el:
                        price_text = price_el.text.strip().replace(',', '').replace('₹', '')
                        try:
                            price = float(price_text)
                            return title, price
                        except ValueError:
                            pass

                    # Alternative price elements
                    price_el = soup.select_one('#priceblock_ourprice, #priceblock_dealprice, .a-color-price')
                    if price_el:
                        price_text = price_el.text.strip().replace(',', '').replace('₹', '')
                        try:
                            price = float(price_text)
                            return title, price
                        except ValueError:
                            pass

            except Exception as e:
                print(f"Error fetching {url} with key {key}: {e}")

    return None, None"""

app_content = re.sub(old_fetch_pattern, new_fetch, app_content, flags=re.DOTALL)

# Add missing import re if not present
if "import re" not in app_content:
    app_content = app_content.replace("import requests", "import requests\nimport re")

with open('/home/jules/Amazon1/app.py', 'w') as f:
    f.write(app_content)
