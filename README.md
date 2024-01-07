# captcha-api
# CAPTCHA API

This Flask-based API provides endpoints for generating, verifying CAPTCHAs, and securely delivering CAPTCHA images.


1. **Clone the repository:**

   ```bash
   git clone https://github.com/Saharahara/captcha-api.git
   cd captcha-api
2. **Install dependencies**
   ```bash
   pip install Flask Flask-CORS captcha
   pip install Flask-CORS
   pip install captcha
3. **Run the Application**
    ```bash
   python3 captcha_api.py
4.  **Generate a captcha**
   Make a GET request to the /api/captcha/generate endpoint:
   ```bash
   curl http://127.0.0.1:5000/api/captcha/generate
   ```
   The response will include a CAPTCHA image and a unique Captcha-ID header.
   You can also directly generate captchas from your browser with the url.


5. **Verify the Captcha**
    Make a POST request to the /api/captcha/verify endpoint with the CAPTCHA ID and user response:
   ```bash
   curl -X POST -H "Content-Type: application/json" -d '{"captchaId": "your_captcha_id", "userResponse": "user_input_here"}' http://127.0.0.1:5000/api/captcha/verify
   ```
   Replace "your_captcha_id" and "user_input_here" with the actual CAPTCHA ID received during generation and the user's input, respectively.

6. **Access CAPTCHA images securely**
 Access CAPTCHA images securely by visiting a URL like http://127.0.0.1:5000/api/captcha/images/your_captcha_id in your browser or using a tool like curl

   

