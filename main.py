import os

from dotenv import load_dotenv
from openai import OpenAI

from gmail_service import send_email
from sheets_service import save_to_google_sheets


# Load environment variables
load_dotenv()


def main():

    # Step 1: Get user question
    question = input("\nEnter your question: ").strip()

    if not question:
        print("Please enter a valid question.")
        return

    # Step 2: Generate AI response
    print("\nGenerating AI response...")

    try:
        api_key = os.getenv("OPENAI_API_KEY")

        if not api_key:
            raise ValueError("OPENAI_API_KEY is missing in .env")

        client = OpenAI(api_key=api_key)

        response = client.responses.create(
            model="gpt-4o-mini",
            input=question
        )

        ai_response = response.output_text

        if not ai_response:
            raise ValueError("OpenAI returned an empty response")

        print("\nAI Response:")
        print(ai_response)

    except Exception as error:
        print(f"OpenAI Error: {error}")
        return

    # Step 3: Send email
    print("\nSending AI response to Gmail...")

    email_status = "Failed"

    try:
        send_email(question, ai_response)
        email_status = "Sent"

        print("Email sent successfully!")

    except Exception as error:
        print(f"Gmail Error: {error}")

    # Step 4: Save data to Google Sheets
    print("\nSaving data to Google Sheets...")

    try:
        save_to_google_sheets(
            question=question,
            ai_response=ai_response,
            email_status=email_status
        )

        print("Google Sheets updated successfully!")

    except Exception as error:
        print(f"Google Sheets Error: {error}")


if __name__ == "__main__":
    main()