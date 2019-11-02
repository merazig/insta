from django.shortcuts import render
from .models import Insta
# Create your views here.
def index(request):
    instas = Insta.objects.all()
    ctx = {'active_tab': 'tab1', 'instas':instas}
    return render(request, 'photos/index.html', ctx) 