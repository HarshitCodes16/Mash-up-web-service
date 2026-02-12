# Mashup Audio Generator & Web Service

This project is developed as part of **UCS654 – Predictive Statistics Assignment**.

It contains:

-  **Program 1:** Command-line Mashup Generator  
-  **Program 2:** Web-based Mashup Service (Flask) with Email Delivery  

---

#  Project Structure

```
Mash-up-web-service/
│── 102303276.py        # Program 1 (CLI mashup generator)
│── app.py              # Flask web app
│── mashup.py           # Core mashup logic
│── audios/
│── templates/
│   └── index.html
│── README.md
```

---

# Requirements

Install required Python libraries:

```bash
pip install flask yt-dlp pydub
```

Also install:

- **FFmpeg** (must be added to system PATH)

Check FFmpeg installation:

```bash
ffmpeg -version
```

---

# How to Run (Program 2 – Web App)

Run the Flask server:

```bash
python app.py
```

Then open in browser:

```
http://127.0.0.1:5000
```

Fill the form and click **Submit**.

---

# How to Run (Program 1 – Command Line)

```bash
python 102303276.py "Sharry Maan" 20 30 output.mp3
```

---

# Email Feature

- Uses **Gmail SMTP**
- Uses **Google App Password**
- Automatically sends **ZIP file** containing mashup to user's email

---

# Example Input

- **Singer Name:** Sharry Maan  
- **Number of Videos:** 20  
- **Duration:** 30 seconds  
- **Email:** yourmail@gmail.com  

---

# Output

- `output.mp3` → Generated mashup file  
- `result.zip` → Sent to user's email  

---

## Web Interface

> Mashup Generator Web UI:

![Web UI](web_app.png)

---

## Email Received Output

> Mashup ZIP received on email:

![Email Output](mail_confirm.jpeg)


# Course Information

- **Course:** UCS654 – Predictive Statistics  
- **Assignment:** Mashup Generator  
- **Student:** Harshit Katyal  
- **Roll No:** 102303276  

---

# Assignment Requirements Covered

- Uses `pypi.org` libraries  
- Downloads from YouTube  
- Converts to audio  
- Cuts first Y seconds  
- Merges into one file  
- Web service implemented  
- Email delivery implemented  
- Input validation done  

---

# Important Notes

- FFmpeg must be properly installed and added to PATH  
- Internet connection required for YouTube download  
- Gmail **App Password** must be configured in `app.py`  
- Do NOT use your normal Gmail password  

---

# Developed By

**Harshit Katyal**  
Roll No: **102303276**  
UCS654 – Predictive Statistics  