from django.core.mail import send_mail
from django.template.loader import render_to_string


def RegisterMail(request):
    EmailAddress = request.POST.get('email')
    send_mail(
        "Pepe",
        "Ola toi testeando lollol",
        "pepe@mail.com",
        [EmailAddress],
        fail_silently=False
    )