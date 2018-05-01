#!/usr/bin/env python3

import web
import json


class Todo:

    def __init__(self, order, title, body):
        self.order = order
        self.title = title
        self.body = body

DATA = [
    Todo(-1, "Test", "Lorem ipsum"),
    Todo(1, "Test2", "Lorem ipsum 2")
]


urls = (
    '/(?:(?P<id>[0-9]+))?', 'TodoResource'
)

class TodoResource:

    def GET(self, id=None):
        # TODO handle index not in list
        if id is not None:
            return json.dumps(DATA[int(id)].__dict__)
        return json.dumps([d.__dict__ for d in DATA])

    def POST(self, id=None):
        if id is not None:
            raise web.badrequest()
        DATA.append(Todo(**json.loads(web.data())))
        DATA.sort(key=lambda todo: todo.order)
        raise web.ok()

    def PUT(self, id=None):
        # TODO handle index not in list
        if id is None:
            raise web.badrequest()
        todo = DATA[int(id)]
        edits = json.loads(web.data())
        todo.order = edits.get('order', todo.order)
        todo.title = edits.get('title', todo.title)
        todo.body = edits.get('body', todo.body)
        raise web.ok()

    def DELETE(self, id=None):
        if id is None:
            DATA = []
        del DATA[int(id)]
        raise web.ok()

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.internalerror = web.debugerror
    app.run()
