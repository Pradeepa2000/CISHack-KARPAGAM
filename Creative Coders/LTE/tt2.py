import pyttsx3
import PyPDF2
book = open("/home/arpit/Desktop/python_tutorial.pdf", "rb")
pdf_reader = PyPDF2.PdfFileReader(book)

# if pdf contains more then one pages
pages = pdf_reader.numPages
print("Total Pages: ", pages)


speaker = pyttsx3.init()  # initialization
speaker.setProperty("rate", 125)  # set speaking speed

for page_num in range(pages):
    print("Current page: ", page_num + 1)
    page = pdf_reader.getPage(page_num)  # getting each pages from pdf

    text = page.extractText()  # extracting text from current page
    # print(text)
    speaker.say(text)  # now extract text will passed here to listen
    speaker.runAndWait()
