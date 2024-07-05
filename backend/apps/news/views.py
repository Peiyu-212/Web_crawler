from django.shortcuts import render


def home_news(request):
    template_path = 'base.html'
    return render(request, template_path, locals())
