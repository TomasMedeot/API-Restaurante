from functools import wraps

def add_variables(**kwargs):
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs_inner):
            kwargs_inner.update(kwargs)
            return f(*args, **kwargs_inner)
        return decorated
    return decorator
