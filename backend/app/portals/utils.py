import hashlib
from datetime import datetime
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import get_user_model

def generate_unique_link(job):
    unique_string = f"{job.title}{datetime.now().timestamp()}"
    return hashlib.md5(unique_string.encode()).hexdigest()


User = get_user_model()

def get_candidate_emails():
    """
    Retrieves the email addresses of all candidates from the database.
    """
    return User.objects.filter(user_type='candidate').values_list('email', flat=True)

def construct_email_content(job, recruiter):
    """
    Constructs the email subject and body for the job posting notification.
    
    :param job: Job instance
    :param recruiter: Recruiter (User instance)
    :return: subject, message
    """
    subject = f'New Job Posted: {job.title}'
    full_link = f"{settings.BASE_URL}{job.unique_link}"
    message = f'A new job "{job.title}" has been posted by {recruiter.name}.\n\n' \
              f'Job Description: {job.description}\n\n' \
              f'You can apply using this link: {full_link}'
    
    return subject, message

def send_job_notification_to_candidates(job, recruiter):
    """
    Sends a job notification email to all candidates.

    :param job: The Job instance
    :param recruiter: The recruiter (User instance)
    """
    # Get all candidate email addresses
    candidate_emails = get_candidate_emails()

    if not candidate_emails:
        return  # No candidates to notify

    # Construct the email content
    subject, message = construct_email_content(job, recruiter)

    # Send email using Django's send_mail function
    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=candidate_emails,
            fail_silently=False,  # Raise an exception on failure
            #headers={'Reply-To': recruiter_email},
        )
    except Exception as e:
    # Log or handle the error
        print(f"Error sending email: {e}")
