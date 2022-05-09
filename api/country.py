from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        url_components = parse.urlsplit(self.path)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)
        if 'name' in dic:
            query = dic['name']
            url = "https://restcountries.com/v3.1/capital/"
            full_url = url + dic['name']
            response = requests.get(full_url)
            data = response.json()
            country = data[0]['name']
            message = str(country['common'])
            final = f'{query} is the capital of {message}'
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(final.encode())
        else:
            message = "Please type a Capital in as your query to the url and then we'll find the Country!"
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(message.encode())
        return
