from django.shortcuts import render, HttpResponse
import app.subtitle_down as sd
import app.global_var as gv

# Create your views here.
def index(request):
    gv.update_cookie(request.POST.get("cookie"))
    return render(request, "index.html")

def bvid(request):
    gv.update_bvid(request.POST.get("bvid"))
    pagelist = sd._get_pagelist(gv.return_bvid())
    return render(request, "index.html", {"pagelist": pagelist})

def page(request):
    gv.update_page(int(request.POST.get("page")) - 1)
    cid_list = sd._get_player_list(gv.return_bvid())
    cid = cid_list[gv.return_page()]
    gv.update_cid(cid)
    subtitle_list = sd._get_subtitle_list(gv.return_bvid(), cid)
    sub_list = ""
    if subtitle_list:
        n = 1
        for x in subtitle_list:
            sub_list = sub_list + str(n) + '.' + x['lan_doc'] + "  "
            n = n+1
    return render(request, "index.html", {"sub_list": sub_list})

def sub(request):
    sub = int(request.POST.get("sub")) - 1
    sub_url = 'https:' + sd._get_subtitle_list(gv.return_bvid(), gv.return_cid())[sub]['subtitle_url']
    text = sd._get_subtitle(sub_url)
    return render(request, "index.html", {"text": text})