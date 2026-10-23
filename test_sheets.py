from sheets_service import save_to_google_sheets


def test_google_sheets():

    print("=" * 50)
    print("GOOGLE SHEETS AUTOMATION TEST")
    print("=" * 50)

    question = "What is AI Automation?"

    ai_response = (
        "AI Automation uses artificial intelligence "
        "to perform repetitive tasks automatically."
    )

    email_status = "Test - Email Not Sent"

    try:
        save_to_google_sheets(
            question=question,
            ai_response=ai_response,
            email_status=email_status
        )

        print("\nGoogle Sheets Test Successful!")

    except Exception as error:
        print(f"\nGoogle Sheets Test Failed: {error}")


if __name__ == "__main__":
    test_google_sheets()