from django.shortcuts import render
from markdown2 import Markdown

from . import util

def convert_md_to_html(title):
    content = util.get_entry(title)
     markdowner = Markdown()
    if content == None:
       return None
    else:
     return markdowner.convert("*boo!*")

def index(request):
   return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

