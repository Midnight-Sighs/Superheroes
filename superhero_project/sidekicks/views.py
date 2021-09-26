from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from .models import Sidekick


# Create your views here.
def index(request):
    all_sidekicks = Sidekick.objects.all
    context = {
        'all_sidekicks': all_sidekicks
    }
    return render(request, 'sidekicks/index.html', context)

def detail(request, sidekick_id):
    single_sidekick = Sidekick.objects.get(pk=sidekick_id)
    context = {
        'single_sidekick': single_sidekick
    }
    return render(request, 'sidekicks/detail.html', context)

def create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        sidekick_to = request.POST.get('sidekick_to')
        primary_ability = request.POST.get('primary_ability')
        description = request.POST.get('description')
        new_sidekick = Sidekick(name=name, alter_ego=alter_ego, sidekick_to=sidekick_to, primary_ability=primary_ability, description=description)
        new_sidekick.save()
        return HttpResponseRedirect(reverse('sidekicks:index'))
    else:
        return render(request, 'sidekicks/create.html')

def edit(request, sidekick_id):
    single_sidekick = Sidekick.objects.get(pk=sidekick_id)
    context = {
        'single_sidekick': single_sidekick
    }
    if request.method == "POST":
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        sidekick_to = request.POST.get('sidekick_to')
        primary_ability = request.POST.get('primary_ability')
        description = request.POST.get('description')
        update_sidekick = Sidekick(id,name,alter_ego,sidekick_to,primary_ability, description)
        update_sidekick.save()
        return HttpResponseRedirect(reverse('sidekicks:index'))
    else:
        return render(request, 'sidekicks/edit.html', context)

def delete(request, sidekick_id):
    deleteMe = Sidekick.objects.get(pk=sidekick_id)
    deleteMe.delete()
    return HttpResponseRedirect(reverse('sidekicks:index'))
