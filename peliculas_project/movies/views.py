from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404
from .models import Movie

def movie_list(request):
    movies = Movie.objects.all().order_by('title') 
    return render(request, 'movies/movie_list.html', {'movies': movies})

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id) 
    return render(request, 'movies/movie_detail.html', {'movie': movie})