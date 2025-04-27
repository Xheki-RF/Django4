from jinja2 import Template, FunctionLoader, Environment


# Module {{}}
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     @property
#     def getName(self):
#         return self.name

#     @property
#     def getAge(self):
#         return self.age

# per = Person("Pavel", 230)
# per = {"name": "Pavel", "age": 25}

# tm = Template("I am {{per.age}} years " \
# "old and my name is {{per.name}}")
# msg = tm.render(per=per)


# Module {%raw%}, {%endraw}
# data = """{%raw%} module
# some stuff {{name}}
# ggwp {%endraw%}"""

# tm = Template(data)
# msg = tm.render()
# print(msg)


# Screening | e
# link = """In HTML-doc links are defined as follows:
# <a href="#">Link</a>"""

# tm = Template("{{link | e}}")
# msg = tm.render(link=link)
# print(msg)


# Module {%for%}, {%endfor%}
# cities = [
#     {"id": 1, "city": "Moscow"},
#     {"id": 2, "city": "Tver"},
#     {"id": 3, "city": "Minsk"},
#     {"id": 4, "city": "Smolensk"},
#     {"id": 5, "city": "Kaluga"},
# ]

# link = """<select name="cities">
# {% for c in cities -%}
#     <option value = "{{c['id']}}">{{c['city']}}</option>
# {% endfor -%}
# </select>"""


# link = """<select name="cities">
# {% for c in cities -%}
# {% if c['id'] <= 3 -%}
#     <option value = "{{c['id']}}">{{c['city']}}</option>
# {% elif c["city"] == "Kaluga" -%}
#     <option>{{c["id"]}} {{c["city"]}}<option>
# {% else -%}
#     {{c["id"]}}
# {% endif -%}
# {% endfor -%}
# </select>"""

# tm = Template(link)
# msg = tm.render(cities=cities)
# print(msg)


# Filters
# cars = [
#     {"model": "AMG", "price": 25000},
#     {"model": "Toyota", "price": 50000},
#     {"model": "BMW", "price": 250000},
#     {"model": "SAAB", "price": 35000},
# ]

# tpl = "Price for cars: {{(car | min(attribute='price'))['model']}}"
# tpl = "Price for cars: {{car | lower}}"
# tm = Template(tpl)
# msg = tm.render(car=cars)
# print(msg)

# tpl = """
# {%- for car in cars -%}
#     Model: {% filter lower %}{{car['model']}}{% endfilter %} Car price: {{car['price'] * 2}}
# {% endfor -%}
# """
# tm = Template(tpl)
# msg = tm.render(cars=cars)
# print(msg)


# {%macro%}
# html = """
# {% macro input(name, value, type, size) -%}
#     input type = "{{type}}" name="{{name}}" value="{{value | e}}" size ="{{size}}"
# {%- endmacro %}

# {{input('Pavel', 5, 'str', 20)}}
# """

# tm = Template(html)
# msg = tm.render()
# print(msg)


# {%call%}
people = [
    {"name": "Alex", "age": 18, "weight": 64},
    {"name": "Nikola", "age": 28, "weight": 65.5},
    {"name": "Ivan", "age": 33, "weight": 70},
]

# html = """
# {% macro listuser(users_list) -%}
# <ul>
# {%- for user in users_list -%}
#     <li>{{user["name"]}} {{caller(user)}}
# {% endfor -%}
# <ul>
# {% endmacro -%}

# {% call(user) listuser(users) -%}
#     <ul>
#     <li>age: {{user['age']}}
#     <li>weight: {{user['age']}}
#     <ul>
# {% endcall -%}
# """

# tm = Template(html)
# msg = tm.render(users=people)
# print(msg)


# Function loader (load templates from files)
def loadTPL(path):
    if path == "index":
        return """Name {% filter title %}{{user["name"]}}{%endfilter%}, Age {{user["age"]}}"""
    else:
        return """Data {{user}}"""
    

file_loader = FunctionLoader(loadTPL)
env = Environment(loader=file_loader)

tm = env.get_template("index2")
msg = tm.render(user=people[0])
print(msg)