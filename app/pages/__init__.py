import os
import markdown2

pages = {
    "/": []
}

pages_path = os.path.dirname(os.path.realpath(__file__))

class Pages:
    def __init__(self):
        self.routes = {}

    def add_page(self, page):
        self.routes[page.meta["base_url"]] = page

class Page:
    def __init__(self, filename, contents):
        self.filename = filename
        self.contents = contents
        self.html = markdown2.markdown(self.contents, extras=["tables", "metadata", "fenced-code-blocks"])
        self.meta = self.html.metadata
        print(self.meta)

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