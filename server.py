from http.server import HTTPServer, SimpleHTTPRequestHandler
import urllib.request
import json


class CodeBuddyHandler(SimpleHTTPRequestHandler):

    def do_POST(self):

        if self.path == "/ask":

            length = int(self.headers["Content-Length"])
            data = self.rfile.read(length)

            request_data = json.loads(data.decode("utf-8"))

            question = request_data["question"]

            prompt = """
You are CodeBuddy, a friendly programming tutor.

The learner is a beginner.

Explain programming concepts clearly and simply.
Use small examples when helpful.
If the learner asks for a coding solution, explain the reasoning
and help them learn rather than blindly giving an answer.

User question:
""" + question

            ollama_data = {
                "model": "qwen2.5-coder:3b",
                "prompt": prompt,
                "stream": False
            }

            ollama_data = json.dumps(ollama_data).encode("utf-8")

            request = urllib.request.Request(
                "http://localhost:11434/api/generate",
                data=ollama_data,
                headers={"Content-Type": "application/json"}
            )

            response = urllib.request.urlopen(request)

            result = json.loads(
                response.read().decode("utf-8")
            )

            answer = result["response"]

            output = json.dumps({
                "answer": answer
            }).encode("utf-8")

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()

            self.wfile.write(output)

        else:

            self.send_error(404)


server = HTTPServer(("localhost", 8000), CodeBuddyHandler)

print("================================")
print("       CODEBUDDY SERVER")
print("================================")
print()
print("Open this in your browser:")
print("http://localhost:8000")
print()
print("Waiting for requests...")
print("Press Ctrl+C to stop the server.")

server.serve_forever()
