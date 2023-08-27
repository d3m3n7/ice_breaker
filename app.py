from flask import Flask, render_template, request, jsonify

from ice_braker import summarize_linkedin
from output_parser import get_parser, parse

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    name = request.form["name"]
    info = summarize_linkedin(person_intel_parser=get_parser())
    person_intel = parse(info)

    return jsonify(
        dict(
            summary=person_intel.summary,
            interests=person_intel.topics_of_interest,
            facts=person_intel.facts,
            ice_breakers=person_intel.ice_breakers,
            picture_url="No picture"
        )
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
