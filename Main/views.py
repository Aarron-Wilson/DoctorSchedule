from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.http import JsonResponse


def home(request):
    return render(request,'home.html')

def roster_page(request):
    doctors = Doctor.objects.all().order_by('name')
    return render(request,'roster.html',{'doctors':doctors})

def block_page(request):
    all_blocks = Section.objects.all()
    return render(request,'block.html',{'blocks':all_blocks})

def schedule_page(request):
    return render(request,'schedule.html')

def create_edit_block(request,pk=None):
    if request.method == 'POST':
        if pk:
            form = BlockForm(request.POST,instance=Section.objects.get(pk=pk))
        else:
            form = BlockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/block')
        else:
            return render(request, 'myapp/includes/create_item_full_modal.html', {'form': form}, status=400)
    else:
        if pk:
            form = BlockForm(instance=Section.objects.get(pk=pk))
        else:
            form = BlockForm()
        
        return render(request,'create_edit_block.html',{'form':form,'pk':pk})

def delete_block(request,pk):
    Section.objects.get(pk=pk).delete()
    return JsonResponse({"message": "Success"})