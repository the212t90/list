from django.views import generic
from django.urls import reverse_lazy
from .models import Book
from .forms import BookForm
from .models import Reference
from .forms import ReferenceForm
from django.shortcuts import render
from django.http import HttpResponse

# 参考文献の一覧表示機能
class BookListView(generic.ListView):
    model = Book
    paginate_by = 5

# 参考文献の詳細表示機能
class BookDetailView(generic.DetailView):
    model = Book

# ToDoの作成機能
class BookCreateView(generic.CreateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('book:list')

# ToDoの編集機能
class BookUpdateView(generic.UpdateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('book:list')

# ToDoの削除機能
class BookDeleteView(generic.DeleteView):
    model = Book
    success_url = reverse_lazy('book:list')


def book_list(request):
    """書籍の一覧"""
    books = Book.objects.all().order_by('id')
    return render(request,
                  'book/book_list.html',     # 使用するテンプレート
                  {'books': books})         # テンプレートに渡すデータ


# 参考文献の一覧表示機能
class ReferenceListView(generic.ListView):
    model = Reference
    paginate_by = 5

# 参考文献の詳細表示機能
class ReferenceDetailView(generic.DetailView):
    model = Reference

# ToDoの作成機能
class ReferenceCreateView(generic.CreateView):
    model = Reference
    form_class = ReferenceForm
    success_url = reverse_lazy('book:rlist')

# ToDoの編集機能
class ReferenceUpdateView(generic.UpdateView):
    model = Reference
    form_class = ReferenceForm
    success_url = reverse_lazy('book:rlist')

# ToDoの削除機能
class ReferenceDeleteView(generic.DeleteView):
    model = Reference
    success_url = reverse_lazy('book:rlist')


def reference(request):
    """書籍の一覧"""
    references = Reference.objects.all().order_by('id')
    return render(request,
                  'book/reference.html',     # 使用するテンプレート
                  {'references': references})         # テンプレートに渡すデータ