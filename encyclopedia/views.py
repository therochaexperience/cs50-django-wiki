from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from . import util, forms
from django.urls import reverse
from django.http import Http404

import markdown2, random

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def renderEntry(request, title):
    entry = markdown2.markdown(util.get_entry(title))
    return render(request, "encyclopedia/entry.html", {
        "entry": entry,
        "entryTitle": title
    })

def entry(request, title):
    try:
        return renderEntry(request, title)
    except:
        return render(request, "encyclopedia/error.html", {
            "entry": title,
        })

def search(request):
    q = request.GET['q']
    try: 
        return renderEntry(request, q)
    except:
        searchContext = {
            "q": q,
            "entries": util.list_entries_substring(q)
        }
        if len(searchContext["entries"]) > 0:
            return render(request, "encyclopedia/search.html", searchContext)
        else:
            return render(request, "encyclopedia/error.html", {
                "entry": q,
            })

def randomEntry(request):
    entries = util.list_entries()
    entry = random.choice(entries)
    return HttpResponseRedirect(reverse('entry', kwargs={'title': entry}))

def redirect(request):
    return HttpResponseRedirect(reverse('index'))

def newpage(request):
    if request.method == 'POST':
        form = forms.NewEntryPageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['entryTitle']
            content = form.cleaned_data['entryContent']
            if util.get_entry(title):                
                return render(request, "encyclopedia/newpage.html", {
                    'form': form,
                    'pageExist': True
                }) 
            else:
                util.save_entry(title, content)
                return HttpResponseRedirect(reverse('entry', kwargs={'title': title}))
        else:
            raise Http404
    else:
        form = forms.NewEntryPageForm()
        return render(request, "encyclopedia/newpage.html", {
            'form': form,
            'pageExist': False
        })

def editpage(request, title):
    if request.method == 'POST':
        form = forms.EditEntryPageForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['entryContent'].replace('\n','')
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse('entry', kwargs={'title': title}))
        else:
            raise Http404
    else:
        original_page = {
            "entryContent" : util.get_entry(title)
        }
        form = forms.EditEntryPageForm(initial=original_page)
        return render(request, "encyclopedia/editpage.html", {
            "entryTitle": title,
            'form': form
        })

