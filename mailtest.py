import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import secret
import datetime
from google import genai
from secret import api_key
        
#generate some python code to draw a manim square name the method helloworld
x="generate a paragraph or a quote from any famous self help book/biography that is motivational and inspiring, and can be used as a daily reminder to stay positive and focused on personal growth. The quote should be concise, impactful, and suitable for sharing on social media platforms like Instagram or Twitter. It should resonate with individuals seeking motivation and encouragement in their daily lives."

# print(x)

client = genai.Client(api_key=api_key)
response = client.models.generate_content(
    model="gemini-1.5-flash",
    contents=x
)
print(response.text)

sender_email = secret.sender_email
receiver_email = secret.receiver_email
app_password = secret.app_password  

timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
subject = f"Book Quote Paragraph [{timestamp}]"
body = response.text.strip()  # Use the generated content as the email body

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

message.attach(MIMEText(body, "plain"))

# Step 3: Send the email using Gmail SMTP server
try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, app_password)
        server.sendmail(sender_email, receiver_email, message.as_string())
    print("✅ Email sent successfully!")
except Exception as e:
    print("❌ Failed to send email:", e)
