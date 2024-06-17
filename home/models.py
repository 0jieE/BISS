from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
import os

def profile_picture_path(instance, filename):
    return os.path.join('profile_pictures', filename)

class CustomUserManager(BaseUserManager):
    def create_user(self, username, first_name, last_name, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, first_name, last_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, first_name, last_name, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('staff', 'Staff'),
        ('user', 'User')
    ]

    username = models.CharField(max_length=255, unique=True)
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    picture = models.ImageField(upload_to='user_pictures/', blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.username})'



class Region(models.Model):
    region_name = models.CharField(max_length=255)
    region_short = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.region_name

class Province(models.Model):
    province_name = models.CharField(max_length=255)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.province_name

class District(models.Model):
    district_name = models.CharField(max_length=255)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.district_name

class CityMunicipality(models.Model):
    municipality_name = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=10)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.municipality_name

class Barangay(models.Model):
    barangay_name = models.CharField(max_length=255)
    municipality = models.ForeignKey(CityMunicipality, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.barangay_name

class Purok(models.Model):
    purok_name = models.CharField(max_length=255)
    barangay = models.ForeignKey(Barangay, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.purok_name

class Religion(models.Model):
    religion_name = models.CharField(max_length=255)

    def __str__(self):
        return self.religion_name

class Tribe(models.Model):
    tribe_name = models.CharField(max_length=255)

    def __str__(self):
        return self.tribe_name

class Organization(models.Model):
    organization_name = models.CharField(max_length=255)

    def __str__(self):
        return self.organization_name

class Occupation(models.Model):
    occupation_name = models.CharField(max_length=255)

    def __str__(self):
        return self.occupation_name

class Profile(models.Model):
    SEX_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female')
    ]
    CIVIL_STATUS_CHOICES = [
        ('single', 'Single'),
        ('married', 'Married'),
        ('widowed', 'Widowed'),
        ('separated', 'Separated'),
        ('annulled', 'Annulled')
    ]
    CITIZENSHIP_CHOICES = [
        ('natural_born', 'Natural Born'),
        ('dual_by_birth', 'Dual by Birth'),
        ('dual_by_naturalization', 'Dual by Naturalization')
    ]
    EDUCATION_CHOICES = [
        ('none', 'None'),
        ('elementary', 'Elementary'),
        ('secondary', 'Secondary'),
        ('tertiary', 'Tertiary'),
        ('college_graduate', 'College Graduate'),
        ('post_graduate', 'Post Graduate')
    ]
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    extension_name = models.CharField(max_length=255, blank=True, null=True)
    birth_date = models.DateTimeField()
    gender = models.CharField(max_length=6, choices=SEX_CHOICES, default='male')
    civil_status = models.CharField(max_length=10, choices=CIVIL_STATUS_CHOICES, default='single')
    citizenship = models.CharField(max_length=50, choices=CITIZENSHIP_CHOICES, default='natural_born')
    religion = models.ForeignKey(Religion, on_delete=models.CASCADE)
    contact_no = models.CharField(max_length=255)
    email_address = models.EmailField()
    facebook_account = models.CharField(max_length=255, blank=True, null=True)
    household_head = models.BooleanField(default=False)
    beneficiary_4p = models.BooleanField(default=False)
    indigenous_group = models.BooleanField(default=False)
    tribe = models.ForeignKey(Tribe, on_delete=models.CASCADE, blank=True, null=True)
    spouse_name = models.CharField(max_length=255, blank=True, null=True)
    spouse_occupation = models.CharField(max_length=255, blank=True, null=True)
    member_organization = models.BooleanField(default=False)
    skills = models.TextField(blank=True, null=True)
    pwd = models.BooleanField(default=False)
    education = models.CharField(max_length=20, choices=EDUCATION_CHOICES, default='none')
    picture = models.ImageField(upload_to=profile_picture_path, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def get_picture_url(self):
        if self.picture:
            return self.picture.url
        else:
            return '/profile_pictures/logo1.jpg' 

    def __str__(self):
        if self.extension_name:
            return f"{self.first_name} {self.middle_name} {self.last_name} {self.extension_name}"
        else:
            return f"{self.first_name} {self.middle_name} {self.last_name}"

class ProfileOccupation(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    occupation = models.ForeignKey(Occupation, on_delete=models.CASCADE)
    occupation_description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

class Farm(models.Model):
    FARM_TYPE_CHOICES = [
        ('upload', 'Upload'),
        ('lowland', 'Lowland')
    ]
    FARM_CROP_CHOICES = [
        ('monocrop', 'Monocrop'),
        ('intercrop', 'Intercrop')
    ]
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    farm_description = models.TextField()
    is_owner = models.BooleanField(default=False)
    owner_name = models.CharField(max_length=255, blank=True, null=True)
    is_tenant = models.BooleanField(default=False)
    tenant_name = models.CharField(max_length=255, blank=True, null=True)
    is_maintainer = models.BooleanField(default=False)
    maintainer_name = models.CharField(max_length=255, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    latitude = models.DecimalField(max_digits=20, decimal_places=16)
    longitude = models.DecimalField(max_digits=20, decimal_places=16)
    altitude = models.DecimalField(max_digits=20, decimal_places=16, blank=True, null=True)
    area = models.DecimalField(max_digits=10, decimal_places=2)
    farm_type = models.CharField(max_length=10, choices=FARM_TYPE_CHOICES, default='lowland')
    farm_crop = models.CharField(max_length=10, choices=FARM_CROP_CHOICES, default='intercrop')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        template = '{0.profile}'
        return template.format(self)

class Crop(models.Model):
    crop_name = models.CharField(max_length=255)
    crop_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.crop_name

class FarmCrop(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    area = models.DecimalField(max_digits=10, decimal_places=2)
    crop_qnty = models.DecimalField(max_digits=10, decimal_places=2)
    income = models.DecimalField(max_digits=10, decimal_places=2)
    is_farming = models.BooleanField(default=True)
    farm_crop_description = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

class FarmPicture(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='farm_pictures/')

class ProfileOrganization(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

class Address(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    house_number = models.CharField(max_length=255)
    address_type = models.CharField(max_length=255)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    municipality = models.ForeignKey(CityMunicipality, on_delete=models.CASCADE)
    barangay = models.ForeignKey(Barangay, on_delete=models.CASCADE)
    purok = models.ForeignKey(Purok, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.house_number}, {self.purok}, {self.barangay}, {self.municipality}, {self.district}, {self.province}, {self.region}"

class Dependents(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    ext_name = models.CharField(max_length=255, blank=True, null=True)
    birth_date = models.DateTimeField()
    education = models.CharField(max_length=20, choices=Profile.EDUCATION_CHOICES, default='none')

    def __str__(self):
        if self.ext_name:
            return f"{self.first_name} {self.middle_name} {self.last_name} {self.ext_name}"
        else:
            return f"{self.first_name} {self.middle_name} {self.last_name}"