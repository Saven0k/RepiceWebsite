from django.shortcuts import render, redirect
import logging
from .models import Recipe
from .forms import RecipeAddForm 
from django.contrib.auth.models import User 
from django.contrib.auth.views import LoginView



# Create your views here.

logger = logging.getLogger(__name__)


def index(request):
    logger.info('index get request ')
    return render(request, 'main/index.html')


    
                  
def recipe(request):
    logger.info('index get request ')
    return render(request, 'main/recipe.html')
    
    
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeAddForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            steps = form.cleaned_data['steps']
            time_to_cook = form.cleaned_data['time_to_cook']
            img = form.cleaned_data['img']
            author = form.cleaned_data['author']
            logger.info(f'Получили {title=}\n {content=}\n {steps=} \n {time_to_cook=} \n {author}')
            recipe = Recipe(title=title, content=content, steps=steps, time_to_cook=time_to_cook, img=img, author=author)
            recipe.save()		    
            return redirect('index')
            
    else: 
        form =  RecipeAddForm()
    logger.info('index get request ')
    return render(request, 'main/add_recipe.html', {'form': form})
                  
                  
# def login(request):
#     return render(request, 'main/login.html')

class CustomLoginView(LoginView):
    template_name = 'main/login.html'


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username, password=password)
        return redirect('add_recipe')
    return render(request, 'main/register.html')