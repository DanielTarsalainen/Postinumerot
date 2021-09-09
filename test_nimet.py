import nimet


def test_lyhenna_j_l_runeberg():
    lyhennetty = nimet.lyhenna_nimi("Johan", "Ludvig", "Runeberg")

    assert lyhennetty == 'J. L. Runeberg'


# test_lyhenna_j_l_runeberg()  # tämä halutaan automatisoida

def test_lyhenna_a_i_virtanen():
    ai_virtanen = nimet.lyhenna_nimi('Artturi', 'Ilmari', 'Virtanen')

    assert ai_virtanen == 'A. I. Virtanen'


def test_ruotsalainen_o():
    erikoistapaus = nimet.lyhenna_nimi("Åke", "Åke", "Åkesson")

    assert erikoistapaus == 'Å. Å. Åkesson'
