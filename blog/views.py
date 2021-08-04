from django.views.generic import ListView, DetailView

from .models import Post
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post-detail.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = "post-new.html"
    fields = '__all__'

class BlogUpdateView(UpdateView):
    model = Post
    template_name = "post-edit.html"
    fields = ['title', 'body']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = "post-delete.html"
    success_url = reverse_lazy('home')