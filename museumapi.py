from flask import Flask, request, jsonify
import mysql.connector
from creds import DB_CONFIG

app = Flask(__name__)