from flask import Flask, send_from_directory

app = Flask(__name__, static_url_path='')

from app import views