from http.server import HTTPServer, BaseHTTPRequestHandler
import time

# ______________
# Get host from your local IP Address
HOST = "146.232.97.102"
PORT = 8000



# ______________
# create class
class NeuralHTTP(BaseHTTPRequestHandler) :

    # create get function
    def do_GET(self) :

        self.send_response(200) # website response to getting the webpage
        self.send_header("Content-type", "text/html") # set webpage as an html file type
        self.end_headers()   # close header
        
        HTML_DATA = '<h1>bblblblb</h1>'
        
        # write content to the webpage
        self.wfile.write(bytes("<html><body>"+ HTML_DATA +"<h1>Hello World!</h1></body></html>", "UTF-8"))

        
    # create post function  
    def do_POST(self) :
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        
        self.wfile.write(bytes('{"time": "' + date +'"} ', "utf-8"))

# ______________
# create server instance
server = HTTPServer((HOST, PORT), NeuralHTTP)
print("Server now running...")

# ______________
# start serving requests
server.serve_forever()

# ______________
# close server when finished
server.server_close()
print("Server stopped!")


# ONCE YOU HAVE EVERYTHING, RIGHT CLICK MAIN.PY AND SELECT " RUN FILE IN TERMINAL " AND THEN OPEN THE LINK IN THE WEB BROWSER

        
# ______________
# ***TIPS***

# 1. ______________
# run " python -m http.server 8000 " in the terminal/cmd to run the localhost server

# 2. ______________
# run " ipconfig " in the terminal/cmd and select the IP Adress at " IPv4 Address " which will act as the websites host

# 3. ______________
# The link " http://localhost:8000/ " OR " http://146.232.97.102:8000/ " will take you to the websites directory

# 4. ______________
# You can run " curl [ip address]:[port] == curl 146.232.97.102:8000 " in the cmd to display the code

# 5. ______________
# You can run " curl [ip address]:[port] -X POST == curl 146.232.97.102:8000 -X POST" in the cmd to display current date




