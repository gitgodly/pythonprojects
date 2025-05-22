class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def display(self):
        print(f"Title: {self.title}\nContent: {self.content}")