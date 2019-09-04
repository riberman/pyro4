import Pyro4

@Pyro4.expose
class Tag(object):

    def get_tag(self):
        global code
        result = code
        code = code + 1
        return "%09d" % result

Pyro4.config.HOST = '127.0.0.1'
code = 000000001
daemon = Pyro4.Daemon()
uri = daemon.register(Tag)

print("Ready. Object uri =", uri)
daemon.requestLoop()
