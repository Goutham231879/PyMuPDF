import fitz

doc = fitz.open("ex.pdf")

print(doc.page_count)

page = doc.load_page(0)

text = page.get_text()

print(text)

doc.close()

