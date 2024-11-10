import docx

docx_file = 'dictionary.docx'
txt_file = 'dictionary.txt'

doc=docx.Document(docx_file)

txt= '\n'.join([para.text for para in doc.paragraphs])
file=open(txt_file, 'w', encoding='utf-8')
file.write(txt)
file.close()
