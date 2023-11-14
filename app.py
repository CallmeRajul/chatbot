#Final app.py 
#import files
from flask import Flask, render_template, request
import openai
app = Flask(__name__)
openai.api_key  = "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"

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, 
    )
    return response.choices[0].message["content"]
@app.route("/")
def home():    
    return render_template("index.html")
@app.route("/get")
def get_bot_response():    
    userText = request.args.get('msg')  
    response = get_completion(userText)  
    return response
if __name__ == "__main__":
    app.run(debug=True)