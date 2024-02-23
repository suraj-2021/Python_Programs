# views.py
from django.shortcuts import render
from .forms import ArticleForm

def create_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or do something else
    else:
        form = ArticleForm()

    return render(request, "article_form.html", {"form": form})
