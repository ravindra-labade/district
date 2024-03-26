from django.shortcuts import render, redirect
from .forms import DistrictForm
from .models import District
from django.contrib.auth.decorators import login_required


def add_district(request):
    template_name = 'distapp/add.html'
    form = DistrictForm()
    if request.method == 'POST':
        form = DistrictForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form': form}
    return render(request, template_name, context)


def show_district(request):
    template_name = 'distapp/show.html'
    districts = District.objects.all()
    context = {'districts': districts}
    return render(request, template_name, context)


def update_district(request, pk):
    template_name = 'distapp/add.html'
    obj = District.objects.get(id=pk)
    form = DistrictForm(instance=obj)
    if request.method == 'POST':
        form = DistrictForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form': form}
    return render(request, template_name, context)



def delete_district(request, pk):
    obj = District.objects.get(id=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('show_url')
    return render(request, 'distapp/confirm.html')