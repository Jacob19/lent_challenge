from django.shortcuts import render
from .models import Tasks
from .forms import TasksList


# Create your views here.
def index(request):
    tasks = Tasks.objects.all()
    return render(request, 'index.html', {'tasks': tasks})
