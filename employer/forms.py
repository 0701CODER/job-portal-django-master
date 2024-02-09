from django import forms

from .models import Company, Job, Category


class EmployerProfileForm(forms.ModelForm):

    class Meta:
        model = Company
        fields=['category', 'name', 'co_introduction', 'logo', 'link']

    def __init__(self, *args, **kwargs):
        super(EmployerProfileForm, self).__init__(*args, **kwargs)
        self.fields['category'].label = "Select your company category"
        self.fields['name'].label = "Enter your company name"
        self.fields['co_introduction'].label = "Introduce your company"
        self.fields['logo'].label = "Upload your logo"
        self.fields['link'].label = "Enter your website link"

class EmployerJobCreationForm(forms.ModelForm):
    
    class Meta:
        model = Job
        fields = [
            'category', 'title', 'location',
            'experience', 'salary', 'cooperation_type',
            'job_description', 'skills_required',
            'military_service', 'degree', 'gender',
        ]
    
    def __init__(self, *args, **kwargs):
        super(EmployerJobCreationForm, self).__init__(*args, **kwargs)
        self.fields['category'].label = "Choose your ad category"
        self.fields['title'].label = "Enter ad title"
        self.fields['location'].label = "Enter the location of the company"
        self.fields['experience'].label = "Required work experience"
        self.fields['salary'].label = "Salary"
        self.fields['cooperation_type'].label = "Type of cooperation"
        self.fields['job_description'].label = "Job description"
        self.fields['skills_required'].label = "Required Skills"
        self.fields['military_service'].label = "Military Status"
        self.fields['gender'].label = "Gender"
        self.fields['degree'].label = "Education"



