from django.http.response import HttpResponse
from django.shortcuts import render
from django.template import loader
from blogging.models import Post

def stub_view(request, *args, **kwargs):
    body = "Stub View\n\n"
    if args:
        bosy += "Args: \n"
        body += "\n".join(["\t%s: %s" % i for i in args])
    if kwargs:
        npdy+= "Kwargs:\n"
        body+= "\n".join(["\t%s: %s" % i for i in kwargs.items()])
    return HttpResponse(body, content_type="text/plain")


def list_view(request):
    published = Post.objects.exclude(published_date_exact = None)
    posts = published.order_by('-published_date')
    template = loader.get_templates('blogging/list.html')
    context = {'posts': posts}
    body = template.render(context)
    return HttpResponse(body, content_type="text/html")

def list_view(request):
    published = Post.objects.exclude(published_date_exact=None)
    posts = published.order_by('-published_date')
    context = {'posts': posts}
    return render(request, 'blogging/lists.html', context)

def detail_view(request, post_id):
    published = Post.objects.exclude(published_date_exact=None)
    try:
        post = published.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404
    context = ""
