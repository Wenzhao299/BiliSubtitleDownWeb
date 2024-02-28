from django.shortcuts import render, HttpResponse
import app.subtitle_down as sd
import app.global_var

# Create your views here.
def index(request):
    app.global_var.update_var(request.POST.get("cookie"))
    return render(request, "index.html")

def bvid(request):
    bvid = request.POST.get("bvid")
    sd.bvid = bvid
    pagelist = sd._get_pagelist(sd.bvid)
    return render(request, "index.html", {"pagelist": pagelist})

def page(request):
    page = int(request.POST.get("page")) - 1
    cid_list = sd._get_player_list(sd.bvid)
    # print(cid_list[page])
    subtitle_list = sd._get_subtitle_list(sd.bvid, cid_list[page])
    # print(subtitle_list)
    sub_list = ""
    if subtitle_list:
        n = 1
        for x in subtitle_list:
            sub_list = sub_list + str(n) + '.' + x['lan_doc'] + "  "
            n = n+1
    return render(request, "index.html", {"sub_list": sub_list})

def sub(request):
    sub = int(request.POST.get("sub")) - 1
    # 'https:' + sub_list[sub]['subtitle_url']