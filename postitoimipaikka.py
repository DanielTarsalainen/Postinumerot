import urllib.request
import json
import http_pyynto


postalinfo = http_pyynto.fetch_postaldata()

postalnumber = input('Kirjoita postinumero: ')

if postalnumber in postalinfo:
    print(postalinfo[postalnumber])
else:
    print("Väärä syöte. Yritä uudelleen")

