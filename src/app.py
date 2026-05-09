import os
import subprocess
import hashlib

def get_user(user_input):
    # SQL injection vulnerability
    query = "SELECT * FROM users WHERE name = " + user_input
    return query

def run_command(cmd):
    # Command injection vulnerability
    os.system(cmd)

def hash_password(password):
    # Weak hashing vulnerability
    return hashlib.md5(password.encode()).hexdigest()

def read_file(filename):
    # Path traversal vulnerability
    with open("/var/data/" + filename) as f:
        return f.read()
