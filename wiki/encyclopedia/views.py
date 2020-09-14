from django.shortcuts import render
from django import forms

from . import util

class NewWikiEntry(forms.Form):
    title = forms.CharField(label="Title")
    content = forms.CharField(widget=forms.Textarea, label="Content")

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
    if request.method == "POST":
        form = NewWikiEntry(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            
            if util.get_entry(title) != None:
                print("it already exists")
                return render(request, "encyclopedia/add.html", {
                    "form": form,
                    "message": "This Title is used on Another Page"
                })
            else:
                util.save_entry(title, content)
                return render(request,"encyclopedia/wiki.html",{
                    "entry": util.get_entry(title),
                    "title": title
                })
    return render(request, "encyclopedia/add.html",{
        "form": NewWikiEntry,
        "message": ""
    })

def random(request):
    return render(request, "encyclopedia/random.html")