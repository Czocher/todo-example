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

    @staticmethod
    def _get_todo_or_400(id):
        try:
            return DATA[int(id)]
        except IndexError:
            raise web.badrequest()

    def GET(self, id=None):
        if id is not None:
            todo = self._get_todo_or_400(id)
            return json.dumps(todo.__dict__)
        return json.dumps([d.__dict__ for d in DATA])

    def POST(self, id=None):
        if id is not None:
            raise web.badrequest()
        DATA.append(Todo(**json.loads(web.data())))
        DATA.sort(key=lambda todo: todo.order)
        raise web.ok()

    def PUT(self, id=None):
        if id is None:
            raise web.badrequest()
        todo = self._get_todo_or_400(id)
        edits = json.loads(web.data())
        todo.order = edits.get('order', todo.order)
        todo.title = edits.get('title', todo.title)
        todo.body = edits.get('body', todo.body)
        raise web.ok()

    def DELETE(self, id=None):
        if id is None:
            DATA = []
        try:
            del DATA[int(id)]
        except IndexError:
            raise web.badrequest()
        raise web.ok()

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.internalerror = web.debugerror
    app.run()
