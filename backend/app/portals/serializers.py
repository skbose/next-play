from rest_framework import serializers
from .models import Job, JobApplication

class JobSerializer(serializers.ModelSerializer):
    attachment_url = serializers.SerializerMethodField()
    unique_link = serializers.CharField(read_only=True)

    class Meta:
        model = Job
        fields = ['id', 'title', 'description', 'attachment', 'attachment_url', 'unique_link', 'posted_at']

    def get_attachment_url(self, obj):
        request = self.context.get('request')
        if obj.attachment:
            return request.build_absolute_uri(obj.attachment.url)
        return None


class JobApplicationSerializer(serializers.ModelSerializer):
    resume_url = serializers.SerializerMethodField()
    candidate = serializers.ReadOnlyField(source='candidate.username')  # To display the username of the candidate

    class Meta:
        model = JobApplication
        fields = ['id', 'job', 'candidate', 'resume', 'resume_url', 'applied_at','experience_summary', 'email_id', 'contact_no' ]

    def get_resume_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.resume.url)
