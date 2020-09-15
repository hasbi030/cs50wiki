from django.shortcuts import render, redirect
from django import forms
import markdown2
import random
from . import util


class NewWikiEntry(forms.Form):
    title = forms.CharField(label="Title")
    content = forms.CharField(widget=forms.Textarea, label="Content")

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    content = util.get_entry(title)
    if content == None:
        content = "##Page Does not Exist"
    content = markdown2.markdown(content)
    return render(request, "encyclopedia/entry.html",{
        "content": content,
        "title": title
    })

def search(request):
    query = request.GET.get('q')

    if query in util.list_entries():
        return redirect("entry", title=query)
    
    return render(request, "encyclopedia/search.html",{
        "entries": util.search(query), 
        "query": query
    })
    

def add(request):
    if request.method == "POST":
        form = NewWikiEntry(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            
            if util.get_entry(title) != None:
                return render(request, "encyclopedia/add.html", {
                    "form": form,
                    "message": "This Title is used on Another Page"
                })
            else:
                util.save_entry(title, content)
                return redirect('entry', title=title)
    return render(request, "encyclopedia/add.html",{
        "form": NewWikiEntry,
        "message": ""
    })
def edit(request, title):
    if request.method == "POST":
        content = request.POST.get('content')
        print(content)
        util.save_entry(title, content)
        return redirect("entry", title=title)
    else:
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
            "title":title,
            "content":content
        })
def random_query(request):
    entries = util.list_entries()
    length = len(entries)-1
    query = entries[random.randint(0, length)]
    return redirect("entry", title=query)