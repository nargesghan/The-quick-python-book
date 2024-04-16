'''In this lab, you create classes to represent an HTML document. To keep things simple,
assume that each element can contain only text and one subelement. So the <html>
element contains only a <body> element, and the <body> element contains (optional)
text and a <p> element that contains only text.
The key feature to implement is the __str__() method, which in turn calls its
subelement’s __str__() method, so that the entire document is returned when the
str() function is called on an <html> element. You can assume that any text comes
before the subelement.
Here’s example output from using the classes:
para = p(text="this is some body text")
doc_body = body(text="This is the body", subelement=para)
doc = html(subelement=doc_body)
print(doc)
<html>
<body>
This is the body
<p>
this is some body text
</p>
</body>
</html>'''

class element:
    def __init__(self, text=None, subelement=None):
        self.subelement = subelement
        self.text = text

    def __str__(self):
        value = "<{}>\n".format(self.__class__.__name__)
        if self.text:
            value += "{}\n".format(self.text)
        if self.subelement:
            value += str(self.subelement)
        value += "</{}>\n".format(self.__class__.__name__)
        return value

class html(element):
    def __init__ (self, text=None, subelement=None):
        super().__init__(text, subelement)

    def __str__(self):
        return super().__str__()

class body(element):
    def __init__ (self, text=None, subelement=None):
        super().__init__(text, subelement)

    def __str__(self):
        return super().__str__()

class p(element):
    def __init__(self, text=None, subelement=None):
        super().__init__(text, subelement)

    def __str__(self):
        return super().__str__()

para = p(text="this is some body text")
doc_body = body(text="This is the body", subelement=para)
doc = html(subelement=doc_body)
print(doc)
