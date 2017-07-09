import re

text = 'yeah, but no, but yeah, but no, but yeah'

# use built-in string method for simple replacements
text.replace('yeah', 'yes')

# for more complicated examples, use re.sub()
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
# use regex groups and then use the group numbers to switch them up
re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
