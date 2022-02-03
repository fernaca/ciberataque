from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Banco
from .forms import PostForm, EditForm
from django.urls import reverse_lazy
  
###################### POST
# Home / ListView
class HomeView(ListView):
    queryset = Post.objects.order_by('-created_on') #Negativo para el Sort
# Otra form de ordenar: ordering = ['-created_on']
    model = Post
    template_name = 'home.html' 

# DetailView
class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_detail.html' 
    
# CreateView. Pasamos el formulario
class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html' 
#    fields = '__all__'    #  o se le especifica los que se quiere: fields = ('title','body')
    # Como le pasamos el form_class, va a usar todos
 
# Editar
class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html' 
    
# Borrar
class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')  #Para el borrado es necesario
    
###################### BANCOS
# CreateView. Pasamos el formulario
class AddPostBanco(CreateView):
    model = Banco
    queryset = Banco.objects.order_by('name') 
    fields = '__all__'  #No usamos el form, ya que es 1 solo campo
    template_name = 'add_banco.html' 
    
def BancoView(request, bco):
    #Hacemos el query
    bancos_posteados = Post.objects.filter(banco = bco)
    return render(request, 'bancos.html', { 'bco': bco, 'bancos_posteados': bancos_posteados})

def ListBancos(request):
#    model = Banco
    #Hacemos el query
    bancos = Banco.objects.all().order_by('name')
    return render(request, 'bancos.html', {'bancos': bancos})

