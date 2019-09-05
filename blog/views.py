from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post


# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/listar_pub.html', {'posts': posts})

def detalle_pub(request,pk):
	p = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/detalle_pub.html', {'p':p})