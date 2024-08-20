from django import forms
from .models import SummaryStudent

class SummaryStudentForm(forms.ModelForm):
    class Meta:
        model = SummaryStudent
        fields = [
            'student_id',
            'student_name', 
            'school',
            'sydney_participant',
            'sydney_percentile',
            'assessment_area',
            'award',
            'class_name',
            'correct_answer_percentage_per_class',
            'correct_answer',
            'participant',
            'student_score',
            'subject',
            'category_id',
            'year_level_name',
            'answer',
            'correct_answer_id'
        ]
