with open('/home/jules/Amazon1/app.py', 'r') as f:
    app_content = f.read()

# Update places calling fetch_amazon_price
old_update_call = "_, current_price = fetch_amazon_price(item.url, user.scraper_api_keys)"
new_update_call = "_, current_price = fetch_amazon_price(item.url, user.scraper_api_keys, user.amazon_paapi_access_key, user.amazon_paapi_secret_key, user.amazon_paapi_partner_tag)"
app_content = app_content.replace(old_update_call, new_update_call)

old_add_call = "title, current_price = fetch_amazon_price(url, scraper_api_keys)"
new_add_call = "title, current_price = fetch_amazon_price(url, scraper_api_keys, user.amazon_paapi_access_key, user.amazon_paapi_secret_key, user.amazon_paapi_partner_tag)"
app_content = app_content.replace(old_add_call, new_add_call)

old_add_keys_check = """    target_price = data.get('target_price')
    scraper_api_keys = data.get('scraper_api_keys') # User passes this from frontend as well
    check_interval_hours = data.get('check_interval_hours', 24)

    # Check duplicate
    existing = Item.query.filter_by(user_id=user.id, url=url).first()
    if existing:
        return jsonify({'error': 'Item is already being tracked in your dashboard.'}), 400

    if not url or not target_price or not scraper_api_keys:
        return jsonify({'error': 'Missing fields'}), 400"""

new_add_keys_check = """    target_price = data.get('target_price')
    check_interval_hours = data.get('check_interval_hours', 24)
    scraper_api_keys = user.scraper_api_keys

    # Check duplicate
    existing = Item.query.filter_by(user_id=user.id, url=url).first()
    if existing:
        return jsonify({'error': 'Item is already being tracked in your dashboard.'}), 400

    if not url or not target_price:
        return jsonify({'error': 'Missing fields'}), 400"""

app_content = app_content.replace(old_add_keys_check, new_add_keys_check)

with open('/home/jules/Amazon1/app.py', 'w') as f:
    f.write(app_content)
