from flask import Flask, render_template, request 
import openai
app=Flask(__name__)
# openai.api_key="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"
def generate_message(name, company):
    prompt = f"""
    Write a professional sales outreach message to {name} from {company}.
    Keep it short, friendly, and persuasive.
    """
   from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}]
)

return response.choices[0].message.content
    return response['choices'][0]['message']['content']
def lead_score(company):
    score = len(company) * 10
    return min(score, 100)
@app.route('/', methods=['GET', 'POST'])
def index():
    message = ""
    score = ""
    if request.method == 'POST':
        name = request.form['name']
        company = request.form['company']
        message = generate_message(name, company)
        score = lead_score(company)
    return render_template('index.html', message=message, score=score)
if __name__ == '__main__':
    import os

app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
