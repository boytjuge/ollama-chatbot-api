from flask import Flask , render_template , url_for , jsonify ,redirect ,session,request , Response
import   ollama
import logging
app = Flask(__name__)
app.config['SECRET_KEY'] = 'fafwfwfwr25*cmcXdm1!2421'
app.config['SESSION_TYPE'] = 'filesystem'

desiredModel = 'llama3.2:latest'
questiontToAsk = "what is youtube ?"


# response = await ollama.chat(model=desiredModel, messages =[{
#         'role':'user',
#         'content':questiontext,
#     },])
# OllamaResponse = response['message']['content']
# print(OllamaResponse)


@app.route('/chatapi', methods=['POST'])
def  chatapi():
    recieve = request.json
    questiontext = recieve['question']
    #print(questiontext)
    print({'ip': request.remote_addr , 'msg':questiontext})
    def generate():
        response = ollama.chat(model=desiredModel, messages=[{
            'role': 'user',
            'content': questiontext,
        }])

        OllamaResponse = response['message']['content']
        yield OllamaResponse
        # Split response by sentence or other logic
        # sentences = OllamaResponse.split('. ')
        # for sentence in sentences:
        #     yield sentence + '. '  # Yielding each sentence as it's processed

    return Response(generate(), content_type='text/plain; charset=utf-8')

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1',port="7778")