from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Announcement
from .forms import AnnounForm

@login_required
def index(request):
     return render(request, 'components/index.html')

@login_required
def announcement(request):
    announcements = Announcement.objects.all()
    return render(request, 'components/announcement.html', {'announcements': announcements})

@login_required
def new_announ(request):
    if request.method == 'POST':
        form = AnnounForm(request.POST)
        if form.is_valid():
            new_announ = form.save(commit=False)
            new_announ.owner = request.user
            new_announ.save()
            return redirect('components:announcement')
    else:
        form = AnnounForm()
    
    context = {'form': form}
    return render(request, 'components/new_announ.html', context)

@login_required
def edit_announ(request, announcement_id):
     announcement = Announcement.objects.get(id=announcement_id)
     if request.user.is_superuser == False:
        if announcement.owner != request.user:
           raise Http404
     if request.method != 'POST':
          form = AnnounForm(instance=announcement)
     else: 
          form = AnnounForm(instance=announcement, data=request.POST)
          if form.is_valid():
             form.save()
             return redirect('components:announcement')
        
     context = {'announcement' : announcement, 'form': form}
     return render(request, 'components/edit_announ.html', context)

@login_required
def delete_announ(request, announcement_id):
    announcement = Announcement.objects.get(id=announcement_id)
    if request.user.is_superuser == False:
        if announcement.owner != request.user:
           raise Http404
    if request.method == 'POST':
        announcement.delete()
        return redirect('components:announcement')
    
    context = {'announcement' : announcement}
    return render(request, 'components/delete_announ.html', context)