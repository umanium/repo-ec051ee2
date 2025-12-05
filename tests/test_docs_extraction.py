from modules import docs_extraction
import os

def test_get_document_from_url():
    destination_dir = os.path.join(os.getcwd(), 'tests/files')
    url = 'https://issuu.com/az-anzeiger/docs/woche_21_limmatwelle_22._mai?mode=embed&layout=white'

    downloaded_file = docs_extraction.from_url(url, destination_dir)
    print(downloaded_file)

    os.remove(downloaded_file)
    assert('tests/files/20250522_WOZ_LIWANZ.pdf' in downloaded_file)