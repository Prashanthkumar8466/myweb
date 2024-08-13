from django.core.mail.backends.smtp import EmailBackend

def get_email_backend():
    from Portfolio.models import email_host
    config = email_host.objects.first()
    if config:
        return EmailBackend(
            host=config.host,
            port=config.port,
            username=config.user,
            password=config.password,
        )
    return None
