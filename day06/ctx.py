
class CtxMgr:
    def __enter__(self):
        print('hello with')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exiting')

    def p(self):
        print('hihihi')


a = CtxMgr()
print('Jeszcze przed with')

with a as b:
    b.p()

print('koniec')
