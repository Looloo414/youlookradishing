from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Workout, Food
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

# --------------SIGN UP/LOGIN-------------------------
def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('about')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

# ----------------WORKOUTS------------------------------

@login_required
def workouts_index(request):
    workouts = Workout.objects.filter(user=request.user)
    return render(request, 'workouts/index.html', {'workouts': workouts})

@login_required
def workouts_detail(request, workout_id):
    workout = Workout.objects.get(id=workout_id)
    return render(request, 'workouts/detail.html', {'workout': workout})

class WorkoutCreate(LoginRequiredMixin, CreateView):
    model = Workout
    fields = ['activity','howLong', 'description']
    success_url = '/workout/'

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)

class WorkoutDelete(LoginRequiredMixin, DeleteView):
    model = Workout
    success_url = '/workout/'

class WorkoutUpdate(LoginRequiredMixin, UpdateView):
    model = Workout
    fields = ['activity', 'howLong', 'description']

# --------------------FOOD----------------------------
@login_required
def food_index(request):
    foods = Food.objects.filter(user=request.user)
    return render(request, 'food/index.html', {'foods': foods})

@login_required
def food_detail(request, food_id):
    food = Food.objects.get(id=food_id)
    return render(request, 'food/detail.html', {'food': food})

class FoodCreate(LoginRequiredMixin, CreateView):
    model = Food
    fields = ['item', 'calories', 'meal']
    success_url = '/food/'

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)

class FoodDelete(LoginRequiredMixin, DeleteView):
    model = Food
    success_url = '/food/'

class FoodUpdate(LoginRequiredMixin,UpdateView):
    model = Food
    fields = ['item', 'calories', 'meal']



