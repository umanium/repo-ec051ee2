import pymupdf

'''
Extract text blocks from a pdf file based on start token and end token.
Text between the start token and end token will be returned as one block.
This method uses pymupdf as the library.

:param doc_path: a PDF document location
:param start_token: start of block to be extracted
:param end_token: end of block to be extracted
:return: text blocks extracted from the document (array of array of string)
'''
def text_blocks_from_pdf(doc_path, start_token, end_token):
    doc = pymupdf.open(doc_path)
    lines = []
    for page in doc:
        text = page.get_text()
        lines += text.split('\n')

    text_blocks = []
    current_block = []
    is_block = False
    for line in lines:
        if is_block:
            current_block.append(line)

        if start_token in line:
            is_block = True
        elif end_token in line:
            is_block = False
            text_blocks.append(current_block)
            current_block = []

    return text_blocks

'''
Extract data from text block extracted by text_blocks_from_pdf to a specified format.

:param text_block: text block to be processed
:param data_definition: an array of dictionary depicting data definition. Every definition must be consisting of name, start_token, end_token
:return: extracted data as a dictionary, with names in data_definition as keys
'''
def data_from_text_block(text_block, data_definition):
    extracted_data = {}
    for definition in data_definition:
        current_block = []
        is_block = False

        start_token = definition['start_token']
        end_token = definition['end_token']
        for line in text_block:
            if is_block:
                current_block.append(line)

            if start_token in line:
                is_block = True
                current_block.append(line)
            elif end_token != '' and end_token in line:
                is_block = False
                break
        
        content_line = ' '.join(current_block)
        content_line = content_line.split(start_token)[1]
        if end_token:
            content_line = content_line.split(end_token)[0]
        
        extracted_data[definition['name']] = content_line.strip()
        
    return extracted_data