from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from .utils import generate_unique_link
User = get_user_model()

class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    attachment = models.FileField(upload_to='job_attachments/', blank=True, null=True)
    posted_at = models.DateTimeField(auto_now_add=True)
    unique_link = models.CharField(max_length=255, unique=True, blank=True)
    recruiter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='jobs')

    def save(self, *args, **kwargs):
        if not self.unique_link:
            self.unique_link = generate_unique_link(self)
        super(Job, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class JobApplication(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    candidate = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')
    resume = models.FileField(upload_to='resumes/')
    applied_at = models.DateTimeField(auto_now_add=True)
    experience_summary = models.TextField(blank=True) 
    email_id = models.EmailField(blank=False) 
    contact_no = models.CharField(max_length=15, blank=False)

    def __str__(self):
        return f'{self.candidate} - {self.job.title}'