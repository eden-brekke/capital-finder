from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class handler(BaseHTTPRequestHandler):
    # def do_GET(self):
    #     # url_components = parse.urlsplit(self.path)
    #     # query_string_list = parse.parse_qsl(url_components.query)
    #     # dic = dict(query_string_list)
    #     #
    #     # if "name" in dic:
    #     #     url = "https://restcountries.com/v3.1/capital"
    #     #     query = dic['name']
    #     #     full_url = url + query
    #     #     response = requests.get(full_url)
    #     #     data = response.json()
    #     #     country = data[0]['name']
    #     #     message = str(country['common'])
    #     #     final_message = f"{query} is the Capital of {country}"
    #     #     self.send_response(200)
    #     #     self.send_header('Content-type', 'text/plain')
    #     #     self.end_headers()
    #     #     self.wfile.write(final_message.encode())
    #     else:
    #         message = "Please type a Capital in as your query to the url and then we'll find the Country!"
    #         self.send_response(200)
    #         self.send_header('Content-type', 'text/plain')
    #         self.end_headers()
    #         self.wfile.write(message.encode())
    #     return
    def do_GET(self):
        url_components = parse.urlsplit(self.path)
        query_list = parse.parse_qsl(url_components.query)  # returns list, ['name', 'peru']
        dictionary = dict(query_list)  # turns list into dict
        # print(dictionary)
        if 'name' in dictionary:
            query = dictionary['name']
            # print(query)
            url = "https://restcountries.com/v3.1/capital/"
            complete_url = url + dictionary['name']
            # print(complete_url + ' this is your URL')
            response = requests.get(complete_url)
            data = response.json()
            country = data[0]['name']  # index's to the capital city.
            print(country)

            message = str(country['common'])
            final = f'{query} is the capital of {message}'
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(final.encode())

        else:
            message = "Type a country in the query to get its capital city."

            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(message.encode())
        return
