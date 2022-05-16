# Strings
text = "X-DSPAM-Confidence: 0.8475"
you = text.find('0.8475')
me =float(text[you:])
print (me)
