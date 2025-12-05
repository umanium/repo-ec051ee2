from modules import text_extraction

def test_extract_text_blocks():
    file_name = 'tests/files/test_doc.pdf'
    start_token = 'Baugesuchspublikation'
    end_token = 'BAUVERWALTUNG WÜRENLOS'

    text_blocks = text_extraction.text_blocks_from_pdf(file_name, start_token, end_token)
    
    expected = [
        ['Baugesuch Nr.: 202536', 'Bauherrschaft: Ortsbürgergemeinde', 'Würenlos, Schulstrasse 26,', '5436 Würenlos', 'Bauvorhaben:', 'Dachsanierung', 'Lage:', 'Parzelle 4885 (Plan 25),', 'Forsthaus ‚Tägerhard‘', 'Zone:', 'Ausserhalb Bauzone - Wald', 'Zusatzgesuch:', 'Departement Bau, Verkehr', 'und Umwelt', 'Gesuchsauflage vom 23. Mai bis 23. Juni 2025', 'während der ordentlichen Schalterstunden im', 'Büro der Bauverwaltung. Allfällige Einwendun-', 'gen sind innerhalb der Auflagefrist im Doppel', 'an den Gemeinderat zu richten und haben ei-', 'nen Antrag und eine Begründung zu enthalten.', 'BAUVERWALTUNG WÜRENLOS'],
        ['Baugesuch Nr.: 202531', 'Bauherrschaft: Markwalder René,', 'Büntenstrasse 43,', '5436 Würenlos', 'Bauvorhaben:', 'Erweiterung Siloanlage und', 'Umnutzung Stall (teilweise)', 'in Milchkuhliegeboxen', 'Lage:', 'Parzelle 3105 (Plan 33),', 'Büntenstrasse 43', 'Zone:', 'Ausserhalb Bauzone –', 'Landschaftsschutzzone', 'Zusatzgesuch:', 'Departement Bau, Verkehr', 'und Umwelt', 'Gesuchsauflage vom 23. Mai bis 23. Juni 2025', 'während der ordentlichen Schalterstunden im', 'Büro der Bauverwaltung. Allfällige Einwendun-', 'gen sind innerhalb der Auflagefrist im Doppel', 'an den Gemeinderat zu richten und haben ei-', 'nen Antrag und eine Begründung zu enthalten.', 'BAUVERWALTUNG WÜRENLOS']
    ]

    assert(text_blocks == expected)

def test_extract_data():
    text_block = ['Baugesuch Nr.: 202536', 'Bauherrschaft: Ortsbürgergemeinde', 'Würenlos, Schulstrasse 26,', '5436 Würenlos', 'Bauvorhaben:', 'Dachsanierung', 'Lage:', 'Parzelle 4885 (Plan 25),', 'Forsthaus ‚Tägerhard‘', 'Zone:', 'Ausserhalb Bauzone - Wald', 'Zusatzgesuch:', 'Departement Bau, Verkehr', 'und Umwelt', 'Gesuchsauflage vom 23. Mai bis 23. Juni 2025', 'während der ordentlichen Schalterstunden im', 'Büro der Bauverwaltung. Allfällige Einwendun-', 'gen sind innerhalb der Auflagefrist im Doppel', 'an den Gemeinderat zu richten und haben ei-', 'nen Antrag und eine Begründung zu enthalten.', 'BAUVERWALTUNG WÜRENLOS']
    data_definition = [
        {
            'name': 'Baugesuch Nr.',
            'start_token': 'Baugesuch Nr.:',
            'end_token': 'Bauherrschaft:'
        },
        {
            'name': 'Bauherrschaft',
            'start_token': 'Bauherrschaft:',
            'end_token': 'Bauvorhaben:'
        },
        {
            'name': 'EOF test',
            'start_token': 'BAUVERWALTUNG',
            'end_token': ''
        }
    ]

    extracted_data = text_extraction.data_from_text_block(text_block, data_definition)

    expected = {
        'Baugesuch Nr.': '202536',
        'Bauherrschaft': 'Ortsbürgergemeinde Würenlos, Schulstrasse 26, 5436 Würenlos',
        'EOF test': 'WÜRENLOS'
    }

    assert(extracted_data == expected)