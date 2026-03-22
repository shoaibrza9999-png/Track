with open('/home/jules/Amazon1/app.py', 'r') as f:
    app_content = f.read()

import re

# Remove SMTP imports
app_content = app_content.replace("import smtplib", "")
app_content = app_content.replace("from email.mime.text import MIMEText", "")
app_content = app_content.replace("from email.mime.multipart import MIMEMultipart", "")

# Rewrite send_email_alert function
old_email_alert = """def send_email_alert(user_email, item_title, item_url, current_price, target_price):
    smtp_server = os.environ.get('SMTP_SERVER', 'smtp.gmail.com')
    smtp_port = int(os.environ.get('SMTP_PORT', 587))
    smtp_user = os.environ.get('SMTP_USER')
    smtp_password = os.environ.get('SMTP_PASSWORD')

    if not (smtp_user and smtp_password):
        print("SMTP credentials not configured. Skipping email.", flush=True)
        return

    msg = MIMEMultipart()
    msg['From'] = smtp_user
    msg['To'] = user_email
    msg['Subject'] = f"Price Drop Alert: {item_title}"

    body = f"Good news! The price of {item_title} has dropped to ₹{current_price}, which is below your target of ₹{target_price}.\\n\\nBuy it here: {item_url}"
    msg.attach(MIMEText(body, 'plain', 'utf-8'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port, timeout=10)
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.send_message(msg)
        server.quit()
        print(f"Sent email alert to {user_email} for {item_title}", flush=True)
    except Exception as e:
        print(f"Failed to send email: {e}", flush=True)"""

new_email_alert = """def send_email_alert(user_email, item_title, item_url, current_price, target_price):
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

app_content = app_content.replace(old_email_alert, new_email_alert)

# Rewrite send_item_added_email
old_added_email = """def send_item_added_email(user_email, item_title, url, target_price):
    smtp_server = os.environ.get('SMTP_SERVER', 'smtp.gmail.com')
    smtp_port = int(os.environ.get('SMTP_PORT', 587))
    smtp_user = os.environ.get('SMTP_USER')
    smtp_password = os.environ.get('SMTP_PASSWORD')

    if not (smtp_user and smtp_password):
        print("SMTP credentials not configured. Skipping email.", flush=True)
        return

    msg = MIMEMultipart()
    msg['From'] = smtp_user
    msg['To'] = user_email
    msg['Subject'] = f"Item Added to Tracker: {item_title}"

    body = f"You have successfully added a new item to track!\\n\\nItem: {item_title}\\nTarget Price: ₹{target_price}\\nURL: {url}\\n\\nWe will notify you when the price drops below your target."
    msg.attach(MIMEText(body, 'plain', 'utf-8'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port, timeout=10)
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.send_message(msg)
        server.quit()
        print(f"Sent added item email to {user_email}", flush=True)
    except Exception as e:
        print(f"Failed to send email: {e}", flush=True)"""

new_added_email = """def send_item_added_email(user_email, item_title, url, target_price):
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

app_content = app_content.replace(old_added_email, new_added_email)

with open('/home/jules/Amazon1/app.py', 'w') as f:
    f.write(app_content)
