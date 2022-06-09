from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .models import Post, Comment, Author, Category
from .filters import PostFilter
from .forms import PostForm
from django.urls import reverse_lazy
from django.shortcuts import render, HttpResponseRedirect


class PostList(ListView):
    model = Post
    ordering = '-creation_date'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10  # вот так мы можем указать количество записей на странице

class ArticleList(PostList):
    template_name = 'article.html'


class PostDetail(DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'new'

    def create_post(request):
        if request.method == 'POST':
            form = PostForm(request.POST)
            form.save()
            return HttpResponseRedirect('//')
        form = PostForm()
        return render(request, 'news_edit.html', {'form': form})


class PostSearch(ListView):
    template_name = 'search.html'
    context_object_name = 'post'
    queryset = Post.objects.all()

    def get_context_data(self, **kwargs):  # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет, полиморфизм, мы скучали!!!)
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())  # вписываем наш фильтр в контекст
        context['categories'] = Category.objects.all()
        context['form'] = PostForm

        return context

class PostView(DetailView):
  model = Post
  template_name = 'post.html'
  context_object_name = 'post'


class PostUpdateView(UpdateView):
    template_name = 'news_edit.html'
    form_class = PostForm

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте, который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)

# дженерик для удаления товара
class PostDeleteView(DeleteView):
    template_name = 'post_delete.html'
    # queryset = Post.objects.get(pk=id)
    success_url = '/news/'
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)

class NewsCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'

    def form_valid(self, form):
        current_url = self.request.path
        post = form.save(commit=False)
        post.category_news = self.model.NEWS
        return super().form_valid(form)


class ArticleCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'

    def form_valid(self, form):
        current_url = self.request.path
        post = form.save(commit=False)
        post.category_news = self.model.ARTICLE
        return super().form_valid(form)


class PostCreate(CreateView):
    # Указываем нашу разработанную форму
    form_class = PostForm
    # модель товаров
    model = Post
    # и новый шаблон, в котором используется форма.
    template_name = 'post_create.html'
