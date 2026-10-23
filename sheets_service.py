import os
import requests

from dotenv import load_dotenv


load_dotenv()


def save_to_google_sheets(
    question,
    ai_response,
    email_status
):

    # Read configuration
    web_app_url = os.getenv(
        "GOOGLE_SHEETS_WEB_APP_URL"
    )

    api_secret = os.getenv(
        "GOOGLE_SHEETS_API_SECRET"
    )

    if not web_app_url or not api_secret:
        raise ValueError(
            "Google Sheets configuration is missing in .env"
        )

    # Prepare JSON payload
    payload = {
        "api_secret": api_secret,
        "question": question,
        "ai_response": ai_response,
        "email_status": email_status
    }

    # Send data to Google Apps Script
    response = requests.post(
        web_app_url,
        json=payload,
        timeout=30,
        allow_redirects=True
    )

    response.raise_for_status()

    # Validate JSON response
    try:
        result = response.json()

    except ValueError:
        raise RuntimeError(
            "Google Apps Script returned an invalid JSON response"
        )

    if result.get("status") != "success":
        raise RuntimeError(
            result.get(
                "message",
                "Unknown Google Sheets error"
            )
        )

    return True