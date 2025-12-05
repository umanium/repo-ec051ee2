from modules import epaper_list

def test_get_links():
    links = epaper_list.get_links('22. Mai')

    assert(type(links) == dict)
    assert('Woche 21/Limmatwelle 22. Mai' in links)
