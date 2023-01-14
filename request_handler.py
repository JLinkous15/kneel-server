import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from views import *


class HandleRequests(BaseHTTPRequestHandler):
    """Controls the functionality of any GET, PUT, POST, DELETE requests to the server
    """

    def do_GET(self):
        """Handles GET requests to the server """
        self._set_headers(200)

        response={}

        (path, id) = self.parse_url(self.path)

        if path == "metals":
            if id is not None:
                response = get_single_metal(id)
            else:
                response=get_all_metals()
        elif path == "orders":
            if id is not None:
                response = get_single_order(id)
            else:
                response=get_all_orders()
        elif path == "sizes":
            if id is not None:
                response = get_single_size(id)
            else:
                response=get_all_sizes()
        elif path == "styles":
            if id is not None:
                response = get_single_style(id)
            else:
                response=get_all_styles()
        else:
            response = []

        self.wfile.write(json.dumps(response).encode())

    def do_POST(self):

        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)
        (resource, id) = self.parse_url(self.path)
        new_resource = None
        if resource == "orders":
            new_resource = create_order(post_body)
        self.wfile.write(json.dumps(new_resource).encode())


    def do_PUT(self):
        self._set_headers(204)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Delete a single animal from the list
        if resource == "orders":
            update_order(id, post_body)

        # Encode the new animal and send in response
        self.wfile.write("".encode())

    def do_DELETE(self):
    # Set a 204 response code
        self._set_headers(204)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Delete a single animal from the list
        if resource == "orders":
            delete_order(id)

        # Encode the new animal and send in response
        self.wfile.write("".encode())

    def _set_headers(self, status):
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_OPTIONS(self):
        """Sets the options headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    def parse_url(self, path):
        """Parses the request url to a tuple
        """
        path_params = path.split("/")
        resource = path_params[1]
        id = None

        try:
            id = int(path_params[2])
        except IndexError:
            pass  

        except ValueError:
            pass  
        
        return (resource, id)  



# point of this application.
def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
