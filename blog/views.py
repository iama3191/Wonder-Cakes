from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import AddPostForm


def blog(request):
    """
    View blog overview page.
    """
    posts = Post.objects.all()
    return render(request, 'blog/blog.html', {'posts': posts})


def post_detail(request, slug):
    """
    View post detail
    """

    query = Post.objects
    post = get_object_or_404(query, slug=slug)

    return render(
        request,
        'blog/post_detail.html',
        {'post': post,}
        )


@login_required
def add_post(request):
    """
    View add post form by admin only.
    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that')
        return redirect(reverse('blog'))

    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            messages.success(request, 'Successfully added post')

            return redirect('blog')
        else:
            messages.error(request,
                           'Something went wrong, please check the forms')
    else:
        form = AddPostForm()

    template = 'blog/add_post.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_post(request, slug):
    """
    View edit post form by admin only.
    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that')
        return redirect(reverse('blog'))

    query = Post.objects
    post = get_object_or_404(query, slug=slug)

    form = AddPostForm(instance=post)
    messages.info(request, f'You are editing {post.title}')

    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully edited post')
            return redirect(reverse('post_detail', kwargs={'slug': slug}))
        else:
            messages.error(request,
                           'Something went wrong, please check the form')

    context = {
        'post': post,
        'form': form
    }
    return render(request, 'blog/edit_post.html', context)


@login_required
def delete_post(request, slug):
    """
    View to delete post by admin only.
    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('blog'))

    query = Post.objects
    post = get_object_or_404(query, slug=slug)

    if request.method == "POST":
        post.delete()
        messages.success(request, 'Successfully deleted post')
        return redirect(reverse('blog'))

    context = {
        'post': post,
        'slug': slug
    }

    return render(request, 'blog/delete_post.html', context)

    messages.info(request, f'You are editing comment by {comment.author}')

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)

        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully edited comment')
            return redirect(reverse('post_detail', kwargs={'slug': slug}))
        else:
            messages.error(request,
                           'Failed to edit comment, please address errors')

    return render(
        request,
        'blog/post_detail.html',
        {'post': post, 'form': form}
        )
