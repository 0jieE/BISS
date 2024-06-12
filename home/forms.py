from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, UsernameField, PasswordResetForm, SetPasswordForm
from django.utils.translation import gettext_lazy as _
from .models import (
    User, Region, Province, District, CityMunicipality, Barangay, Purok,
    Religion, Tribe, Organization, Occupation, Profile, ProfileOccupation,
    Farm, Crop, FarmCrop, FarmPicture, ProfileOrganization, Address, Dependents
)

class LoginForm(forms.Form):
  username = UsernameField(label=_("Your Username"), widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"}))
  password = forms.CharField(
      label=_("Your Password"),
      strip=False,
      widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"}),
  )

class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = ['region_name', 'region_short']
        widgets = {
            'region_name': forms.TextInput(attrs={'class': 'form-control'}),
            'region_short': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ProvinceForm(forms.ModelForm):
    class Meta:
        model = Province
        fields = ['province_name', 'region']
        widgets = {
            'province_name': forms.TextInput(attrs={'class': 'form-control'}),
            'region': forms.Select(attrs={'class': 'form-control'}),
        }

class DistrictForm(forms.ModelForm):
    class Meta:
        model = District
        fields = ['district_name', 'province']
        widgets = {
            'district_name': forms.TextInput(attrs={'class': 'form-control'}),
            'province': forms.Select(attrs={'class': 'form-control'}),
        }

class CityMunicipalityForm(forms.ModelForm):
    class Meta:
        model = CityMunicipality
        fields = ['municipality_name', 'zip_code', 'district']
        widgets = {
            'municipality_name': forms.TextInput(attrs={'class': 'form-control'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control'}),
            'district': forms.Select(attrs={'class': 'form-control'}),
        }

class BarangayForm(forms.ModelForm):
    class Meta:
        model = Barangay
        fields = ['barangay_name', 'municipality']
        widgets = {
            'barangay_name': forms.TextInput(attrs={'class': 'form-control'}),
            'municipality': forms.Select(attrs={'class': 'form-control'}),
        }

class PurokForm(forms.ModelForm):
    class Meta:
        model = Purok
        fields = ['purok_name', 'barangay']
        widgets = {
            'purok_name': forms.TextInput(attrs={'class': 'form-control'}),
            'barangay': forms.Select(attrs={'class': 'form-control'}),
        }

class ReligionForm(forms.ModelForm):
    class Meta:
        model = Religion
        fields = ['religion_name']
        widgets = {
            'religion_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class TribeForm(forms.ModelForm):
    class Meta:
        model = Tribe
        fields = ['tribe_name']
        widgets = {
            'tribe_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['organization_name']
        widgets = {
            'organization_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class OccupationForm(forms.ModelForm):
    class Meta:
        model = Occupation
        fields = ['occupation_name']
        widgets = {
            'occupation_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'last_name', 'first_name', 'middle_name', 'extension_name', 'birth_date',
            'gender', 'civil_status', 'citizenship', 'religion', 'contact_no',
            'email_address', 'facebook_account', 'household_head', 'beneficiary_4p',
            'indigenous_group', 'tribe', 'spouse_name', 'spouse_occupation',
            'member_organization', 'skills', 'pwd', 'education', 'picture'
        ]
        widgets = {
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control'}),
            'extension_name': forms.TextInput(attrs={'class': 'form-control'}),
            'birth_date': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'civil_status': forms.Select(attrs={'class': 'form-control'}),
            'citizenship': forms.Select(attrs={'class': 'form-control'}),
            'religion': forms.Select(attrs={'class': 'form-control'}),
            'contact_no': forms.TextInput(attrs={'class': 'form-control'}),
            'email_address': forms.EmailInput(attrs={'class': 'form-control'}),
            'facebook_account': forms.TextInput(attrs={'class': 'form-control'}),
            'household_head': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'beneficiary_4p': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'indigenous_group': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'tribe': forms.Select(attrs={'class': 'form-control'}),
            'spouse_name': forms.TextInput(attrs={'class': 'form-control'}),
            'spouse_occupation': forms.TextInput(attrs={'class': 'form-control'}),
            'member_organization': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'skills': forms.Textarea(attrs={'class': 'form-control'}),
            'pwd': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'education': forms.Select(attrs={'class': 'form-control'}),
            'picture': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }

class ProfileOccupationForm(forms.ModelForm):
    class Meta:
        model = ProfileOccupation
        fields = ['profile', 'occupation', 'occupation_description']
        widgets = {
            'profile': forms.Select(attrs={'class': 'form-control'}),
            'occupation': forms.Select(attrs={'class': 'form-control'}),
            'occupation_description': forms.Textarea(attrs={'class': 'form-control'}),
        }

class FarmForm(forms.ModelForm):
    class Meta:
        model = Farm
        fields = [
            'profile', 'farm_description', 'is_owner', 'owner_name', 'is_tenant',
            'tenant_name', 'is_maintainer', 'maintainer_name', 'notes', 'latitude',
            'longitude', 'altitude', 'area', 'farm_type', 'farm_crop'
        ]
        widgets = {
            'profile': forms.Select(attrs={'class': 'form-control'}),
            'farm_description': forms.Textarea(attrs={'class': 'form-control'}),
            'is_owner': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'owner_name': forms.TextInput(attrs={'class': 'form-control'}),
            'is_tenant': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'tenant_name': forms.TextInput(attrs={'class': 'form-control'}),
            'is_maintainer': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'maintainer_name': forms.TextInput(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control'}),
            'latitude': forms.NumberInput(attrs={'class': 'form-control'}),
            'longitude': forms.NumberInput(attrs={'class': 'form-control'}),
            'altitude': forms.NumberInput(attrs={'class': 'form-control'}),
            'area': forms.NumberInput(attrs={'class': 'form-control'}),
            'farm_type': forms.Select(attrs={'class': 'form-control'}),
            'farm_crop': forms.Select(attrs={'class': 'form-control'}),
        }

class CropForm(forms.ModelForm):
    class Meta:
        model = Crop
        fields = ['crop_name', 'crop_description']
        widgets = {
            'crop_name': forms.TextInput(attrs={'class': 'form-control'}),
            'crop_description': forms.Textarea(attrs={'class': 'form-control'}),
        }

class FarmCropForm(forms.ModelForm):
    class Meta:
        model = FarmCrop
        fields = [
            'farm', 'crop', 'area', 'crop_qnty', 'income', 'is_farming',
            'farm_crop_description'
        ]
        widgets = {
            'farm': forms.Select(attrs={'class': 'form-control'}),
            'crop': forms.Select(attrs={'class': 'form-control'}),
            'area': forms.NumberInput(attrs={'class': 'form-control'}),
            'crop_qnty': forms.NumberInput(attrs={'class': 'form-control'}),
            'income': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_farming': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'farm_crop_description': forms.Textarea(attrs={'class': 'form-control'}),
        }

class FarmPictureForm(forms.ModelForm):
    class Meta:
        model = FarmPicture
        fields = ['farm', 'picture']
        widgets = {
            'farm': forms.Select(attrs={'class': 'form-control'}),
            'picture': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }

class ProfileOrganizationForm(forms.ModelForm):
    class Meta:
        model = ProfileOrganization
        fields = ['profile', 'organization']
        widgets = {
            'profile': forms.Select(attrs={'class': 'form-control'}),
            'organization': forms.Select(attrs={'class': 'form-control'}),
        }

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = [
            'profile', 'house_number', 'address_type', 'region', 'province',
            'district', 'municipality', 'barangay', 'purok',
        ]
        widgets = {
            'profile': forms.Select(attrs={'class': 'form-control'}),
            'house_number': forms.TextInput(attrs={'class': 'form-control'}),
            'address_type': forms.TextInput(attrs={'class': 'form-control'}),
            'region': forms.Select(attrs={'id': 'id_region'}),
            'province': forms.Select(attrs={'id': 'id_province'}),
            'district': forms.Select(attrs={'id': 'id_district'}),
            'municipality': forms.Select(attrs={'id': 'id_municipality'}),
            'barangay': forms.Select(attrs={'id': 'id_barangay'}),
            'purok': forms.Select(attrs={'id': 'id_purok'}),

        }

class DependentsForm(forms.ModelForm):
    class Meta:
        model = Dependents
        fields = ['profile', 'last_name', 'first_name', 'middle_name', 'ext_name', 'birth_date', 'education']
        widgets = {
            'profile': forms.Select(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control'}),
            'ext_name': forms.TextInput(attrs={'class': 'form-control'}),
            'birth_date': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'education': forms.Select(attrs={'class': 'form-control'}),
        }

