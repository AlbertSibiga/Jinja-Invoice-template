from jinja2 import Environment, FileSystemLoader
import pdfkit
import os
import time
def html2pdf(customer_name):
    config = pdfkit.configuration(wkhtmltopdf = r"C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
    # options = {
    #         'page-size': 'Letter',
    #         'margin-top': '0.35in',
    #         'margin-right': '0.75in',
    #         'margin-bottom': '0.75in',
    #         'margin-left': '0.75in',
    #         'encoding': "UTF-8",
    #         'no-outline': None,
    #         'enable-local-file-access': None
    #     }
    pdfkit.from_file(customer_name + ".html", customer_name + ".pdf", configuration = config)

max_score = 100

test_name = "Python Challenge"
students = [
    {"name": "Sandrine", "score": 100},
    {"name": "Gergeley", "score": 87},
    {"name": "Frieda", "score": 92},
]

customer_count = [
    {"name" : "customer1"},
    {"name" : "customer2"},
    {"name" : "customer3"},
    {"name" : "customer4"},
]

sub_total = 0
tax = 32.5
total = 0
# template_indexes = ["30", "31", "32", "33", "34"]
template_indexes = ["34"]


items = [
    {
        "name" : "item1",
        "price" : 100,
        "quantity" : 5
    },
    {
        "name" : "item2",
        "price" : 120,
        "quantity" : 1
    },
    {
        "name" : "item3",
        "price" : 130,
        "quantity" : 3
    },
    {
        "name" : "item4",
        "price" : 100,
        "quantity" : 5
    },
    {
        "name" : "item5",
        "price" : 120,
        "quantity" : 1
    },
    {
        "name" : "item6",
        "price" : 130,
        "quantity" : 3
    },
    {
        "name" : "item7",
        "price" : 100,
        "quantity" : 5
    },
    {
        "name" : "item8",
        "price" : 120,
        "quantity" : 1
    },
    {
        "name" : "item9",
        "price" : 130,
        "quantity" : 3
    },
]
for item in items:
    sub_total += item['price'] * item['quantity']
total = tax + sub_total
environment = Environment(loader=FileSystemLoader("templates/"))
invoice_loop = 1
    
def html_gen(invoice_loop, template_name):
    template = environment.get_template(template_name + ".html")
    filename = f"{template_name.lower()}.html"
    content = template.render(
        items = items,
        sub_total = sub_total,
        tax = tax,
        total = total,
        invoice_no = invoice_loop
    )
    with open(filename, mode="w", encoding="utf-8") as message:
        message.write(content)
        invoice_loop += 1

for template_index in template_indexes:
    html_gen(invoice_loop, template_index)     

for template_index in template_indexes:
    html2pdf(template_index)
