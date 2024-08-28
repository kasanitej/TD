from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Secure World!"

if __name__ == '__main__':
    # Specify the paths to your certificate and key files
    # openssl req -newkey rsa:4096 -keyout key.pem -out cert.pem -x509 -days 365
    # pass phrase : 1234 #You must type in 4 to 1024 characters
    # Country Name (2 letter code) [AU]:IN
    # State or Province Name (full name) [Some-State]:Andhra Pradesh
    # Locality Name (eg, city) []:Rajahmundry
    # Organization Name (eg, company) [Internet Widgits Pty Ltd]:kasani    
    # Organizational Unit Name (eg, section) []:
    # Common Name (e.g. server FQDN or YOUR name) []:kasanitej.com
    # Email Address []:kasanitej@gmail.com
    # To Check the details of certificate cert.pem
    # openssl x509 -in cert.pem -noout -text 
    context = ('cert.pem', 'key.pem')
    
    # Run the app with SSL context
    app.run(host='0.0.0.0', port=5000, ssl_context=context)
