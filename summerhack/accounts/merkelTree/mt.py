import os
import hashlib
from accounts.models import Tree
import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

date = datetime.datetime.now()


#MyModel.objects.create(val=1)
class MarkleTree:
    def __init__(self, root):
        self._linelength = 30
        self._root = BASE_DIR + "/merkelTree/" + root
        self._mt = {}
        self._hashlist = {}
        self._tophash = ''
        self.buffer = ''
        self.__MT__()

    def Line(self):
        print(self._linelength * '-')

    def PrintHashList(self):
        self.Line()
        for item, itemhash in self._hashlist.iteritems():
            self.buffer += '%s %s \n' % (itemhash, item)
        self.Line()
        return

    def PrintMT(self, hash):
        value = self._mt[hash]
        item = value[0]
        child = value[1]
        self.buffer += '%s %s \n' % (hash, item)
        tree = Tree(folder_path=item, key=hash)
        tree.save()
        if not child:
            return
        for itemhash, item in child.iteritems():
            self.buffer += '    -> %s %s\n' % (itemhash, item)
            tree = Tree(folder_path=item, key=itemhash)
            tree.save()
        for itemhash, item in child.iteritems():
            self.PrintMT(itemhash)

    def MT(self):
        for node, hash in self._hashlist.iteritems():
            items = self.GetItems(node)
            value = []
            value.append(node)
            list = {}
            for item in items:
                if node == self._root:
                    list[self._hashlist[item]] = item
                else:
                    list[self._hashlist[os.path.join(node, item)]] = os.path.join(node, item)
            value.append(list)
            self._mt[hash] = value
        self._tophash = self._hashlist[self._root]

    def __MT__(self):
        self.HashList(self._root)
        # self.PrintHashList()
        self.MT()
        self.buffer += 'Merkle Tree for %s: \n' % self._root
        self.PrintMT(self._tophash)
        self.Line()

    def md5sum(self, data):
        m = hashlib.md5()
        fn = os.path.join(self._root, data)
        if os.path.isfile(fn):
            try:
                f = file(fn, 'rb')
            except:
                return 'ERROR: unable to open %s\n' % fn
            while True:
                d = f.read(8096)
                if not d:
                    break
                m.update(d)
            f.close()
        else:
            m.update(data)
        return m.hexdigest()

    def GetItems(self, directory):
        value = []
        if directory != self._root:
            directory = os.path.join(self._root, directory)
        if os.path.isdir(directory):
            items = os.listdir(directory)
            for item in items:
                value.append(item)
                # value.append(os.path.join(".", item))
            value.sort()
        return value

    def HashList(self, rootdir):
        self.HashListChild(rootdir)
        items = self.GetItems(rootdir)
        if not items:
            self._hashlist[rootdir] = ''
            return
        s = ''
        for subitem in items:
            s = s + self._hashlist[subitem]
        self._hashlist[rootdir] = self.md5sum(s)

    def HashListChild(self, rootdir):
        items = self.GetItems(rootdir)
        if not items:
            self._hashlist[rootdir] = ''
            return
        for item in items:
            itemname = os.path.join(rootdir, item)
            if os.path.isdir(itemname):
                self.HashListChild(item)
                subitems = self.GetItems(item)
                s = ''
                for subitem in subitems:
                    s = s + self._hashlist[os.path.join(item, subitem)]
                if rootdir == self._root:
                    self._hashlist[item] = self.md5sum(s)
                else:
                    self._hashlist[itemname] = self.md5sum(s)
            else:
                if rootdir == self._root:
                    self._hashlist[item] = self.md5sum(item)
                else:
                    self._hashlist[itemname] = self.md5sum(itemname)


def MTDiff(mt_a, a_tophash, mt_b, b_tophash):
    buffer = ""
    if a_tophash == b_tophash:
        buffer += "Top hash is equal for {} and {}\n".format(mt_a._root, mt_b._root)
    else:
        a_value = mt_a._mt[a_tophash]
        a_child = a_value[1]  # retrive the child list for merkle tree a
        b_value = mt_b._mt[b_tophash]
        b_child = b_value[1]  # retrive the child list for merkle tree b

        for itemhash, item in a_child.iteritems():
            try:
                if b_child[itemhash] == item:
                    pass
                    #buffer += "Info: SAME : {}\n".format(item)
            except:
                buffer += "Info: DIFFERENT : {}\n".format(item)
                temp_value = mt_a._mt[itemhash]
                if len(temp_value[1]) > 0:  # check if this is a directory
                    diffhash = list(set(b_child.keys()) - set(a_child.keys()))
                    buffer += MTDiff(mt_a, itemhash, mt_b, diffhash[0])
    return buffer


def TestIfExist(mt_a, a_tophash):
    tree = Tree.object.get(key=a_tophash)
    if tree is None:
        Tree.object.get(key=a_tophash)










# if __name__ == "__main__":
#    buffer = ""
#    mt_a = MarkleTree('testA')
# print(mt_a._mt)
#    mt_b = MarkleTree('testB')
#    buffer += "{}{}".format(mt_a.buffer, mt_b.buffer)
#    buffer += MTDiff(mt_a, mt_a._tophash, mt_b, mt_b._tophash)
#    print(buffer)
