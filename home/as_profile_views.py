from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.contrib.auth import logout, authenticate,login
from django.http import JsonResponse
from .models import Profile, Religion, Tribe, Organization,Occupation, ProfileOccupation,ProfileOrganization, Dependents
from .forms import ProfileForm, ReligionForm, TribeForm,OccupationForm ,OrganizationForm, ProfileOccupationForm, ProfileOrganizationForm, DependentsForm

#profile
###############################################################################################################

@login_required
def profile(request):
    profiles = Profile.objects.all()
    context = {
        'parent': 'profiles',
        'segment': 'profiles',
        'profiles': profiles,
    }
    return render(request, 'user/profile/profile.html', context)

@login_required
def add_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
    else:
        form = ProfileForm()
    return save_profile(request, form, 'user/profile/add_profile.html')

@login_required
def edit_profile(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
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
        form = ProfileOrganizationForm(request.POST)
    else:
        form = ProfileOrganizationForm()
    return save_profile_organization(request, form, 'user/profile/profile_organization/add_profile_organization.html')

@login_required
def edit_profile_organization(request, pk):
    profile_organization = get_object_or_404(ProfileOrganization, pk=pk)
    if request.method == 'POST':
        form = ProfileOrganizationForm(request.POST, instance=profile_organization)
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
