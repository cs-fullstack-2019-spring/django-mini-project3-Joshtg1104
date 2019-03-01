from django import forms
from .models import TeacherTimeModel


class TeachTimeForm(forms.ModelForm):
    class Meta:
        model = TeacherTimeModel
        fields = ["teacher_name", "school_name", "subject_teaching", "daily_hours_taught", "date_of_work"]
