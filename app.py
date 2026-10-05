from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get('message', '')
    # Placeholder for AstraMind AI logic
    response = f"AstraMind received: {message}"
    return jsonify({"response": response})

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>AstraMind MVP</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            #chat-log { height: 300px; border: 1px solid #ccc; padding: 10px; overflow-y: auto; margin-bottom: 10px; }
            #message { width: 80%; padding: 10px; }
            button { padding: 10px 20px; }
        </style>
    </head>
    <body>
        <h1>AstraMind</h1>
        <div id="chat-log"></div>
        <input type="text" id="message" placeholder="Ask AstraMind something...">
        <button onclick="sendMessage()">Send</button>

        <script>
            async function sendMessage() {
                const msgInput = document.getElementById('message');
                const log = document.getElementById('chat-log');
                const text = msgInput.value;
                if (!text) return;
                
                log.innerHTML += '<div><b>You:</b> ' + text + '</div>';
                msgInput.value = '';
                
                const response = await fetch('/api/chat', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ message: text })
                });
                
                const data = await response.json();
                log.innerHTML += '<div><b>AstraMind:</b> ' + data.response + '</div>';
                log.scrollTop = log.scrollHeight;
            }
        </script>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True, port=5000)
