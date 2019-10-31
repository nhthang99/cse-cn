from PyQt5.QtCore import QAbstractListModel, QModelIndex, Qt, QVariant

class Model(QAbstractListModel):
    def __init__(self, *args):
        QAbstractListModel.__init__(self, *args)
        self.items=[]
        self.modelDict = None

    def rowCount(self, parent=QModelIndex, **kwargs):
        return len(self.items)   

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.ItemDataRole:
                return self.data(index)
            elif role==Qt.DisplayRole:
                return QVariant(self.items[index.row()])

    def getData(self, data):
        return self.modelDict[str(data)]

    def addItems(self, instDict):
        for key in instDict:
            inst=instDict.get(key)
            index=QModelIndex()
            self.beginInsertRows(index, 0, 0)
            self.setData(index, QVariant(inst), Qt.DisplayRole)
        self.items.extend(instDict)
        self.endInsertRows()
        self.modelDict = instDict