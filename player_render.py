from livereload import Server, shell


def rebuild():
    pass

rebuild()

server = Server()
server.watch('index.html', rebuild)
server.serve(root='docs/_build/html')