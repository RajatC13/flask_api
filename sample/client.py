import requests, json

class Ring():

    def __init__(self,url='http://127.0.0.1:5000'):
        self.url = url


    def __call__(self, *args, **kwargs):
        newurl = self.url +"/todos"
        lists = requests.get(newurl)
        return str(lists.json())


    def append(self, name):
        newurl = self.url +"/todos"
        resp1 = requests.post(newurl, data={"name":name})
        #print(resp1.json())
        pass


    def __getitem__(self, index):
        newurl = self.url +"/todos/"+ str(index)
        print(newurl)
        resp1 = requests.get(newurl)
        return str(resp1.json())


def test():
    '''DO NOT CHANGE THIS TEST CODE OR YOU WILL GET ZERO!'''
    ring = Ring('http://127.0.0.1:5000')
    ring.append('Chuck')
    ring.append('Alice')
    ring.append('Bob')
    print(ring[0])
    print(ring())
    ring.append('Charlie')
    print(ring[0])
    print(ring())

    """
    print(ring[0])
    print(ring())
    ring.append('Charlie')
    print(ring[0])
    print(ring())
    """

if __name__ == "__main__":
    test()
