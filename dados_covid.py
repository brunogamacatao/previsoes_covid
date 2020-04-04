import http.client
import mimetypes

def load_covid_data():
  conn = http.client.HTTPSConnection("xx9p7hp1p7.execute-api.us-east-1.amazonaws.com")
  payload = ''
  headers = {
    'authority': 'xx9p7hp1p7.execute-api.us-east-1.amazonaws.com',
    'method': 'GET',
    'path': '/prod/PortalAcumulo',
    'scheme': 'https',
    'accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'zip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,pt;q=0.8,ja;q=0.7',
    'origin': 'https://covid.saude.gov.b',
    'referer': 'https://covid.saude.gov.br/?fbclid=IwAR1mlx1mFSxaMUfPXSso-TM936HNfW5ZOYnl48taVYmGmuoZLtNN5G7B-_o',
    'sec-fetch-mode': 'cors',
    'sec-fetch-size': 'cross-site',
    'x-parse-application-id': 'unAFkcaNDeXajurGB7LChj8SgQYS2ptm'
  }
  conn.request("GET", "/prod/PortalAcumulo", payload, headers)
  res = conn.getresponse()
  return res.read()
