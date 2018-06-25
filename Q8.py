from xml.dom import minidom
doc = minidom.parse('data.xml')
books = doc.getElementsByTagName("book")
for book in books:
    category =  book.getAttribute("category")
    title = book.getElementsByTagName("author")[0].firstChild.data
    year = book.getElementsByTagName("year")[0].firstChild.data
    price = book.getElementsByTagName("price")[0].firstChild.data
    print("Category:%s Title:%s Year:%s Price:%s" % (category, title, year, price))
