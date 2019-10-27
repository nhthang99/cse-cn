from PyQt5.QtCore import QAbstractListModel
from PyQt5.QtCore import Qt


class MessageModel(QAbstractListModel):
    def __init__(self, *args, messages=None, **kwargs):
        super(MessageModel, self).__init__(*args, **kwargs)
        self.messages = messages or []

    def data(self, index, role):
        if role == Qt.DisplayRole:
            status, text = self.messages[index.row()]
            return text

    def rowCount(self, index):
        return len(self.messages)
