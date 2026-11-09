from django.shortcuts import render, redirect
from django.http import HttpRequest, Http404
from .data.sites import sites


def home_view(request: HttpRequest):
    return render(request, "main/home.html", {"sites": sites})


def sites_view(request: HttpRequest):
    return render(request, "main/sites.html", {"sites": sites})


def site_detail_view(request: HttpRequest, slug):
    for site in sites:
        if site["slug"] == slug:
            return render(request, "main/site_detail.html", {"site": site})
    raise Http404("الموقع غير موجود")


def toggle_theme(request: HttpRequest):
    current = request.COOKIES.get("theme", "light")
    new_theme = "light" if current == "dark" else "dark"

    next_url = request.META.get("HTTP_REFERER") or "/"
    response = redirect(next_url)
    response.set_cookie("theme", new_theme, max_age=60 * 60 * 24 * 30)
    return response