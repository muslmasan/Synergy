from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile
from django import forms
from django.utils.html import format_html
import base64


class UserProfileForm(forms.ModelForm):
    image_file = forms.ImageField(required=False, label="Profile Image")  # Field for uploading the image
    cover_file = forms.ImageField(required=False, label="Cover Image")    # Field for uploading the cover

    class Meta:
        model = UserProfile
        exclude = ['image', 'cover']  # Exclude the BinaryField from the form

    def save(self, commit=True):
        instance = super().save(commit=False)

        # Handle the image field
        image_file = self.cleaned_data.get('image_file')
        if image_file:
            instance.image = image_file.read()

        # Handle the cover field
        cover_file = self.cleaned_data.get('cover_file')
        if cover_file:
            instance.cover = cover_file.read()

        if commit:
            instance.save()
        return instance


class UserProfileAdmin(admin.ModelAdmin):
    form = UserProfileForm
    list_display = ('email', 'username', 'is_staff', 'is_active', 'created_at','image_tag')
    readonly_fields = ('created_at', 'updated_at')  # Fields that are not editable
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'bio', 'gender', 'image_file', 'cover_file')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'created_at', 'updated_at')}),
    )

    def image_tag(self, obj):
        if obj.image:
            # Ensure obj.image is in the proper format (bytes) for base64 encoding
            encoded_image = base64.b64encode(obj.image).decode('utf-8')
            return format_html('<img src="data:image/jpeg;base64,{}" style="width: 50px; height: 50px;" />', encoded_image)
        return "No Image"

    image_tag.short_description = "Profile Image"
    
admin.site.register(UserProfile, UserProfileAdmin)
