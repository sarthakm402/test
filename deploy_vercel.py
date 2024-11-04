from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

# Expose the app object to be used by Vercel as a handler
def handler(request, *args):
    return app(request.environ, start_response=args[0])

# Required for Vercel's serverless function handler
app.handler = handler
