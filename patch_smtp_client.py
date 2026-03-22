with open('/home/jules/Amazon1/app.py', 'r') as f:
    app_content = f.read()

old_email_alert = """def send_email_alert(user_email, item_title, item_url, current_price, target_price):
    email_api_url = os.environ.get('EMAIL_API_URL', 'http://russetduck.onpella.app/send-email')
    email_api_key = os.environ.get('EMAIL_API_KEY', '')

    subject = f"Price Drop Alert: {item_title}"
    body = f"Good news! The price of {item_title} has dropped to ₹{current_price}, which is below your target of ₹{target_price}.\\n\\nBuy it here: {item_url}"

    payload = {
        "to_email": user_email,
        "subject": subject,
        "body": body
    }

    headers = {"Content-Type": "application/json"}
    if email_api_key:
        headers["x-api-key"] = email_api_key

    try:
        response = requests.post(email_api_url, json=payload, headers=headers, timeout=10)
        if response.status_code == 200:
            print(f"Sent email alert to {user_email} for {item_title}", flush=True)
        else:
            print(f"Failed to send email. API returned {response.status_code}: {response.text}", flush=True)
    except Exception as e:
        print(f"Failed to call email API: {e}", flush=True)"""

new_email_alert = """def send_email_alert(user_email, item_title, item_url, current_price, target_price):
    email_api_url = os.environ.get('EMAIL_API_URL', 'http://russetduck.onpella.app/send-email')
    email_api_key = os.environ.get('EMAIL_API_KEY', '')

    smtp_server = os.environ.get('SMTP_SERVER', 'smtp.gmail.com')
    smtp_port = int(os.environ.get('SMTP_PORT', 587))
    smtp_user = os.environ.get('SMTP_USER')
    smtp_password = os.environ.get('SMTP_PASSWORD')

    subject = f"Price Drop Alert: {item_title}"
    body = f"Good news! The price of {item_title} has dropped to ₹{current_price}, which is below your target of ₹{target_price}.\\n\\nBuy it here: {item_url}"

    payload = {
        "to_email": user_email,
        "subject": subject,
        "body": body,
        "smtp_server": smtp_server,
        "smtp_port": smtp_port,
        "smtp_user": smtp_user,
        "smtp_password": smtp_password
    }

    headers = {"Content-Type": "application/json"}
    if email_api_key:
        headers["x-api-key"] = email_api_key

    try:
        response = requests.post(email_api_url, json=payload, headers=headers, timeout=10)
        if response.status_code == 200:
            print(f"Sent email alert to {user_email} for {item_title}", flush=True)
        else:
            print(f"Failed to send email. API returned {response.status_code}: {response.text}", flush=True)
    except Exception as e:
        print(f"Failed to call email API: {e}", flush=True)"""

app_content = app_content.replace(old_email_alert, new_email_alert)

old_added_email = """def send_item_added_email(user_email, item_title, url, target_price):
    email_api_url = os.environ.get('EMAIL_API_URL', 'http://russetduck.onpella.app/send-email')
    email_api_key = os.environ.get('EMAIL_API_KEY', '')

    subject = f"Item Added to Tracker: {item_title}"
    body = f"You have successfully added a new item to track!\\n\\nItem: {item_title}\\nTarget Price: ₹{target_price}\\nURL: {url}\\n\\nWe will notify you when the price drops below your target."

    payload = {
        "to_email": user_email,
        "subject": subject,
        "body": body
    }

    headers = {"Content-Type": "application/json"}
    if email_api_key:
        headers["x-api-key"] = email_api_key

    try:
        response = requests.post(email_api_url, json=payload, headers=headers, timeout=10)
        if response.status_code == 200:
            print(f"Sent added item email to {user_email}", flush=True)
        else:
            print(f"Failed to send email. API returned {response.status_code}: {response.text}", flush=True)
    except Exception as e:
        print(f"Failed to call email API: {e}", flush=True)"""

new_added_email = """def send_item_added_email(user_email, item_title, url, target_price):
    email_api_url = os.environ.get('EMAIL_API_URL', 'http://russetduck.onpella.app/send-email')
    email_api_key = os.environ.get('EMAIL_API_KEY', '')

    smtp_server = os.environ.get('SMTP_SERVER', 'smtp.gmail.com')
    smtp_port = int(os.environ.get('SMTP_PORT', 587))
    smtp_user = os.environ.get('SMTP_USER')
    smtp_password = os.environ.get('SMTP_PASSWORD')

    subject = f"Item Added to Tracker: {item_title}"
    body = f"You have successfully added a new item to track!\\n\\nItem: {item_title}\\nTarget Price: ₹{target_price}\\nURL: {url}\\n\\nWe will notify you when the price drops below your target."

    payload = {
        "to_email": user_email,
        "subject": subject,
        "body": body,
        "smtp_server": smtp_server,
        "smtp_port": smtp_port,
        "smtp_user": smtp_user,
        "smtp_password": smtp_password
    }

    headers = {"Content-Type": "application/json"}
    if email_api_key:
        headers["x-api-key"] = email_api_key

    try:
        response = requests.post(email_api_url, json=payload, headers=headers, timeout=10)
        if response.status_code == 200:
            print(f"Sent added item email to {user_email}", flush=True)
        else:
            print(f"Failed to send email. API returned {response.status_code}: {response.text}", flush=True)
    except Exception as e:
        print(f"Failed to call email API: {e}", flush=True)"""

app_content = app_content.replace(old_added_email, new_added_email)

with open('/home/jules/Amazon1/app.py', 'w') as f:
    f.write(app_content)
