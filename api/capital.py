from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        url_components = parse.urlsplit(self.path)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        if 'name' in dic:
            url = "https://restcountries.com/v3.1/name"
            query = dic['name']
            full_url = url + query
            response = requests.get(full_url)
            data = response.json()
            capital = data[0]['capital']
            message = str(capital[0])
            print_message = f'The capital of {query} is {message}'
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(print_message.encode())
        else:
            message = "Oh no! Please type a country in as your query and then we will give you the capital city!"
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(message.encode())
        return
