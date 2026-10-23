# 🤖 Python AI API Automation

## 📌 Project Overview

Python AI API Automation is a beginner-friendly automation project
that integrates OpenAI, Gmail, and Google Sheets using Python.

The application allows users to enter a question once in the
VS Code terminal.

The question is sent to the OpenAI API, and the generated
response is automatically:

- Displayed in the terminal
- Sent to Gmail
- Saved to Google Sheets

This project demonstrates practical AI API integration
and workflow automation using Python.

---

## 🚀 Features

- AI-powered question answering
- OpenAI API integration
- Automated Gmail notifications
- Google Sheets data storage
- Google Apps Script integration
- Environment variable configuration
- API secret validation
- Error handling
- Independent Google Sheets testing

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Main automation language |
| OpenAI API | AI response generation |
| Gmail SMTP | Automated email delivery |
| Google Sheets | Data storage |
| Google Apps Script | HTTP API endpoint |
| Requests | HTTP communication |
| python-dotenv | Environment variable management |
| VS Code | Development environment |

---

## 🏗️ Project Architecture

```text
               USER INPUT
                   |
                   v
             VS Code Terminal
                   |
                   v
                 main.py
                   |
                   v
               OpenAI API
                   |
                   v
           AI Generated Response
                   |
          +--------+--------+
          |                 |
          v                 v
     Gmail Service     Sheets Service
          |                 |
          v                 v
      Gmail SMTP       HTTP POST
          |                 |
          v                 v
      Gmail Inbox      Google Apps Script
                            |
                            v
                       Google Sheets
```

---

## 📂 Project Structure

```text
Python-AI-API-Automation/
│
├── main.py
├── gmail_service.py
├── sheets_service.py
├── test_sheets.py
│
├── requirements.txt
├── .env
├── .env.example
├── .gitignore
│
└── README.md
```

---

## ⚙️ Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

Replace the placeholder URL with your own repository URL.

### Step 2: Open the Project

```bash
cd YOUR_REPOSITORY
```

### Step 3: Create a Virtual Environment

```bash
python -m venv .venv
```

### Step 4: Activate the Virtual Environment

Windows CMD:

```cmd
.venv\Scripts\activate
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Step 5: Install Dependencies

```bash
python -m pip install -r requirements.txt
```

---

## 🔐 Environment Configuration

Create a `.env` file in the project root.

```env
OPENAI_API_KEY=your_openai_api_key

GMAIL_SENDER=your_email@gmail.com
GMAIL_APP_PASSWORD=your_gmail_app_password
GMAIL_RECEIVER=your_email@gmail.com

GOOGLE_SHEETS_WEB_APP_URL=your_google_apps_script_url
GOOGLE_SHEETS_API_SECRET=your_api_secret
```

Never commit the `.env` file to GitHub.

OpenAI API usage may incur charges.

---

## 📧 Gmail Configuration

1. Sign in to your Google account.
2. Enable 2-Step Verification.
3. Open Google App Passwords.
4. Create an App Password for Python automation.
5. Store the App Password in `.env`.

The application uses Gmail SMTP over SSL on port 465.

Google App Password availability depends on your account settings.

---

## 📊 Google Sheets Configuration

### Step 1: Create a Spreadsheet

Create a spreadsheet named:

`Python_AI_API_Automation`

Rename the first worksheet:

`AI_Responses`

### Step 2: Add Column Headings

| Date & Time | User Question | AI Response | Email Status |
|-------------|---------------|-------------|--------------|

### Step 3: Create Google Apps Script

Open:

Extensions → Apps Script

Create the `doPost(e)` handler using the
Google Apps Script code supplied with this project.

### Step 4: Configure API Secret

Open:

Project Settings → Script Properties

Add:

```text
Property: API_SECRET
Value: Your randomly generated secret
```

The value must match `GOOGLE_SHEETS_API_SECRET`
in the Python `.env` file.

### Step 5: Deploy the Web App

Deploy the script as a Web App.

For this personal learning demo:

- Execute as: Me
- Who has access: Anyone

Copy the Web App URL into `.env`.

Warning: The endpoint is publicly reachable.
The shared secret provides basic protection only.
Do not use this configuration for sensitive data
or production workloads.

---

## ▶️ Run the Application

Execute:

```bash
python main.py
```

Enter your question:

```text
What is AI automation?
```

---

## 💻 Expected Terminal Output

```text
Enter your question: What is AI automation?

Generating AI response...

AI Response:
AI automation uses artificial intelligence
to perform tasks automatically.

Sending AI response to Gmail...
Email sent successfully!

Saving data to Google Sheets...
Google Sheets updated successfully!
```

The actual AI-generated answer may vary.

---

## 📧 Gmail Output

Subject:

AI API Automation - Generated Response

Email body:

```text
Hello,

Your AI-generated response is ready.

Question:
What is AI automation?

AI Response:
AI automation uses artificial intelligence
to perform tasks automatically.

Regards,
Python AI API Automation
```

---

## 📊 Google Sheets Output

| Date & Time | User Question | AI Response | Email Status |
|-------------|---------------|-------------|--------------|
| Automatically generated | What is AI automation? | AI-generated response | Sent |

Each successful execution creates a new row.

---

## 🧪 Test Google Sheets Independently

Run:

```bash
python test_sheets.py
```

Expected output:

```text
==================================================
GOOGLE SHEETS AUTOMATION TEST
==================================================

Google Sheets Test Successful!
```

This test does not call OpenAI or send Gmail messages.

---

## 🔄 Automation Workflow

1. User enters a question in VS Code.
2. Python sends the question to OpenAI.
3. OpenAI generates a response.
4. Python sends the response to Gmail.
5. Python sends the same response to Google Apps Script.
6. Google Apps Script inserts a row into Google Sheets.
7. Python displays the execution status.

---

## 🛡️ Security

- Store credentials in `.env`.
- Never commit passwords or API keys.
- Use Gmail App Passwords instead of regular passwords.
- Validate requests using an API secret.
- Keep Google Apps Script deployment URLs private.
- Use test data rather than sensitive information.
- Rotate exposed secrets immediately.

---

## 🐛 Troubleshooting

### OpenAI API Error

Verify:

- OpenAI API key
- API access
- Available API credits
- Internet connectivity

### Gmail Authentication Error

Verify:

- Gmail address
- 2-Step Verification
- Gmail App Password
- SMTP connectivity

### Google Sheets Unauthorized Request

Verify:

- Apps Script `API_SECRET`
- Python `GOOGLE_SHEETS_API_SECRET`
- Both values match exactly

### Google Sheets Not Updating

Verify:

- Web App URL
- Apps Script deployment
- Sheet name `AI_Responses`
- Google Apps Script execution logs

---

## 🎯 Learning Outcomes

This project demonstrates:

- Python API integration
- Generative AI integration
- HTTP POST requests
- JSON payload handling
- Gmail SMTP automation
- Google Sheets automation
- Environment variable management
- Error handling
- Basic API authentication

---

## 🔮 Future Enhancements

- Streamlit web interface
- Scheduled automation
- Email templates
- Logging and monitoring
- Multiple Gmail recipients
- Google Sheets reporting dashboard
- Retry handling
- Duplicate request prevention
- Docker containerization

---

## 📌 Project Status

| Component | Status |
|-----------|--------|
| Python Application | Completed |
| OpenAI API | Completed |
| Gmail Integration | Completed |
| Google Apps Script | Completed |
| Google Sheets Integration | Completed |
| End-to-End Automation | Completed |

---

## 👨‍💻 Project Type

Python | Generative AI | API Integration | Gmail Automation |
Google Sheets Automation