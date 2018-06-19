# Python's Decorator Syntax
# We dont have to 'get_text = p_decorate(get_text)'. There is a neat shortvut for that,
# which is to mention the name of the decorating function before the function to be decoratedselfself.
# The name of the decorator should be preprended with an @ symbol:
def p_decorate(func):
    def func_wrapper(name):
        return "<p>{0}</p>".format(func(name))
    return func_wrapper

@p_decorate
def get_text(name):
    return "lorem ipsum, {0} dolor sit amet".format(name)

print(get_text("Dawid"))
