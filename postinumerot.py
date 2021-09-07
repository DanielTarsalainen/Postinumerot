from http_pyynto import fetch_postaldata


class coloredtext:
    SOS = '\033[93m'
    ENDC = '\033[0m'
        #I found a cool method to colorize text.
        #Source: https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal

def groupby_district(number_library):
    places = {}
    for postalnumber, name in number_library.items():
        if name not in places:
            places[name] = []

        places[name].append(postalnumber)

    return places

postalinfo = fetch_postaldata()

inputdistrict = input('Kirjoita paikkakunta: ').strip().upper()

districts = groupby_district(postalinfo)

if inputdistrict in districts:
        districts[inputdistrict].sort()
        foundnumbers_str = ", ".join(districts[inputdistrict])
            
        print(f'Paikkakunnan "{inputdistrict.title()}" postinumerot: {foundnumbers_str}')
else:
        print(f"{coloredtext.SOS}Syöte oli virheellinen. Yritä uudelleen!{coloredtext.ENDC}")