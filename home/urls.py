from django.urls import path

from . import as_address_views, as_auth_views, as_farm_views, as_profile_views

urlpatterns = [
#Authentication
    path("accounts/login/",as_auth_views.login_view,name='login'),
    path('accounts/logout/', as_auth_views.logout_view, name='signout'),

#addresses
    path('address/list', as_address_views.address, name='address-list'),
    path('address/add', as_address_views.add_address, name='add-address'),
    path('address/<int:pk>/edit', as_address_views.edit_address, name='edit-address'),
    path('edit/<int:pk>/edit', as_address_views.delete_address, name='delete-address'),
    #region
    path("region/list",as_address_views.region, name='region'),
    path("region/add",as_address_views.add_region, name='add-region'),
    path('region/<int:pk>/edit/', as_address_views.edit_region, name='edit-region'),
    path('region/<int:pk>/delete/', as_address_views.delete_region, name='delete-region'),
    #province
    path("province/list",as_address_views.province, name='province'),
    path("province/add",as_address_views.add_province, name='add-province'),
    path('province/<int:pk>/edit/', as_address_views.edit_province, name='edit-province'),
    path('province/<int:pk>/delete/', as_address_views.delete_province, name='delete-province'),
    #district
    path("district/list",as_address_views.district, name='district'),
    path("district/add",as_address_views.add_district, name='add-district'),
    path('district/<int:pk>/edit/', as_address_views.edit_district, name='edit-district'),
    path('district/<int:pk>/delete/', as_address_views.delete_district, name='delete-district'),
    #municipality
    path("municipality/list",as_address_views.municipality, name='municipality'),
    path("municipality/add",as_address_views.add_municipality, name='add-municipality'),
    path('municipality/<int:pk>/edit/', as_address_views.edit_municipality, name='edit-municipality'),
    path('municipality/<int:pk>/delete/', as_address_views.delete_municipality, name='delete-municipality'),
    #barangay
    path("barangay/list",as_address_views.barangay, name='barangay'),
    path("barangay/add",as_address_views.add_barangay, name='add-barangay'),
    path('barangay/<int:pk>/edit/', as_address_views.edit_barangay, name='edit-barangay'),
    path('barangay/<int:pk>/delete/', as_address_views.delete_barangay, name='delete-barangay'),
    #purok
    path("purok/list",as_address_views.purok, name='purok'),
    path("purok/add",as_address_views.add_purok, name='add-purok'),
    path('purok/<int:pk>/edit/', as_address_views.edit_purok, name='edit-purok'),
    path('purok/<int:pk>/delete/', as_address_views.delete_purok, name='delete-purok'),

    #address selector
    path('ajax/load-provinces/', as_address_views.load_provinces, name='ajax_load_provinces'),
    path('ajax/load-districts/', as_address_views.load_districts, name='ajax_load_districts'),
    path('ajax/load-cities/', as_address_views.load_cities, name='ajax_load_cities'),
    path('ajax/load-barangays/', as_address_views.load_barangays, name='ajax_load_barangays'),
    path('ajax/load-puroks/', as_address_views.load_puroks, name='ajax_load_puroks'),
###############################################################################################################


#profile
    path('profile-list/', as_profile_views.profile, name='profile-list'),
    path('profile/details/', as_profile_views.get_profile_details, name='get-profile-details'),
    path("profile/add",as_profile_views.add_profile, name='add-profile'),
    path('profile/<int:pk>/edit/', as_profile_views.edit_profile, name='edit-profile'),
    path('profile/<int:pk>/delete/', as_profile_views.delete_profile, name='delete-profile'),
    #religion
    path('religion-list/', as_profile_views.religion, name='religion-list'),
    path("religion/add",as_profile_views.add_religion, name='add-religion'),
    path('religion/<int:pk>/edit/', as_profile_views.edit_religion, name='edit-religion'),
    path('religion/<int:pk>/delete/', as_profile_views.delete_religion, name='delete-religion'),
    #tribe
    path('tribe-list/', as_profile_views.tribe, name='tribe-list'),
    path("tribe/add",as_profile_views.add_tribe, name='add-tribe'),
    path('tribe/<int:pk>/edit/', as_profile_views.edit_tribe, name='edit-tribe'),
    path('tribe/<int:pk>/delete/', as_profile_views.delete_tribe, name='delete-tribe'),
    #organization
    path('organization-list/', as_profile_views.organization, name='organization-list'),
    path("organization/add",as_profile_views.add_organization, name='add-organization'),
    path('organization/<int:pk>/edit/', as_profile_views.edit_organization, name='edit-organization'),
    path('organization/<int:pk>/delete/', as_profile_views.delete_organization, name='delete-organization'),
    #occupation
    path('occupation-list/', as_profile_views.occupation, name='occupation-list'),
    path("occupation/add",as_profile_views.add_occupation, name='add-occupation'),
    path('occupation/<int:pk>/edit/', as_profile_views.edit_occupation, name='edit-occupation'),
    path('occupation/<int:pk>/delete/', as_profile_views.delete_occupation, name='delete-occupation'),
    #profile_occupation
    path('profile_occupation-list/', as_profile_views.profile_occupation, name='profile_occupation-list'),
    path("profile_occupation/add",as_profile_views.add_profile_occupation, name='add-profile-occupation'),
    path('profile_occupation/<int:pk>/edit/', as_profile_views.edit_profile_occupation, name='edit-profile-occupation'),
    path('profile_occupation/<int:pk>/delete/', as_profile_views.delete_profile_occupation, name='delete-profile-occupation'),
    #profile_organization
    path('profile_organization-list/', as_profile_views.profile_organization, name='profile_organization-list'),
    path("profile_organization/add",as_profile_views.add_profile_organization, name='add-profile_organization'),
    path('profile_organization/<int:pk>/edit/', as_profile_views.edit_profile_organization, name='edit-profile_organization'),
    path('profile_organization/<int:pk>/delete/', as_profile_views.delete_profile_organization, name='delete-profile_organization'),
    #dependents
    path('dependents-list/', as_profile_views.dependents, name='dependents-list'),
    path("dependent/add",as_profile_views.add_dependent, name='add-dependent'),
    path('dependent/<int:pk>/edit/', as_profile_views.edit_dependent, name='edit-dependent'),
    path('dependent/<int:pk>/delete/', as_profile_views.delete_dependent, name='delete-dependent'),
###################################################################################################################

#farm
    path('farm-list/', as_farm_views.farm, name='farm-list'),
    path("farm/add",as_farm_views.add_farm, name='add-farm'),
    path('farm/<int:pk>/edit/', as_farm_views.edit_farm, name='edit-farm'),
    path('farm/<int:pk>/delete/', as_farm_views.delete_farm, name='delete-farm'),
    #farmcrop
    path('farm_crop-list/', as_farm_views.farm_crop, name='farm_crop-list'),
    path("farm_crop/add",as_farm_views.add_farm_crop, name='add-farmcrop'),
    path('farm_crop/<int:pk>/edit/', as_farm_views.edit_farm_crop, name='edit-farmcrop'),
    path('farm_crop/<int:pk>/delete/', as_farm_views.delete_farm_crop, name='delete-farmcrop'),
    #crop
    path('crop-list/', as_farm_views.crop, name='crop-list'),
    path("crop/add",as_farm_views.add_crop, name='add-crop'),
    path('crop/<int:pk>/edit/', as_farm_views.edit_crop, name='edit-crop'),
    path('crop/<int:pk>/delete/', as_farm_views.delete_crop, name='delete-crop'),
    #farmpicture
    path('farm_picture-list/', as_farm_views.farm_picture, name='farm_picture-list'),
    path("farm_picture/add",as_farm_views.add_farm_picture, name='add-farm_picture'),
    path('farm_picture/<int:pk>/edit/', as_farm_views.edit_farm_picture, name='edit-farm_picture'),
    path('farm_picture/<int:pk>/delete/', as_farm_views.delete_farm_picture, name='delete-farm_picture'),

]
