from django.db import models

class Course(models.Model):
  title = models.CharField(max_length=100)
  max_students = models.IntegerField(default=0)
  start_date = models.DateField()
  end_date = models.DateField()
  def __str__(self):
    return self.title

class Staff(models.Model):
  name = models.CharField(max_length=100)
  course = models.ForeignKey(Course, on_delete=models.CASCADE)
  def __str__(self):
    return self.name

class Student(models.Model):
  name = models.CharField(max_length=100)
  course = models.ForeignKey(Course, on_delete=models.CASCADE)
  def __str__(self):
    return self.name
