from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import JsonResponse
import json

def home(request):
    return render(request, 'home.html')


def roster_page(request):
    doctors = Doctor.objects.all().order_by('name')
    return render(request, 'roster.html', {'doctors': doctors})


def block_page(request):
    all_blocks = Section.objects.all()
    return render(request, 'block.html', {'blocks': all_blocks})


def schedule_page(request):
    return render(request, 'schedule.html')

def manage_job_slots(request,pk):
    block = Section.objects.get(pk=pk)
    job_slots = JobSlot.objects.filter(section=block)
    return render(request, 'manage_job_slots.html', {'block': block,'job_slots':job_slots})

def create_edit_block(request, pk=None):
    if request.method == 'POST':
        if pk:
            form = BlockForm(request.POST, instance=Section.objects.get(pk=pk))
        else:
            form = BlockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/block')
        else:
            return render(request,
                          'myapp/includes/create_item_full_modal.html',
                          {'form': form},
                          status=400)
    else:
        if pk:
            form = BlockForm(instance=Section.objects.get(pk=pk))
        else:
            form = BlockForm()

        return render(request, 'create_edit_block.html', {
            'form': form,
            'pk': pk
        })

def delete_block(request, pk):
    Section.objects.get(pk=pk).delete()
    return JsonResponse({"message": "Success"})

def add_job_slot(request,pk):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode("utf-8"))
        except json.JSONDecodeError:
            return JsonResponse({"success": "false"}, status=400)

        try:
            section = Section.objects.get(pk=pk)
        except Section.DoesNotExist:
            return JsonResponse({"success": "false"}, status=400)
            
        job_slot = JobSlot()
        job_slot.section = section
        job_slot.amount = data['amount']
        job_slot.min_year = data['min_year']
        job_slot.max_year = data['max_year']
        job_slot.only_IM = data['only_IM']
        job_slot.save()

        return JsonResponse({"success": "true",'pk':job_slot.pk})
    else:
        return JsonResponse({"success": "false"}, status=400)

def delete_job_slot(request,pk):
    JobSlot.objects.get(pk=pk).delete()
    return JsonResponse({"success": "true"})
