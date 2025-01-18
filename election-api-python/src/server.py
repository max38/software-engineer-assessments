from flask import Flask, request
from results_controller import ResultsController

app: Flask = Flask(__name__)
controller: ResultsController = ResultsController()

@app.route("/result/<identifier>", methods=["GET"])
def individual_result(identifier) -> dict:
    return controller.get_result(int(identifier))

@app.route("/result", methods=["POST"])
def add_result() -> dict:
    return controller.new_result(request.json)

@app.route("/scoreboard", methods=["GET"])
def scoreboard() -> dict:
    return controller.scoreboard()

@app.errorhandler(Exception)
def all_exception_handler(e):
    print(f"[ERROR] - exception ({type(e).__name__}) occurred during request handling: {e}")
    return {}, 500
