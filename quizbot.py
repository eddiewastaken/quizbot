import pytesseract, re, pprint
from PIL import Image, ImageGrab, ImageEnhance
from apiclient.discovery import build

#counts instances of word in string
def count(word, string):
    return sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(word), string))

#create an api service
service = build("customsearch", "v1", developerKey="####################")

#grab a screenshot bound by coords - convert to grey
img = ImageGrab.grab(bbox=(833,158,1153,477))
img = img.convert("L")

#initiate tesseract OCR, perform OCR on screenshot
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract'
text = pytesseract.image_to_string(img)
#print(text)

#removes line breaks in question and answers
textclean = '\r\n'.join(line for line in text.splitlines() if line)
textclean = textclean.splitlines()
textclean = [x.lower() for x in textclean]

#grabs answers to strings
a = (textclean)[len(textclean)-3].lower()
b = (textclean)[len(textclean)-2].lower()
c = (textclean)[len(textclean)-1].lower()

#puts options into list, then subtracts to leave question
options = []
options.append(a)
options.append(b)
options.append(c)
question=[i for i in textclean+options if i not in textclean or i not in options]

#puts resulting question into string
q = ' '.join(question)

#initialise result
result = []

#perform query and append snippets to list
for i in range(2):
        res = service.cse().list(
        q=q,
        cx='####################',
        googlehost='google.com',
        start=str(i*10+1)
        ).execute()
        for x in res['items']:
            result.append(x['snippet'])
            
#combine all snippets into one block of text, and make it lowercase
joinedresult = (" ".join(result)).lower()

#get counts of whole term
acount = count(a.lower(), joinedresult)
bcount = count(b.lower(), joinedresult)
ccount = count(c.lower(), joinedresult)

#reverse and add to count if 2 words
if len(a.split()) == 2:
    acount+=count(' '.join(reversed(a.split())), joinedresult)
if len(b.split()) == 2:
    bcount+=count(' '.join(reversed(b.split())), joinedresult)
if len(c.split()) == 2:
    ccount+=count(' '.join(reversed(c.split())), joinedresult)

#add word counts to score
for x in a.split():
    acount+=count(x, joinedresult)
for x in b.split():
    bcount+=count(x, joinedresult)
for x in c.split():
    ccount+=count(x, joinedresult)

#add totals
total = acount+bcount+ccount+0.1

#display totals as percentage rounded to 2 d.p.
print(a + " percentage: " + str(round((acount/(total)*100)+0.1, 2)))
print(b + " percentage: " + str(round((bcount/(total)*100)+0.1, 2)))
print(c + " percentage: " + str(round((ccount/(total)*100)+0.1, 2)))
