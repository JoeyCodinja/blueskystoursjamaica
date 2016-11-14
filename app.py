from flask import Flask
from flask import render_template
import os

application = Flask(__name__)
application.config.update(TEMPLATES_AUTO_RELOAD=True)
    


@application.route('/')
def index():
    return render_template('index.html')
    
if __name__ == "__main__":
    application.run(host=os.getenv("IP", "0.0.0.0"), port=os.getenv("PORT", 8080))
    