# lets decorate get_text fucntion with 3 other functions:
# BASIC APPROACH

def p_decorate(func):
   def func_wrapper(name):
       return "<p>{0}</p>".format(func(name))
   return func_wrapper

def strong_decorate(func):
    def func_wrapper(name):
        return "<strong>{0}</strong>".format(func(name))
    return func_wrapper

def div_decorate(func):
    def func_wrapper(name):
        return "<div>{0}</div>".format(func(name))
    return func_wrapper

def get_text(name):
    return "lorem ipsum, {0} dolor sit amet".format(name)

get_text = div_decorate(p_decorate(strong_decorate(get_text)))

print(get_text('Dawid'))

# for PYTHON DECORATOR SYNTAX see dec4.py
