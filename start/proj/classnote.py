from datetime import datetime

class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "title": self.title,
            "content": self.content,
            "timestamp": self.timestamp
        }

    @staticmethod
    def from_dict(data):
        note = Note(data["title"], data["content"])
        note.timestamp = data["timestamp"]
        return note
