from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import Book
from app.forms import BookForm
from django.http import HttpResponse, JsonResponse
from django.views.generic  import ListView, CreateView, UpdateView, DeleteView, DetailView

def home(request):
    books = Book.objects.all()
    return render(request, "home.html", {"books": books})

def create_book(request):
    form = BookForm()
    if request.method == "POST":
        book = BookForm(request.POST)
        book.save()
        return redirect("home")
    return render(request, "create_book.html", {"form": form})
        


class BookList(ListView):
    model = Book
    template_name = "home.html"
    context_object_name = "books"


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