from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PubForm


# Create your views here.

def listar_pub(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/listar_pub.html', {'posts': posts})

def detalle_pub(request, pk):
    p = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detalle_pub.html', {'p': p})

def nueva_pub(request):
    if request.method == "POST":
        f = PubForm(request.POST)
        if f.is_valid():
            p = f.save(commit=False)
            p.author = request.user
            #p.published_date = timezone.now()
            p.save()
            return redirect('detalle_pub', pk=p.pk)
    else:
        f = PubForm()
    return render(request, 'blog/editar_pub.html', {'f': f})

def editar_pub(request, pk):
    p = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        f = PubForm(request.POST, instance=p)
        if f.is_valid():
            p = f.save(commit=False)
            p.author = request.user
            #p.published_date = timezone.now()
            p.save()
            return redirect('detalle_pub', pk=p.pk)
    else:
        f = PubForm(instance=p)
    return render(request, 'blog/editar_pub.html', {'f': f})

def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('detalle_pub', pk=pk)

def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('listar_pub')