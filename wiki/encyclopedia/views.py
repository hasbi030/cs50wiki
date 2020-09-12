from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def wiki(request, entry):
    print(util.get_entry(entry))
    return render(request, "encyclopedia/wiki.html", {
        "entry": util.get_entry(entry.capitalize()),
        "title": entry.capitalize()
    })
