import json
import PySimpleGUIQt as g
import urllib.request
from currency_converter import CurrencyConverter
def get_price():
    request = urllib.request.urlopen("https://api.coindesk.com/v1/bpi/currentprice.json")
    x = json.loads(request.read().decode("utf-8"))
    request.close()
    return x

layout = [
    [g.Text("Bitcoin Price: USD {}".format(get_price()["bpi"]["USD"]["rate"]))],
    [g.Text("Last Updated: {}".format(get_price()["time"]["updated"]))],
    [g.Button("Ok")]
]

window = g.Window('Bitcoin Price GUI', layout)
while True:
    event, value = window.Read()
    if event == "Ok":
        break
    else:
        break

window.Close()