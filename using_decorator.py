def decorator_tag_div(fn):
    def wrapped():
        return '<div>' + fn() + '</div>'
    return wrapped

def decorator_tag_span(fn):
    def wrapped():
        return '<span>' + fn() + '</span>'
    return wrapped

def decorator_tag_a(fn):
    def wrapped():
        return '<a>' + fn() + '</a>'
    return wrapped

@decorator_tag_div
@decorator_tag_a
@decorator_tag_span
def name():
    return 'Hello'

print(name())