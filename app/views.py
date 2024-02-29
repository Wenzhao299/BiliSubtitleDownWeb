from django.shortcuts import render, HttpResponse
import app.subtitle_down as sd
import app.global_var as gv

# Create your views here.
def index(request):
    gv.set_obj('cookie', request.POST.get("cookie"))
    return render(request, "index.html", {"obj": gv.obj})

def bvid(request):
    gv.set_obj('bvid', request.POST.get("bvid"))
    pagelist = sd._get_pagelist(gv.get_obj('bvid'))

    gv.set_obj('pagelist', pagelist)
    # return render(request, "index.html", {"pagelist": pagelist})
    return render(request, "index.html", {"obj": gv.obj})

def page(request):
    gv.set_obj('page',int(request.POST.get("page")) - 1)
    cid_list = sd._get_player_list(gv.get_obj('bvid'))
    cid = cid_list[gv.get_obj('page')]
    gv.set_obj('cid', cid)
    subtitle_list = sd._get_subtitle_list(gv.get_obj('bvid'), cid)
    sub_list = ""
    if subtitle_list:
        n = 1
        for x in subtitle_list:
            sub_list = sub_list + str(n) + '.' + x['lan_doc'] + "  "
            n = n+1
    gv.set_obj('sub_list', sub_list)
    # return render(request, "index.html", {"sub_list": sub_list})
    return render(request, "index.html", {"obj": gv.obj})

def sub(request):
    sub = int(request.POST.get("sub")) - 1
    sub_url = 'https:' + sd._get_subtitle_list(gv.get_obj('bvid'), gv.get_obj('cid'))[sub]['subtitle_url']
    text = sd._get_subtitle(sub_url)
    gv.set_obj('sub', sub)
    gv.set_obj('text', text)
    # return render(request, "index.html", {"text": text})
    return render(request, "index.html", {"obj": gv.obj})