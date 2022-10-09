from django.db import models

# Create your models here.
class Clients(models.Model):
    POSITIONTYPES = (
        ("fulltime","full time"),
        ("more20","more than 20 hours/week"),
        ("less20","less than 20 hours/week"),
    )
    name = models.CharField(max_length=255, verbose_name="Company Name *")
    email = models.EmailField(verbose_name="Email *")
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name="Job Description / Position Link",
        help_text='Feel free to leave it for now, we will get access to know your company')
    position = models.CharField(max_length=32, choices=POSITIONTYPES, verbose_name='Position *')
    application_date = models.DateTimeField(auto_now=True,verbose_name="Basvuru Tarihi")

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Sirketler listesi'
        verbose_name = 'Sirket'

class Skills(models.Model):
    skills = models.CharField(max_length=255, null=True, blank=True, verbose_name='skills')

    def __str__(self):
        return self.skills



class Developers(models.Model):
    ENGLISHLEVEL = (
        ("advanced","advanced"),
        ("good","good"),
        ("intermediate","intermediate"),
        ("elementary","elementary"),
        ("beginner","beginner"),
    )

    SPECIALIZATIONLEVEL = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5-7", "5-7"),
        ("7-10", "7-10"),
        ("10+", "10+"),
    )
    SPECIALIZATION = (
        ("backend", "backend developer"),
        ("frontend", "frontend"),
        ("fullstack", "fullstack"),
        ("software", "software engineer"),
        ("datascientist", "datascientist"),
        ("dataengineer", "dataengineer"),
        ("dataanalyst", "dataanalyst"),
        ("devops", "devops"),
        ("gamedesigner", "gamedesigner"),
        ("designer", "designer"),
        ("qa", "qa"),
        ("other", "other"),
    )
    name = models.CharField(max_length=255, verbose_name="Developer Adi")
    email = models.EmailField(verbose_name="email")
    country = models.CharField(max_length=64, verbose_name="Ulke Adi")
    english_level = models.CharField(choices=ENGLISHLEVEL, max_length=64, verbose_name="Ingilizce seviyesi")
    specialization = models.CharField(choices=SPECIALIZATION, max_length=64, verbose_name="Posizyon")
    description = models.TextField(null=True, blank=True, verbose_name="aciklama")
    experience = models.CharField(choices=SPECIALIZATIONLEVEL, max_length=64, verbose_name="tecrube")
    skills = models.ManyToManyField(
        Skills, blank=True, related_name='developer', verbose_name='Maharetler'
    )
    application_date = models.DateTimeField(auto_now=True, verbose_name="Basvuru Tarihi")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Developer listesi'
        verbose_name = 'Developer'