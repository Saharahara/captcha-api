from flask import Flask, request, jsonify, send_file
from captcha.image import ImageCaptcha
from flask_cors import CORS
import random
import string
import os
import secrets

app = Flask(__name__)
CORS(app)
captchas = {}


@app.route('/api/captcha/generate', methods=['GET'])
def generate_captcha():
    captcha_id = secrets.token_urlsafe(16)
    captcha_text = generate_random_text()
    captchas[captcha_id] = captcha_text
    image = ImageCaptcha()
    data = image.generate(captcha_text)
    print(captchas)
    return data.getvalue(), 200, {'Content-Type': 'image/png', 'Captcha-ID': captcha_id}


@app.route('/api/captcha/verify', methods=['POST'])
def verify_captcha():
    data = request.get_json()
    captcha_id = data.get('captchaId')
    user_response = data.get('userResponse')

    if captcha_id in captchas and user_response == captchas[captcha_id]:
        # Remove the used CAPTCHA to prevent reuse
        del captchas[captcha_id]
        return jsonify({'success': True}), 200
    else:
        return jsonify({'success': False}), 403


@app.route('/api/captcha/images/<captcha_id>', methods=['GET'])
def deliver_captcha_image(captcha_id):
    if captcha_id in captchas:
        image_path = f'temporary_images/{captcha_id}.png'
        image = ImageCaptcha()
        image.write(captchas[captcha_id], image_path)
        return send_file(image_path, mimetype='image/png', as_attachment=True)
    else:
        return jsonify({'error': 'Invalid CAPTCHA ID'}), 404

def generate_random_text():   
    size = random.randint(4, 6)
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(size))

if __name__ == '__main__':
    # Ensure a folder for temporary images exists
    os.makedirs('temporary_images', exist_ok=True)
    app.run(debug=True)

