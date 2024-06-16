from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.contrib.auth import logout, authenticate,login
from django.http import JsonResponse
from .models import Profile, Religion, Tribe, Organization,Occupation, ProfileOccupation,ProfileOrganization, Dependents, Address,\
                    Farm, FarmCrop, Religion, Tribe, Region, Province, District, CityMunicipality, Barangay, Purok
from .forms import ProfileForm, ReligionForm, TribeForm,OccupationForm ,OrganizationForm, ProfileOccupationForm, ProfileOrganizationForm, DependentsForm
from datetime import date
import decimal

#profile
###############################################################################################################
def calculate_age(birth_date):
    today = date.today()
    return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))


@login_required
def profile(request):
    profiles = Profile.objects.all()
    context = {
        'parent': '',
        'segment': 'profiles',
        'profiles': profiles,
    }
    return render(request, 'user/profile/profile.html', context)


def serialize_model_instance(instance, fields):
    """Helper function to serialize a model instance to a dictionary."""
    data = {}
    for field in fields:
        value = getattr(instance, field)
        if isinstance(value, (Religion, Tribe, Region, Province, District, CityMunicipality, Barangay, Purok)):
            data[field] = str(value)
        elif hasattr(value, 'isoformat'):  # For datetime fields
            data[field] = value.isoformat()
        elif isinstance(value, (int, float, bool, str)):
            data[field] = value
        elif isinstance(value, decimal.Decimal):
            data[field] = float(value)
        else:
            data[field] = str(value)
    return data

