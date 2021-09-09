import http_pyynto


postalinfo = http_pyynto.fetch_postaldata()


def seek_district(number):
    postalinfo = http_pyynto.fetch_postaldata()

    if number in postalinfo:
        return postalinfo[number]
    else:
        return 'Unindentified'


def main():
    postalnumber = input('Kirjoita postinumero: ')

    print(seek_district(postalnumber))


if __name__ == '__main__':
    main()
