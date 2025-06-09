from mako.template import Template
import json


# Load the data from JSON file
with open('site/src/data.json', 'r') as f:
    data = json.load(f)


# Load the index.html template
with open('site/src/index.html', 'r') as f:
    template_string = f.read()


class MyObject:
    def __init__(self, d=None):
        if d is not None:
            for key, value in d.items():
                setattr(self, key, value)


o = MyObject(data)     

# Render the template with the data
print(Template(template_string).render(data=o))
