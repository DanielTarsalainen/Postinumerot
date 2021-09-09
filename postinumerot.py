from http_pyynto import fetch_postaldata


class coloredtext:
    SOS = '\033[93m'
    ENDC = '\033[0m'
    # I found a cool method to colorize text.
    # Source: https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal


def groupby_district(number_library):
    places = {}

    for postalnumber, name in number_library.items():
        name = cleanup_district(name)

        if name not in places:
            places[name] = []

        places[name].append(postalnumber)

    return places


def cleanup_district(district):
    cleaned_district = district.replace(" ", "").replace("-", "")

    if cleaned_district == "SMARTPSOT":
        cleaned_district = cleaned_district.replace("SO", "OS")

    return cleaned_district


def main():

    postalinfo = fetch_postaldata()

    districts = groupby_district(postalinfo)

    while True:
        inputdistrict = input('Kirjoita paikkakunta: ').strip().upper()
        inputdistrict = cleanup_district(inputdistrict)

        if inputdistrict in districts:
            districts[inputdistrict].sort()
            foundnumbers_str = ", ".join(districts[inputdistrict])

            print(
                f'Paikkakunnan "{inputdistrict.title()}" postinumerot: {foundnumbers_str}')
            break
        else:
            print(
                f'{coloredtext.SOS}Syöte oli virheellinen. Yritä uudelleen!{coloredtext.ENDC}')


if __name__ == '__main__':
    main()
