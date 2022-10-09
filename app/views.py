from django.shortcuts import render
from django.core.mail import EmailMessage
from app.forms import ClientsCreateForm
from app.models import Developers, Skills
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def applier_email(request, mail):
    try:
        subject = 'Thank you for registering to our site'
        message = 'Congratulations, we received your apply; Our team will contact you within 24 hours.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [mail]
        send_mail( subject, message, email_from, recipient_list )
        return True
    except:
        return False

def our_email(request, mail, file= None, type= None):
    try:
        subject = ''
        message = ''
        if type == 'company':
            subject = 'Yeni sirket Kaydi'
            message = "New Company Applier :-D  email: {mail}, Company Name: {name}," \
                      "Description: {description}, Position: {position}".format(mail=mail,
                                                        name=request.POST.get("name"),
                                                        description =request.POST.get("description"),
                                                        position=request.POST.get("position"))

        if type == 'developer':
            name = request.POST.get('name')
            dev_mail = request.POST.get('email')
            country = request.POST.get('country')
            english = request.POST.get('english')
            specialization = request.POST.get('specialization')
            experience = request.POST.get('experience')
            note = request.POST.get('note')
            tags = request.POST.get('tags')

            subject = 'Yeni Developer Kaydi'

            message = 'New Developer Apply :-D, name:{name}, email: {dev_mail}, ' \
                      'country Name: {country},  ' \
                      'English Level: {english},  ' \
                      'Specializations: {specialization},  ' \
                      'experience: {experience} years,  ' \
                      'note: {note},  ' \
                      'tags: {tags}'.format(name =name, dev_mail=dev_mail, country=country, english=english,
                                            specialization=specialization, experience=experience, note=note,tags=tags)


        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['berkansems@gmail.com', 'olenasems88@gmail.com', 'talenterminal@gmail.com']
        if file:
            new_mail = EmailMessage(subject, message, settings.EMAIL_HOST_USER, recipient_list)
            new_mail.attach(file.name, file.read(), file.content_type)
            new_mail.send()
        else:
            send_mail( subject, message, email_from, recipient_list )
        return True
    except:
        return False


def home(request):

    if request.method == "POST":

        subject = 'Yeni Istek'
        direct_mail = request.POST.get('direct_mail')
        applier_email(request, mail=direct_mail)
        message = 'Dogrudan iletisim kurmak istiyor: {direct_mail}'.format(direct_mail=direct_mail)
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['berkansems@gmail.com', 'olenasems88@gmail.com', 'talenterminal@gmail.com']
        messages.success(request, 'Congratulations, we receive your application and will contact you within 24 hours!')
        send_mail(subject, message, email_from, recipient_list)

    return render(request, 'index.html')

def developers(request):
    return render(request, 'index.html')

def company_apply(request):

    company_form = ClientsCreateForm()
    if request.method == 'POST':

        form = ClientsCreateForm(request.POST)
        if form.is_valid():
            form.save()
            applier_email(request, mail=request.POST.get('email'))
            mail_sent_to_us = our_email(request, mail=request.POST.get('email'), type='company' )
            if mail_sent_to_us:
                messages.success(request, 'Congratulations, we receive your application and will contact you within 24 hours!')
            else:
                messages.success(request, 'An error occurred, you can directly send an email to info@talenterminal.com')
        else:
            messages.success(request, 'An error occurred, you can directly send an email to info@talenterminal.com')
    return render(request, 'company_apply.html', context={'company_form':company_form})


def dev_apply(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        dev_mail = request.POST.get('email')
        country = request.POST.get('country')
        english = request.POST.get('english')
        specialization = request.POST.get('specialization')
        experience = request.POST.get('experience')
        note = request.POST.get('note')
        tags = request.POST.get('tags')
        developer = Developers.objects.create(
            name=name,
            email=dev_mail,
            country=country,
            english_level=english,
            specialization=specialization,
            description=note,
            experience=experience,
        )
        tags_list = tags.split(',')
        for item in tags_list:
            skill_lower = item.lower()
            try:
                skill = Skills.objects.get(skills=skill_lower)
            except:
                skill = Skills.objects.create(skills=skill_lower)
            developer.skills.add(skill)
        applier_email(request, mail=dev_mail)
        mail_to_us = our_email(request, mail=dev_mail, file=request.FILES.get('cv'), type= 'developer')
        if mail_to_us:
            messages.success(request, 'Congratulations, we receive your application and will contact you within 24 hours!')
        else:
            messages.success(request, 'An error occurred, you can directly send an email to info@talenterminal.com')


    return render(request, 'developers_apply.html')