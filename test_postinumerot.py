from http_pyynto import fetch_postaldata
import postinumerot

postalinfo = fetch_postaldata()


def test_finds_only_one_postalcode():
    numbers = postinumerot.groupby_district(postalinfo)

    result = numbers["KORVATUNTURI"]

    result_str = " ".join(result)

    assert result_str == "99999"


def test_finds_two_postalcodes():
    numbers = postinumerot.groupby_district(postalinfo)

    numbers["JOKELA"].sort()

    result = numbers["JOKELA"]

    result_str = ", ".join(result)

    assert result_str == "05400, 05401"


def test_finds_many_postalcodes():
    numbers = postinumerot.groupby_district(postalinfo)

    numbers["JÄRVENPÄÄ"].sort()

    result = numbers["JÄRVENPÄÄ"]

    result_str = ", ".join(result)

    assert result_str == "04400, 04401, 04410, 04420, 04430, 04431, 04440"


def test_doesnt_find_bug_one():
    numbers = postinumerot.groupby_district(postalinfo)

    result = "SMARTPSOT" in numbers

    assert result == False


# I found out that SMART-POST doesn't exist in the JSON data anymore, so there wasn't anything to fix
def test_doesnt_find_bug_two():
    numbers = postinumerot.groupby_district(postalinfo)

    result = "SMART-POST" in numbers

    assert result == False


def test_doesnt_find_bug_three():
    numbers = postinumerot.groupby_district(postalinfo)

    result = "SMART POST" in numbers

    assert result == False


def test_finds_the_right_locale():
    numbers = postinumerot.groupby_district(postalinfo)

    result = "SMARTPOST" in numbers

    assert result == True


def test_finds_postalnumbers_with_smartpost():
    numbers = postinumerot.groupby_district(postalinfo)

    numbers["SMARTPOST"].sort()

    result = numbers["SMARTPOST"]

    result_str = ", ".join(result)

    ultimate_result = "00104, 00124, 00134, 00144, 00154, 00164, 00174, 00184, 00204, 00214, 00224, 00234, 00244, 00254" in result_str

    assert ultimate_result == True


def test_shows_cleanup_works_one():
    result = postinumerot.cleanup_district("H ä m-eenlinna")

    assert result == "Hämeenlinna"


def test_shows_cleanup_works_two():
    result = postinumerot.cleanup_district("SMARTPSOT")

    assert result == "SMARTPOST"
