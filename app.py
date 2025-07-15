from flask import Flask, request, jsonify, render_template
from agents import multi_agent

# Initialize Flask application
app = Flask(__name__)

#Load index.html template
@app.route("/")
def index():
    return render_template("index.html")

# Endpoint to handle queries
@app.route("/query", methods=["POST"])
def handle_query():
    data = request.get_json()
    query = data.get("query", "")

    try:
        response = multi_agent.run(query)
        response = str(response.content)
        while "transfer_task_to_" in response:
            response = response[response.index("transfer_task_to_"):]
            response = "\n".join(response.split("\n")[1:])
            response = response.strip()
        response = response.replace("\n\n", "\n")
        response = response.strip()
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"response": f"<strong>Error:</strong> {str(e)}"}), 500

# Main entry point to run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
