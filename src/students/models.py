from django.db import models

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class School(models.Model):
    name = models.CharField(max_length=255)

class Assessment_Areas(models.Model):
    name = models.CharField(max_length=255)

class Awards(models.Model):
    title = models.CharField(max_length=255)

class Class(models.Model):
    name = models.CharField(max_length=255)

class Subject(models.Model):
    name = models.CharField(max_length=255)

class Answers(models.Model):
    content = models.TextField()

class SummaryStudent(models.Model):
    student_id = models.IntegerField(default = '1')
    student_name = models.CharField(max_length=255, default=student_id)
    school = models.CharField(max_length=255)
    sydney_participant = models.CharField(max_length=255)
    sydney_percentile = models.DecimalField(max_digits=5, decimal_places=2)
    assessment_area = models.ForeignKey('Assessment_Areas', on_delete=models.CASCADE)
    award = models.ForeignKey('Awards', on_delete=models.CASCADE)
    class_name = models.ForeignKey('Class', on_delete=models.CASCADE)
    correct_answer_percentage_per_class = models.DecimalField(max_digits=5, decimal_places=2)
    correct_answer = models.IntegerField()
    participant = models.CharField(max_length=255)
    student_score = models.DecimalField(max_digits=5, decimal_places=2)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)
    category_id = models.IntegerField()
    year_level_name = models.CharField(max_length=255)
    answer = models.ForeignKey('Answers', on_delete=models.CASCADE)
    correct_answer_id = models.IntegerField()

    def __str__(self):
        return f"{self.student.name} - {self.school}"
