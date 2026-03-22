with open('/home/jules/Amazon1/README.md', 'r') as f:
    readme_content = f.read()

old_env = """2. **Email Alerts (Optional but recommended):**
   - `SMTP_SERVER`: The SMTP server (e.g., `smtp.gmail.com`).
   - `SMTP_PORT`: The SMTP port (usually `587`).
   - `SMTP_USER`: The email address used to send alerts.
   - `SMTP_PASSWORD`: The app password or password for the SMTP user."""

new_env = """2. **Email Alerts (Optional but recommended):**
   - `EMAIL_API_URL`: The URL of your lightweight SMTP server (e.g., `http://russetduck.onpella.app/send-email`). Defaults to `http://russetduck.onpella.app/send-email`.
   - `EMAIL_API_KEY`: An optional API key if your lightweight SMTP server requires authentication."""

readme_content = readme_content.replace(old_env, new_env)

with open('/home/jules/Amazon1/README.md', 'w') as f:
    f.write(readme_content)
