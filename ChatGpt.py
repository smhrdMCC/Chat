from flask import Flask, request, jsonify
import openai
import time

app = Flask(__name__)
with open("key.txt", "r") as f:
    example = f.read()


# OpenAI API 인증
openai.api_key=example

# ChatGPT에 대한 함수 정의
def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system", 
                "content": "너는 심리 상담을 해주면서 힐링이 되는 말을 해주는 역할이야"
            },
            {"role": "user", "content": prompt},
  ]
    )
    return response.choices[0].message.content

# 라우트 정의
@app.route('/chat', methods=['POST'])
def chat():
    
    data = request.get_json()
    prompt = data
    response = chat_with_gpt(prompt)
    
    print(response)
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=False,host="127.0.0.1",port=5000)
    