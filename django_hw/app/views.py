from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import Book
from app.forms import BookForm, SearchForm
from django.http import HttpResponse, JsonResponse
from django.views.generic  import ListView, CreateView, UpdateView, DeleteView, DetailView


# def home(request):
#     books = Book.objects.all()
#     return render(request, "home.html", {"books": books})

# def create_book(request):
#     form = BookForm()
#     if request.method == "POST":
#         book = BookForm(request.POST)
#         book.save()
#         return redirect("home")
#     return render(request, "create_book.html", {"form": form})
        


class BookList(ListView):
    model = Book
    template_name = "home.html"
    context_object_name = "books"
    paginate_by = 3
    
    def get_queryset(self):
        queryset = super().get_queryset()
        search_form = SearchForm(self.request.GET)  # Инициализируем форму поиска с данными из запроса
        if search_form.is_valid():
            cleaned_data = search_form.cleaned_data
            title = cleaned_data.get("title")
            if title:
                queryset = queryset.filter(title__icontains=title)
        return queryset


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = SearchForm(self.request.GET) 
        return context



class BookDetail(DetailView):
    model = Book
    template_name = "detail_book.html"
    context_object_name = "book"


class BookCreate(CreateView):
    model = Book
    template_name = "create_book.html"
    form_class = BookForm
    success_url = reverse_lazy("home")

class BookUpdate(UpdateView):
    model = Book
    template_name = "update_book.html"
    form_class = BookForm

    def get_success_url(self):
        return reverse_lazy("detail_book", kwargs={"pk": self.object.pk})

class BookDelete(DeleteView):
    model = Book
    template_name = "delete_book.html"
    success_url = reverse_lazy("home")