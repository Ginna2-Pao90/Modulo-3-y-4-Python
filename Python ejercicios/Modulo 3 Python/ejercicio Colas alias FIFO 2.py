class QueueError(IndexError):
    pass


class primero:
    def __init__(self):
        self.primero =[]

    def put(self, c):
        self.primero.insert(0,c)

    def get(self):
        if len(self.primero)>0:
            c = self.primero[-1]
            del self.primero[-1]
            return c
        else:
            raise QueueError

class SuperQueue(primero):
    def vacio(self):
        return len(self.primero) == 0

que = SuperQueue()
que.put(19)
que.put("gato")
que.put(True)
for i in range(4):
    if not que.vacio():
        print(que.get())
    else:
        print("Cola vacía")
