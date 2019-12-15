from flask import Flask, render_template
import os
app = Flask(__name__)

port = int(os.getenv("PORT", 3000))

@app.route('/', methods=['GET'])
def root():
    if(port==3000):
        return render_template('index.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)

