from flask import Flask
from flask import render_template
import os

app = Flask(__name__)
app.config.update(TEMPLATES_AUTO_RELOAD=True)
    


@app.route('/')
def index():
    return render_template('index.html')
    
if __name__ == "__main__":
    app.run(host=os.getenv("IP", "0.0.0.0"), port=os.getenv("PORT", 8080))
    