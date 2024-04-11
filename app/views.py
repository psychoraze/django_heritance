from django.shortcuts import render
from .models import Pet, Post
from .forms import PetForm, PostForm
from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy

def index(request):
    pets = Pet.objects.all()
    return render(request, 'index.html', {'pets': pets})

class PetCreate(CreateView):
    model = Pet
    form_class = PetForm
    success_url = reverse_lazy('index')
    template_name = 'create.html'

class PostCreate(CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('index')
    template_name = 'create.html'

class PostView(DetailView):
    model = Post
    template_name = 'view.html'

    def get_posts(self, **kwargs):
        posts = super().get_context_data(**kwargs)
        posts['form'] = PostForm
        posts['posts'] = Post.objects.all(id=kwargs['pk'])
        return posts