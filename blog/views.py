from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect
from django.contrib.auth.models import User

def	post_list(request):
	posts = Post.objects.filter(yayinlama_tarihi__lte=timezone.now()).order_by('yayinlama_tarihi')
	return	render(request,	'blog/post_list.html',	{'posts': posts})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.yazar = request.user
			post.yayinlama_tarihi = timezone.now()
			# post.yazar_id=11
			post.save()
			return redirect('blog.views.post_detail', pk=post.pk)
	else:
		form = PostForm()
		return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.yazar = request.user
			post.yayinlama_tarihi = timezone.now()
			# post.yazar_id=11
			post.save()
			return redirect('blog.views.post_detail', pk=post.pk)
		else:
			form = PostForm(instance=post)
			return render(request, 'blog/post_edit.html', {'form': form})
