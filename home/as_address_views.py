# views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string, get_template
from django.http import JsonResponse
from .models import Region,Province, District, CityMunicipality, Barangay, Purok, Address
from .forms import AddressForm, RegionForm, ProvinceForm, DistrictForm, CityMunicipalityForm, BarangayForm, PurokForm

#address
#########################################################################################################
def address(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        addresses = Address.objects.all()
        context = {
                'parent': '',
                'segment': 'addresses',
                'addresses':addresses,
        }
        return render(request, 'user/address/address.html',context)


def add_address(request):
        if(request.method == 'POST'):
                form = AddressForm(request.POST)
        else:    
                form = AddressForm()

        return save_address(request, form, 'user/address/add_address.html')

def edit_address(request,pk):
        address = get_object_or_404(Address, pk=pk)
        if(request.method == 'POST'):
                form = AddressForm(request.POST, instance=address)
        else:    
                form = AddressForm(instance=address)
        return save_address(request, form, 'user/address/edit_address.html')


def delete_address(request,pk):
        address = get_object_or_404(Address, pk=pk)
        data = dict()
        if request.method == 'POST':
            address.delete()
            data['form_is_valid'] = True
            addresses= Address.objects.all()
            data['address_list'] = render_to_string('user/address/list_address.html',{'addresses':addresses})
        else:    
            context = {'address':address}
            data['html_form'] = render_to_string('user/address/delete_address.html',context,request=request)
        return JsonResponse(data)

def save_address(request, form, template_name):
    data = dict()
    if form.is_valid():
        form.save()
        data['form_is_valid'] = True
        addresses= Address.objects.all()
        data['address_list'] = render_to_string('user/address/list_address.html',{'addresses':addresses})
    else:
        data['form_is_valid'] = False

    context = {'form':form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

#regions
#########################################################################################################

@login_required
def region(request):
    regions = Region.objects.all()
    context = {
        'parent': 'addresses',
        'segment': 'region',
        'regions': regions,
    }
    return render(request, 'user/address/region/region.html', context)

@login_required
def add_region(request):
    if request.method == 'POST':
        form = RegionForm(request.POST)
    else:
        form = RegionForm()
    return save_region(request, form, 'user/address/region/add_region.html')

@login_required
def edit_region(request, pk):
    region = get_object_or_404(Region, pk=pk)
    if request.method == 'POST':
        form = RegionForm(request.POST, instance=region)
    else:
        form = RegionForm(instance=region)
    return save_region(request, form, 'user/address/region/edit_region.html')

@login_required
def delete_region(request, pk):
    region = get_object_or_404(Region, pk=pk)
    data = dict()
    if request.method == 'POST':
        region.delete()
        data['form_is_valid'] = True
        regions = Region.objects.all()
        data['region_list'] = render_to_string('user/address/region/list_region.html', {'regions': regions})
    else:
        context = {'region': region}
        data['html_form'] = render_to_string('user/address/region/delete_region.html', context, request=request)
    return JsonResponse(data)

def save_region(request, form, template_name):
    data = dict()
    if form.is_valid():
        form.save()
        data['form_is_valid'] = True
        regions = Region.objects.all()
        data['region_list'] = render_to_string('user/address/region/list_region.html', {'regions': regions})
    else:
        data['form_is_valid'] = False

    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


#Province
#########################################################################################################

@login_required
def province(request):
    provinces = Province.objects.all()
    context = {
        'parent': 'addresses',
        'segment': 'province',
        'provinces': provinces,
    }
    return render(request, 'user/address/province/province.html', context)

@login_required
def add_province(request):
    if request.method == 'POST':
        form = ProvinceForm(request.POST)
    else:
        form = ProvinceForm()
    return save_province(request, form, 'user/address/province/add_province.html')

@login_required
def edit_province(request, pk):
    province = get_object_or_404(Province, pk=pk)
    if request.method == 'POST':
        form = ProvinceForm(request.POST, instance=province)
    else:
        form = ProvinceForm(instance=province)
    return save_province(request, form, 'user/address/province/edit_province.html')

@login_required
def delete_province(request, pk):
    province = get_object_or_404(Province, pk=pk)
    data = dict()
    if request.method == 'POST':
        province.delete()
        data['form_is_valid'] = True
        provinces = Province.objects.all()
        data['province_list'] = render_to_string('user/address/province/list_province.html', {'provinces': provinces})
    else:
        context = {'province': province}
        data['html_form'] = render_to_string('user/address/province/delete_province.html', context, request=request)
    return JsonResponse(data)

def save_province(request, form, template_name):
    data = dict()
    if form.is_valid():
        form.save()
        data['form_is_valid'] = True
        provinces = Province.objects.all()
        data['province_list'] = render_to_string('user/address/province/list_province.html', {'provinces': provinces})
    else:
        data['form_is_valid'] = False

    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

#District
#########################################################################################################

@login_required
def district(request):
    districts = District.objects.all()
    context = {
        'parent': 'addresses',
        'segment': 'district',
        'districts': districts,
    }
    return render(request, 'user/address/district/district.html', context)

@login_required
def add_district(request):
    if request.method == 'POST':
        form = DistrictForm(request.POST)
    else:
        form = DistrictForm()
    return save_district(request, form, 'user/address/district/add_district.html')

@login_required
def edit_district(request, pk):
    district = get_object_or_404(District, pk=pk)
    if request.method == 'POST':
        form = DistrictForm(request.POST, instance=district)
    else:
        form = DistrictForm(instance=district)
    return save_district(request, form, 'user/address/district/edit_district.html')

@login_required
def delete_district(request, pk):
    district = get_object_or_404(District, pk=pk)
    data = dict()
    if request.method == 'POST':
        district.delete()
        data['form_is_valid'] = True
        districts = District.objects.all()
        data['district_list'] = render_to_string('user/address/district/list_district.html', {'districts': districts})
    else:
        context = {'district': district}
        data['html_form'] = render_to_string('user/address/district/delete_district.html', context, request=request)
    return JsonResponse(data)

def save_district(request, form, template_name):
    data = dict()
    if form.is_valid():
        form.save()
        data['form_is_valid'] = True
        districts = District.objects.all()
        data['district_list'] = render_to_string('user/address/district/list_district.html', {'districts': districts})
    else:
        data['form_is_valid'] = False

    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

#CityMunicipality
#########################################################################################################

@login_required
def municipality(request):
    municipalities = CityMunicipality.objects.all()
    context = {
        'parent': 'addresses',
        'segment': 'municipality',
        'municipalities': municipalities,
    }
    return render(request, 'user/address/municipality/municipality.html', context)

@login_required
def add_municipality(request):
    if request.method == 'POST':
        form = CityMunicipalityForm(request.POST)
    else:
        form = CityMunicipalityForm()
    return save_municipality(request, form, 'user/address/municipality/add_municipality.html')

@login_required
def edit_municipality(request, pk):
    municipality = get_object_or_404(CityMunicipality, pk=pk)
    if request.method == 'POST':
        form = CityMunicipalityForm(request.POST, instance=municipality)
    else:
        form = CityMunicipalityForm(instance=municipality)
    return save_municipality(request, form, 'user/address/municipality/edit_municipality.html')

@login_required
def delete_municipality(request, pk):
    municipality = get_object_or_404(CityMunicipality, pk=pk)
    data = dict()
    if request.method == 'POST':
        municipality.delete()
        data['form_is_valid'] = True
        municipalities = CityMunicipality.objects.all()
        data['municipality_list'] = render_to_string('user/address/municipality/list_municipality.html', {'municipalities': municipalities})
    else:
        context = {'municipality': municipality}
        data['html_form'] = render_to_string('user/address/municipality/delete_municipality.html', context, request=request)
    return JsonResponse(data)

def save_municipality(request, form, template_name):
    data = dict()
    if form.is_valid():
        form.save()
        data['form_is_valid'] = True
        municipalities = CityMunicipality.objects.all()
        data['municipality_list'] = render_to_string('user/address/municipality/list_municipality.html', {'municipalities': municipalities})
    else:
        data['form_is_valid'] = False

    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

#barangay
#########################################################################################################

@login_required
def barangay(request):
    barangays = Barangay.objects.all()
    context = {
        'parent': 'addresses',
        'segment': 'barangays',
        'barangays': barangays,
    }
    return render(request, 'user/address/barangay/barangay.html', context)

@login_required
def add_barangay(request):
    if request.method == 'POST':
        form = BarangayForm(request.POST)
    else:
        form = BarangayForm()
    return save_barangay(request, form, 'user/address/barangay/add_barangay.html')

@login_required
def edit_barangay(request, pk):
    barangay = get_object_or_404(Barangay, pk=pk)
    if request.method == 'POST':
        form = BarangayForm(request.POST, instance=barangay)
    else:
        form = BarangayForm(instance=barangay)
    return save_barangay(request, form, 'user/address/barangay/edit_barangay.html')

@login_required
def delete_barangay(request, pk):
    barangay = get_object_or_404(Barangay, pk=pk)
    data = dict()
    if request.method == 'POST':
        barangay.delete()
        data['form_is_valid'] = True
        barangays = Barangay.objects.all()
        data['barangay_list'] = render_to_string('user/address/barangay/list_barangay.html', {'barangays': barangays})
    else:
        context = {'barangay': barangay}
        data['html_form'] = render_to_string('user/address/barangay/delete_barangay.html', context, request=request)
    return JsonResponse(data)

def save_barangay(request, form, template_name):
    data = dict()
    if form.is_valid():
        form.save()
        data['form_is_valid'] = True
        barangays = Barangay.objects.all()
        data['barangay_list'] = render_to_string('user/address/barangay/list_barangay.html', {'barangays': barangays})
    else:
        data['form_is_valid'] = False

    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

#Purok
#########################################################################################################


@login_required
def purok(request):
    puroks = Purok.objects.all()
    context = {
        'parent': 'addresses',
        'segment': 'puroks',
        'puroks': puroks,
    }
    return render(request, 'user/address/purok/purok.html', context)

@login_required
def add_purok(request):
    if request.method == 'POST':
        form = PurokForm(request.POST)
    else:
        form = PurokForm()
    return save_purok(request, form, 'user/address/purok/add_purok.html')

@login_required
def edit_purok(request, pk):
    purok = get_object_or_404(Purok, pk=pk)
    if request.method == 'POST':
        form = PurokForm(request.POST, instance=purok)
    else:
        form = PurokForm(instance=purok)
    return save_purok(request, form, 'user/address/purok/edit_purok.html')

@login_required
def delete_purok(request, pk):
    purok = get_object_or_404(Purok, pk=pk)
    data = dict()
    if request.method == 'POST':
        purok.delete()
        data['form_is_valid'] = True
        puroks = Purok.objects.all()
        data['purok_list'] = render_to_string('user/address/purok/list_purok.html', {'puroks': puroks})
    else:
        context = {'purok': purok}
        data['html_form'] = render_to_string('user/address/purok/delete_purok.html', context, request=request)
    return JsonResponse(data)

def save_purok(request, form, template_name):
    data = dict()
    if form.is_valid():
        form.save()
        data['form_is_valid'] = True
        puroks = Purok.objects.all()
        data['purok_list'] = render_to_string('user/address/purok/list_purok.html', {'puroks': puroks})
    else:
        data['form_is_valid'] = False

    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)



#address selector
#########################################################################################################

def load_provinces(request):
    region_id = request.GET.get('region_id')
    provinces = Province.objects.filter(region_id=region_id).order_by('province_name')
    return JsonResponse(list(provinces.values('id', 'province_name')), safe=False)

def load_districts(request):
    province_id = request.GET.get('province_id')
    districts = District.objects.filter(province_id=province_id).order_by('district_name')
    return JsonResponse(list(districts.values('id', 'district_name')), safe=False)

def load_cities(request):
    district_id = request.GET.get('district_id')
    cities = CityMunicipality.objects.filter(district_id=district_id).order_by('municipality_name')
    return JsonResponse(list(cities.values('id', 'municipality_name')), safe=False)

def load_barangays(request):
    municipality_id = request.GET.get('municipality_id')
    barangays = Barangay.objects.filter(municipality_id=municipality_id).order_by('barangay_name')
    return JsonResponse(list(barangays.values('id', 'barangay_name')), safe=False)

def load_puroks(request):
    barangay_id = request.GET.get('barangay_id')
    puroks = Purok.objects.filter(barangay_id=barangay_id).order_by('purok_name')
    return JsonResponse(list(puroks.values('id', 'purok_name')), safe=False)

