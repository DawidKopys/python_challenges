# "In the context of design patterns, decorators dynamically alter the functionality of a function,
#  method ir ckass without having to directly use subclasses"

# "This is ideal when you need to extend the functionality of functions that you dont't want to modify"

# "...decorators work as wrappers, modifying the behavior of the code before and after a target
#  function execution, without the need to modify the function itself, augumenting the original
#  functionality, thus decorating it"

# a function that wraps the string output of another function by p tags:
def get_text(name):
    return "lorem ipsum, {0} dolor sit amet".format(name)

def p_decorate(func):
    def func_wrapper(name):
        return "<p>{0}</p>".format(func(name))
    return func_wrapper

my_get_text = p_decorate(get_text)
print(my_get_text('Dawid'))

# To have get_text itself be decorated by p_decorate, we just have to
# assign get_text to the result of p_decorate.
get_text = p_decorate(get_text)

print(get_text('Dawid'))

# other changes

# Python's Decorator Syntax - see dec2.py
# We dont have to 'get_text = p_decorate(get_text)'. There is a neat shortvut for that,
# which is to mention the name of the decorating function before the function to be decoratedselfself.
# The name of the decorator should be preprended with an @ symbol:
