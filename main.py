from modules import epaper_list, docs_extraction
from modules import text_extraction

import json
import os

print('Start data extraction...')
links = epaper_list.get_links('22. Mai')
destination_dir = os.path.join(os.getcwd(), 'files')
print(f'URLs to be processed: {len(links)}.')

print('Downloading documents...')
file_to_read = []
for name in links:
    downloaded_file = docs_extraction.from_url(links[name], destination_dir)
    file_to_read.append(downloaded_file)
print('Download completed.')

print('Extracting data from file...')
text_blocks = text_extraction.text_blocks_from_pdf(file_to_read[0], 'Baugesuchspublikation', 'BAUVERWALTUNG WÜRENLOS')
data_definition = [
    {
        'name': 'Bauherrschaft',
        'start_token': 'Bauherrschaft:',
        'end_token': 'Bauvorhaben:'
    },
    {
        'name': 'Bauvorhaben',
        'start_token': 'Bauvorhaben:',
        'end_token': 'Lage:'
    },
    {
        'name': 'Lage',
        'start_token': 'Lage:',
        'end_token': 'Zone:'
    },
    {
        'name': 'Zone',
        'start_token': 'Zone:',
        'end_token': 'Zusatzgesuch:'
    },
    {
        'name': 'Zusatzgesuch',
        'start_token': 'Zusatzgesuch:',
        'end_token': 'Gesuchsauflage'
    },
    {
        'name': 'other',
        'start_token': 'Gesuchsauflage',
        'end_token': ''
    },
]

extracted_information = [text_extraction.data_from_text_block(block, data_definition) for block in text_blocks]

# write output to file
with open(os.path.join(destination_dir, 'output.json'), 'w', encoding='utf-8') as out:
    json.dump(extracted_information, out, ensure_ascii=False, indent=4)

print(f'Extracting data Finished. Extracted information is stored in {os.path.join(destination_dir, 'output.json')}.')
