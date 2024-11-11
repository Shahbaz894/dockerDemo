from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    table = []
    number = None

    if request.method == "POST":
        try:
            # Get the input number from the form
            number = int(request.form["number"])

            # Generate the multiplication table
            table = [(number, i, number * i) for i in range(1, 11)]
        except ValueError:
            # Handle non-integer input
            number = None

    return render_template("index.html", number=number, table=table)

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=5000)
