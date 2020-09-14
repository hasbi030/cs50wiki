from django.shortcuts import render

from . import util


def index(request):
    query = request.GET.get("q")
    if query != None:
        return render(request, "encyclopedia/wiki.html", {
            "entry": util.get_entry(query),
            "title": query.capitalize()
    })
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def wiki(request, entry):
    query = request.GET.get("q")
    if query == None:
        return render(request, "encyclopedia/wiki.html", {
            "entry": util.get_entry(entry),
            "title": entry.capitalize()
    })
    else:
        return render(request, "encyclopedia/wiki.html", {
            "entry": util.get_entry(query),
            "title": query.capitalize()
    })


def add(request):
    return render(request, "encyclopedia/add.html")

def random(request):
    return render(request, "encyclopedia/random.html")