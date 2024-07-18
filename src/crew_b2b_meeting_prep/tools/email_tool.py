import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from crewai_tools import BaseTool


class EmailTool(BaseTool):
    name: str = "Email"
    description: str = (
        "Sends an email to a specified recipient with a message."
    )

    def _run(self, report: str) -> str:
        message = Mail(
            from_email=os.environ.get('FROM_EMAIL'),
            to_emails=os.environ.get('TO_EMAIL'),
            subject='Test tool',
            html_content=report)
        try:
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e.message)
            return "Email not sent"
        
        return "Email sent successfully"
