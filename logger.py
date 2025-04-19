from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Function to print logs in table format
def print_log_table(data):
    print(f"\n{'='*40}")
    print(f"{'LOGGED DATA':^40}")
    print(f"{'='*40}")
    print(f"{'Source':<20} | {'IP':<15} | {'User-Agent':<30} | {'Timezone':<15}")
    print(f"{'-'*40}")
    print(f"{data.get('source', 'Unknown'):<20} | {data.get('ip', 'Unknown IP'):<15} | {data.get('user_agent', 'Unknown'):<30} | {data.get('timezone', 'Unknown'):<15}")
    print(f"{'='*40}\n")

@app.route('/log', methods=['POST'])
def log_data():
    data = request.get_json()
    headers = dict(request.headers)

    # Print log in terminal in table format
    print_log_table(data)
    
    # Save the log to a file
    with open("logs.txt", "a") as f:
        f.write(json.dumps(data) + "\n")
    
    return jsonify({"status": "logged"})

@app.route('/')
def serve_page():
    return open("index.html").read()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