def get_profile_details(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest' and request.method == 'GET':
        profile_id = request.GET.get('profile_id')
        profile = get_object_or_404(Profile, pk=profile_id)

        # Fetch related Address
        address = Address.objects.filter(profile=profile).first()
        address_fields = [
            'address_type', 'house_number', 'region', 'province',
            'district', 'municipality', 'barangay', 'purok'
        ]
        address_data = serialize_model_instance(address, address_fields) if address else {}

        # Fetch related Dependents
        dependents = Dependents.objects.filter(profile=profile)
        dependents_fields = ['first_name', 'last_name', 'ext_name', 'birth_date']
        dependents_data = [
            serialize_model_instance(dep, dependents_fields) for dep in dependents
        ] if dependents.exists() else []

        # Fetch related Farms and their FarmCrops
        farms = Farm.objects.filter(profile=profile)
        farms_data = []
        for farm in farms:
            farm_crops = FarmCrop.objects.filter(farm=farm)
            farm_crop_fields = ['crop', 'area', 'crop_qnty', 'income', 'is_farming', 'farm_crop_description']
            farm_crops_data = [
                serialize_model_instance(farm_crop, farm_crop_fields) for farm_crop in farm_crops
            ]
            farm_fields = ['farm_description', 'is_owner', 'owner_name', 'is_tenant', 'tenant_name',
                           'is_maintainer', 'maintainer_name', 'notes', 'latitude', 'longitude',
                           'altitude', 'area', 'farm_type', 'farm_crop']
            farm_data = serialize_model_instance(farm, farm_fields)
            farm_data['farm_crops'] = farm_crops_data
            farms_data.append(farm_data)

        # Serialize the profile object
        profile_fields = [
            'email_address', 'facebook_account', 'civil_status', 'citizenship',
            'household_head', 'beneficiary_4p', 'indigenous_group', 'spouse_name',
            'spouse_occupation', 'member_organization', 'skills', 'pwd', 'created_on', 'education'
        ]
        data = serialize_model_instance(profile, profile_fields)
        data.update({
            # 'image_url': profile.get_picture_url() if callable(profile.get_picture_url) else profile.get_picture_url,
            'religion': str(profile.religion),
            'tribe': str(profile.tribe) if profile.tribe else None,
            'created_on': profile.created_on.isoformat() if profile.created_on else None,
            'address': address_data,
            'dependents': dependents_data,
            'farms': farms_data
        })
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Invalid request'})











@login_required
def add_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
    else:
        form = ProfileForm()
    return save_profile(request, form, 'user/profile/add_profile.html')

@login_required
def edit_profile(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
    else:
        form = ProfileForm(instance=profile)
    return save_profile(request, form, 'user/profile/edit_profile.html')

@login_required
def delete_profile(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    data = dict()
    if request.method == 'POST':
        profile.delete()
        data['form_is_valid'] = True
        profiles = Profile.objects.all()
        data['profile_list'] = render_to_string('user/profile/list_profile.html', {'profiles': profiles})
    else:
        context = {'profile': profile}
        data['html_form'] = render_to_string('user/profile/delete_profile.html', context, request=request)
    return JsonResponse(data)

def save_profile(request, form, template_name):
    data = dict()
    if form.is_valid():
        form.save()
        data['form_is_valid'] = True
        profiles = Profile.objects.all()
        data['profile_list'] = render_to_string('user/profile/list_profile.html', {'profiles': profiles})
    else:
        data['form_is_valid'] = False

    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


#religion
###############################################################################################################

@login_required
def religion(request):
    religions = Religion.objects.all()
    context = {
        'parent': 'profile-data',
        'segment': 'religions',
        'religions': religions,
    }
    return render(request, 'user/profile/religion/religion.html', context)

@login_required
def add_religion(request):
    if request.method == 'POST':
        form = ReligionForm(request.POST)
    else:
        form = ReligionForm()
    return save_religion(request, form, 'user/profile/religion/add_religion.html')

@login_required
def edit_religion(request, pk):
    religion = get_object_or_404(Religion, pk=pk)
    if request.method == 'POST':
        form = ReligionForm(request.POST, instance=religion)
    else:
        form = ReligionForm(instance=religion)
    return save_religion(request, form, 'user/profile/religion/edit_religion.html')

@login_required
def delete_religion(request, pk):
    religion = get_object_or_404(Religion, pk=pk)
    data = dict()
    if request.method == 'POST':
        religion.delete()
        data['form_is_valid'] = True
        religions = Religion.objects.all()
        data['religion_list'] = render_to_string('user/profile/religion/list_religion.html', {'religions': religions})
    else:
        context = {'religion': religion}
        data['html_form'] = render_to_string('user/profile/religion/delete_religion.html', context, request=request)
    return JsonResponse(data)

def save_religion(request, form, template_name):
    data = dict()
    if form.is_valid():
        form.save()
        data['form_is_valid'] = True
        religions = Religion.objects.all()
        data['religion_list'] = render_to_string('user/profile/religion/list_religion.html', {'religions': religions})
    else:
        data['form_is_valid'] = False

    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

#tribe
###############################################################################################################

@login_required
def tribe(request):
    tribes = Tribe.objects.all()
    context = {
        'parent': 'profile-data',
        'segment': 'tribes',
        'tribes': tribes,
    }
    return render(request, 'user/profile/tribe/tribe.html', context)

@login_required
def add_tribe(request):
    if request.method == 'POST':
        form = TribeForm(request.POST)
    else:
        form = TribeForm()
    return save_tribe(request, form, 'user/profile/tribe/add_tribe.html')

@login_required
def edit_tribe(request, pk):
    tribe = get_object_or_404(Tribe, pk=pk)
    if request.method == 'POST':
        form = TribeForm(request.POST, instance=tribe)
    else:
        form = TribeForm(instance=tribe)
    return save_tribe(request, form, 'user/profile/tribe/edit_tribe.html')

@login_required
def delete_tribe(request, pk):
    tribe = get_object_or_404(Tribe, pk=pk)
    data = dict()
    if request.method == 'POST':
        tribe.delete()
        data['form_is_valid'] = True
        tribes = Tribe.objects.all()
        data['tribe_list'] = render_to_string('user/profile/tribe/list_tribe.html', {'tribes': tribes})
    else:
        context = {'tribe': tribe}
        data['html_form'] = render_to_string('user/profile/tribe/delete_tribe.html', context, request=request)
    return JsonResponse(data)

def save_tribe(request, form, template_name):
    data = dict()
    if form.is_valid():
        form.save()
        data['form_is_valid'] = True
        tribes = Tribe.objects.all()
        data['tribe_list'] = render_to_string('user/profile/tribe/list_tribe.html', {'tribes': tribes})
    else:
        data['form_is_valid'] = False

    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


#organization
###############################################################################################################

@login_required
def organization(request):
    organizations = Organization.objects.all()
    context = {
        'parent': 'profile-data',
        'segment': 'organizations',
        'organizations': organizations,
    }
    return render(request, 'user/profile/organization/organization.html', context)

@login_required
def add_organization(request):
    if request.method == 'POST':
        form = OrganizationForm(request.POST)
    else:
        form = OrganizationForm()
    return save_organization(request, form, 'user/profile/organization/add_organization.html')

@login_required
def edit_organization(request, pk):
    organization = get_object_or_404(Organization, pk=pk)
    if request.method == 'POST':
        form = OrganizationForm(request.POST, instance=organization)
    else:
        form = OrganizationForm(instance=organization)
    return save_organization(request, form, 'user/profile/organization/edit_organization.html')

@login_required
def delete_organization(request, pk):
    organization = get_object_or_404(Organization, pk=pk)
    data = dict()
    if request.method == 'POST':
        organization.delete()
        data['form_is_valid'] = True
        organizations = Organization.objects.all()
        data['organization_list'] = render_to_string('user/profile/organization/list_organization.html', {'organizations': organizations})
    else:
        context = {'organization': organization}
        data['html_form'] = render_to_string('user/profile/organization/delete_organization.html', context, request=request)
    return JsonResponse(data)

def save_organization(request, form, template_name):
    data = dict()
    if form.is_valid():
        form.save()
        data['form_is_valid'] = True
        organizations = Organization.objects.all()
        data['organization_list'] = render_to_string('user/profile/organization/list_organization.html', {'organizations': organizations})
    else:
        data['form_is_valid'] = False

    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

#profile_oocupation
###############################################################################################################

@login_required
def profile_occupation(request):
    profile_occupations = ProfileOccupation.objects.all()
    context = {
        'parent': '',
        'segment': 'profile_occupations',
        'profile_occupations': profile_occupations,
    }
    return render(request, 'user/profile/profile_occupation/profile_occupation.html', context)

@login_required
def add_profile_occupation(request):
    if request.method == 'POST':
        form = ProfileOccupationForm(request.POST)
    else:
        form = ProfileOccupationForm()
    return save_profile_occupation(request, form, 'user/profile/profile_occupation/add_profile_occupation.html')

@login_required
def edit_profile_occupation(request, pk):
    profile_occupation = get_object_or_404(ProfileOccupation, pk=pk)
    if request.method == 'POST':
        form = ProfileOccupationForm(request.POST, instance=profile_occupation)
    else:
        form = ProfileOccupationForm(instance=profile_occupation)
    return save_profile_occupation(request, form, 'user/profile/profile_occupation/edit_profile_occupation.html')

@login_required
def delete_profile_occupation(request, pk):
    profile_occupation = get_object_or_404(ProfileOccupation, pk=pk)
    data = dict()
    if request.method == 'POST':
        profile_occupation.delete()
        data['form_is_valid'] = True
        profile_occupations = ProfileOccupation.objects.all()
        data['profile_occupation_list'] = render_to_string('user/profile/profile_occupation/list_profile_occupation.html', {'profile_occupations': profile_occupations})
    else:
        context = {'profile_occupation': profile_occupation}
        data['html_form'] = render_to_string('user/profile/profile_occupation/delete_profile_occupation.html', context, request=request)
    return JsonResponse(data)

def save_profile_occupation(request, form, template_name):
    data = dict()
    if form.is_valid():
        form.save()
        data['form_is_valid'] = True
        profile_occupations = ProfileOccupation.objects.all()
        data['profile_occupation_list'] = render_to_string('user/profile/profile_occupation/list_profile_occupation.html', {'profile_occupations': profile_occupations})
    else:
        data['form_is_valid'] = False

    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

#profile_organization
###############################################################################################################

@login_required
def profile_organization(request):
    profile_organizations = ProfileOrganization.objects.all()
    context = {
        'parent': '',
        'segment': 'profile_organizations',
        'profile_organizations': profile_organizations,
    }
    return render(request, 'user/profile/profile_organization/profile_organization.html', context)

@login_required
def add_profile_organization(request):
    if request.method == 'POST':
        form = ProfileOrganizationForm(request.POST, request.FILES)
    else:
        form = ProfileOrganizationForm()
    return save_profile_organization(request, form, 'user/profile/profile_organization/add_profile_organization.html')

@login_required
def edit_profile_organization(request, pk):
    profile_organization = get_object_or_404(ProfileOrganization, pk=pk)
    if request.method == 'POST':
        form = ProfileOrganizationForm(request.POST, request.FILES, instance=profile_organization)
    else:
        form = ProfileOrganizationForm(instance=profile_organization)
    return save_profile_organization(request, form, 'user/profile/profile_organization/edit_profile_organization.html')

@login_required
def delete_profile_organization(request, pk):
    profile_organization = get_object_or_404(ProfileOrganization, pk=pk)
    data = dict()
    if request.method == 'POST':
        profile_organization.delete()
        data['form_is_valid'] = True
        profile_organizations = ProfileOrganization.objects.all()
        data['profile_organization_list'] = render_to_string('user/profile/profile_organization/list_profile_organization.html', {'profile_organizations': profile_organizations})
    else:
        context = {'profile_organization': profile_organization}
        data['html_form'] = render_to_string('user/profile/profile_organization/delete_profile_organization.html', context, request=request)
    return JsonResponse(data)

def save_profile_organization(request, form, template_name):
    data = dict()
    if form.is_valid():
        form.save()
        data['form_is_valid'] = True
        profile_organizations = ProfileOrganization.objects.all()
        data['profile_organization_list'] = render_to_string('user/profile/profile_organization/list_profile_organization.html', {'profile_organizations': profile_organizations})
    else:
        data['form_is_valid'] = False

    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

#dependents
###############################################################################################################

@login_required
def dependents(request):
    dependents_list = Dependents.objects.all()
    context = {
        'parent': 'profiles',
        'segment': 'dependents',
        'dependents': dependents_list,
    }
    return render(request, 'user/profile/dependents/dependents.html', context)

@login_required
def add_dependent(request):
    if request.method == 'POST':
        form = DependentsForm(request.POST)
    else:
        form = DependentsForm()
    return save_dependent(request, form, 'user/profile/dependents/add_dependent.html')

@login_required
def edit_dependent(request, pk):
    dependent = get_object_or_404(Dependents, pk=pk)
    if request.method == 'POST':
        form = DependentsForm(request.POST, instance=dependent)
    else:
        form = DependentsForm(instance=dependent)
    return save_dependent(request, form, 'user/profile/dependents/edit_dependent.html')

@login_required
def delete_dependent(request, pk):
    dependent = get_object_or_404(Dependents, pk=pk)
    data = dict()
    if request.method == 'POST':
        dependent.delete()
        data['form_is_valid'] = True
        dependents_list = Dependents.objects.all()
        data['dependents_list'] = render_to_string('user/profile/dependents/list_dependents.html', {'dependents': dependents_list})
    else:
        context = {'dependent': dependent}
        data['html_form'] = render_to_string('user/profile/dependents/delete_dependent.html', context, request=request)
    return JsonResponse(data)

def save_dependent(request, form, template_name):
    data = dict()
    if form.is_valid():
        form.save()
        data['form_is_valid'] = True
        dependents_list = Dependents.objects.all()
        data['dependents_list'] = render_to_string('user/profile/dependents/list_dependents.html', {'dependents': dependents_list})
    else:
        data['form_is_valid'] = False

    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

#occupation
###############################################################################################################

@login_required
def occupation(request):
    occupations = Occupation.objects.all()
    context = {
        'parent': 'profile-data',
        'segment': 'occupations',
        'occupations': occupations,
    }
    return render(request, 'user/profile/occupation/occupation.html', context)

@login_required
def add_occupation(request):
    if request.method == 'POST':
        form = OccupationForm(request.POST)
    else:
        form = OccupationForm()
    return save_occupation(request, form, 'user/profile/occupation/add_occupation.html')

@login_required
def edit_occupation(request, pk):
    occupation = get_object_or_404(Occupation, pk=pk)
    if request.method == 'POST':
        form = OccupationForm(request.POST, instance=occupation)
    else:
        form = OccupationForm(instance=occupation)
    return save_occupation(request, form, 'user/profile/occupation/edit_occupation.html')

@login_required
def delete_occupation(request, pk):
    occupation = get_object_or_404(Occupation, pk=pk)
    data = dict()
    if request.method == 'POST':
        occupation.delete()
        data['form_is_valid'] = True
        occupations = Occupation.objects.all()
        data['occupation_list'] = render_to_string('user/profile/occupation/list_occupation.html', {'occupations': occupations})
    else:
        context = {'occupation': occupation}
        data['html_form'] = render_to_string('user/profile/occupation/delete_occupation.html', context, request=request)
    return JsonResponse(data)

def save_occupation(request, form, template_name):
    data = dict()
    if form.is_valid():
        form.save()
        data['form_is_valid'] = True
        occupations = Occupation.objects.all()
        data['occupation_list'] = render_to_string('user/profile/occupation/list_occupation.html', {'occupations': occupations})
    else:
        data['form_is_valid'] = False

    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)
