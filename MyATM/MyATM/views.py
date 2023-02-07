from django.http import HttpResponse
from django.template import Template, Context

def home(request):

    html_file=open("MyATM\mytemplates\index.html")
    html_template=Template(html_file.read())
    html_file.close()
    context=Context()
    final_file = html_template.render(context)
    return HttpResponse(final_file)

