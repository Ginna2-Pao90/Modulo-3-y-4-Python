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


que = primero()
que.put(10)
que.put("gato")
que.put(True)
try:
    for i in range(4):
        print(que.get())
except:
    print("Error de Cola")