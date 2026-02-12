#orre efan rgus rmqv

from flask import Flask, render_template, request
import re
import shutil
import os
import smtplib
import os
from email.message import EmailMessage
from mashup import create_mashup

SENDER_EMAIL = os.getenv("SENDER_EMAIL", "") # your email address
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD", "") # your email password or app password

app = Flask(__name__)

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        singer = request.form["singer"]
        num = int(request.form["num"])
        duration = int(request.form["duration"])
        email = request.form["email"]

        if not is_valid_email(email):
            return "Invalid Email ID!"

        output = "output.mp3"

        # Create mashup
        create_mashup(singer, num, duration, output)

        # Zip it
        zip_name = "result"
        if os.path.exists("result.zip"):
            os.remove("result.zip")

        shutil.make_archive(zip_name, "zip", root_dir=".", base_dir=output)

        # Send email
        msg = EmailMessage()
        msg["Subject"] = "Your Mashup is Ready!"
        msg["From"] = SENDER_EMAIL
        msg["To"] = email
        msg.set_content("Your mashup is attached.")

        with open("result.zip", "rb") as f:
            msg.add_attachment(
                f.read(),
                maintype="application",
                subtype="zip",
                filename="result.zip"
            )

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
            smtp.send_message(msg)

        return "Mashup sent to your email successfully!"

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
