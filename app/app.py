from flask import Flask, jsonify

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def home():
        return jsonify({"message": "CI/CD with Jenkins is working!"})

    @app.route("/health")
    def health():
        return jsonify({"status": "healthy"})

    return app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
