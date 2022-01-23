import os
import markdown

pages = {
    "/": []
}

pages_path = os.path.dirname(os.path.realpath(__file__))

class Pages:
    def __init__(self):
        self.pages = {}

    def add_page(self, page):
        self.pages[page.meta["base_url"][0]] = page

class Page:
    def __init__(self, filename, contents):
        self.md = markdown.Markdown(extensions = ['meta'])
        self.filename = filename
        self.contents = contents
        self.html = self.md.convert(self.contents)
        self.meta = self.md.Meta

def create_pages():
    _pages = Pages()
    for filename in os.listdir(pages_path):
        f = os.path.join(pages_path, filename)
        if os.path.isfile(f) and f.endswith(".md"):
            with open(f, "r") as file:
                contents = file.read()

            page = Page(f, contents)
            _pages.add_page(page)

    return _pages