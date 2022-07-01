from audioop import reverse
from pickle import FALSE
from re import template
from urllib import request
from django.shortcuts import redirect, render
from django.views.generic.base import View
from django.views.generic import ListView, DetailView

from .models import Actor, Category, Movie, Genre
from .forms import ReviewForm
# Create your views here.

class GenreYear:
    
    def get_genres(self):
        return Genre.objects.all()

    def get_years(self):
        return Movie.objects.filter(draft=False).values("year")


class MoviesView(ListView, GenreYear):
    # model = Movie
    # queryset = Movie.objects.filter(draft=False)
    # template_name = "movies/movies.html"
    model = Movie
    quaryset = Movie.objects.filter(draft=False)


class MovieDetailView(DetailView, GenreYear):
    model = Movie
    slug_field = "url"

class AddReview(View):
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.movie = movie
            form.save()

        return redirect("/")

class ActorView(DetailView, GenreYear):
    model = Actor
    template_name ='movies/actor.html'
    slug_field = "name"