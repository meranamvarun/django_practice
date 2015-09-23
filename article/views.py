from django.shortcuts import render_to_response
from article.models import Article
from django.http import  HttpResponseRedirect
from forms import ArticleForm
from django.core.context_processors import csrf


def articles(request):
    return render_to_response('articles.html',
                             {'articles':Article.objects.all() })

def article(request, article_id=1):
    return render_to_response('article.html',
                             { 'article': Article.objects.get(id=article_id) })

def like_article(request,article_id):
    if article_id:
        a = Article.objects.get(id=article_id)
        a.likes+=1
        a.save()

    return HttpResponseRedirect('/articles/get/%s' % article_id)


def create(request):
    if request.POST:
        form = ArticleForm(request.POST,request.FILES) 
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('articles/all')
    
    else:
        form = ArticleForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('create_article.html',args)



