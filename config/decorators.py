from flask import request


def request_body(class_):
    def wrap(f):
        def decorator(*args):
            obj = class_(**request.get_json())
            return f(obj, *args)
        return decorator
    return wrap
