from flask import Flask, render_template, request

# Create the web app
app = Flask(__name__)

# Connect the home page ("/") to this Python function
@app.route("/", methods=["GET", "POST"])
def home():
    greeting = ""

    # If the user clicked the button to send their name:
    if request.method == "POST":
        name = request.form.get("user_name")
        greeting = f"Hello, {name}! Welcome to your first web app."

    # Show the web page and pass the greeting into it
    return render_template("index.html", greeting=greeting)

# Start the app
if __name__ == "__main__":
    app.run(debug=True)