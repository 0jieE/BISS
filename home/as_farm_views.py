
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.http import JsonResponse
from .models import Farm, Crop, FarmCrop, FarmPicture
from .forms import FarmForm,CropForm, FarmCropForm, FarmPictureForm


#farm
##################################################################################################
@login_required
def farm(request):
    farms = Farm.objects.all()
    context = {
        'parent': '',
        'segment': 'farms',
        'farms': farms,
    }
    return render(request, 'user/farm/farm.html', context)

@login_required
def add_farm(request):
    if request.method == 'POST':
        form = FarmForm(request.POST)
    else:
        form = FarmForm()
    return save_farm(request, form, 'user/farm/add_farm.html')

@login_required
def edit_farm(request, pk):
    farm = get_object_or_404(Farm, pk=pk)
    if request.method == 'POST':
        form = FarmForm(request.POST, instance=farm)
    else:
        form = FarmForm(instance=farm)
    return save_farm(request, form, 'user/farm/edit_farm.html')

@login_required
def delete_farm(request, pk):
    farm = get_object_or_404(Farm, pk=pk)
    data = dict()
    if request.method == 'POST':
        farm.delete()
        data['form_is_valid'] = True
        farms = Farm.objects.all()
        data['farm_list'] = render_to_string('user/farm/list_farm.html', {'farms': farms})
    else:
        context = {'farm': farm}
        data['html_form'] = render_to_string('user/farm/delete_farm.html', context, request=request)
    return JsonResponse(data)

def save_farm(request, form, template_name):
    data = dict()
    if form.is_valid():
        form.save()
        data['form_is_valid'] = True
        farms = Farm.objects.all()
        data['farm_list'] = render_to_string('user/farm/list_farm.html', {'farms': farms})
    else:
        data['form_is_valid'] = False

    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

#crop
##################################################################################################

@login_required
def crop(request):
    crops = Crop.objects.all()
    context = {
        'parent': 'farm_management',
        'segment': 'crops',
        'crops': crops,
    }
    return render(request, 'user/farm/crop/crop.html', context)

@login_required
def add_crop(request):
    if request.method == 'POST':
        form = CropForm(request.POST)
    else:
        form = CropForm()
    return save_crop(request, form, 'user/farm/crop/add_crop.html')

@login_required
def edit_crop(request, pk):
    crop = get_object_or_404(Crop, pk=pk)
    if request.method == 'POST':
        form = CropForm(request.POST, instance=crop)
    else:
        form = CropForm(instance=crop)
    return save_crop(request, form, 'user/farm/crop/edit_crop.html')

@login_required
def delete_crop(request, pk):
    crop = get_object_or_404(Crop, pk=pk)
    data = dict()
    if request.method == 'POST':
        crop.delete()
        data['form_is_valid'] = True
        crops = Crop.objects.all()
        data['crop_list'] = render_to_string('user/farm/crop/list_crop.html', {'crops': crops})
    else:
        context = {'crop': crop}
        data['html_form'] = render_to_string('user/farm/crop/delete_crop.html', context, request=request)
    return JsonResponse(data)

def save_crop(request, form, template_name):
    data = dict()
    if form.is_valid():
        form.save()
        data['form_is_valid'] = True
        crops = Crop.objects.all()
        data['crop_list'] = render_to_string('user/farm/crop/list_crop.html', {'crops': crops})
    else:
        data['form_is_valid'] = False

    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

#farm_crop
##################################################################################################

@login_required
def farm_crop(request):
    farm_crops = FarmCrop.objects.all()
    context = {
        'parent': '',
        'segment': 'farm_crops',
        'farm_crops': farm_crops,
    }
    return render(request, 'user/farm/farm_crop/farm_crop.html', context)

@login_required
def add_farm_crop(request):
    if request.method == 'POST':
        form = FarmCropForm(request.POST)
    else:
        form = FarmCropForm()
    return save_farm_crop(request, form, 'user/farm/farm_crop/add_farm_crop.html')

@login_required
def edit_farm_crop(request, pk):
    farm_crop = get_object_or_404(FarmCrop, pk=pk)
    if request.method == 'POST':
        form = FarmCropForm(request.POST, instance=farm_crop)
    else:
        form = FarmCropForm(instance=farm_crop)
    return save_farm_crop(request, form, 'user/farm/farm_crop/edit_farm_crop.html')

@login_required
def delete_farm_crop(request, pk):
    farm_crop = get_object_or_404(FarmCrop, pk=pk)
    data = dict()
    if request.method == 'POST':
        farm_crop.delete()
        data['form_is_valid'] = True
        farm_crops = FarmCrop.objects.all()
        data['farm_crop_list'] = render_to_string('user/farm/farm_crop/list_farm_crop.html', {'farm_crops': farm_crops})
    else:
        context = {'farm_crop': farm_crop}
        data['html_form'] = render_to_string('user/farm/farm_crop/delete_farm_crop.html', context, request=request)
    return JsonResponse(data)

def save_farm_crop(request, form, template_name):
    data = dict()
    if form.is_valid():
        form.save()
        data['form_is_valid'] = True
        farm_crops = FarmCrop.objects.all()
        data['farm_crop_list'] = render_to_string('user/farm/farm_crop/list_farm_crop.html', {'farm_crops': farm_crops})
    else:
        data['form_is_valid'] = False

    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


#farm_picture
##################################################################################################

@login_required
def farm_picture(request):
    farm_pictures = FarmPicture.objects.all()
    context = {
        'parent': '',
        'segment': 'farm_pictures',
        'farm_pictures': farm_pictures,
    }
    return render(request, 'user/farm/farm_picture/farm_picture.html', context)

@login_required
def add_farm_picture(request):
    if request.method == 'POST':
        form = FarmPictureForm(request.POST, request.FILES)
    else:
        form = FarmPictureForm()
    return save_farm_picture(request, form, 'user/farm/farm_picture/add_farm_picture.html')

@login_required
def edit_farm_picture(request, pk):
    farm_picture = get_object_or_404(FarmPicture, pk=pk)
    if request.method == 'POST':
        form = FarmPictureForm(request.POST, request.FILES, instance=farm_picture)
    else:
        form = FarmPictureForm(instance=farm_picture)
    return save_farm_picture(request, form, 'user/farm/farm_picture/edit_farm_picture.html')

@login_required
def delete_farm_picture(request, pk):
    farm_picture = get_object_or_404(FarmPicture, pk=pk)
    data = dict()
    if request.method == 'POST':
        farm_picture.delete()
        data['form_is_valid'] = True
        farm_pictures = FarmPicture.objects.all()
        data['farm_picture_list'] = render_to_string('user/farm/farm_picture/list_farm_picture.html', {'farm_pictures': farm_pictures})
    else:
        context = {'farm_picture': farm_picture}
        data['html_form'] = render_to_string('user/farm/farm_picture/delete_farm_picture.html', context, request=request)
    return JsonResponse(data)

def save_farm_picture(request, form, template_name):
    data = dict()
    if form.is_valid():
        form.save()
        data['form_is_valid'] = True
        farm_pictures = FarmPicture.objects.all()
        data['farm_picture_list'] = render_to_string('user/farm/farm_picture/list_farm_picture.html', {'farm_pictures': farm_pictures})
    else:
        data['form_is_valid'] = False

    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


