from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

# Create your models here.
class Student(models.Model):

    first_name = models.CharField(_("First Name"), max_length=50)
    last_name = models.CharField(_("Last Name"), max_length=50)
    username = models.SlugField(blank=True, null=True)
    cod_student = models.IntegerField(_(""), unique=True)

    aprooved = models.BooleanField(_(""), default=False)
    average_score = models.FloatField(
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = _("Student")
        verbose_name_plural = _("Students")

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse("student_detail", kwargs={"pk": self.pk})



class Lab(models.Model):
    lab_name = models.CharField(_("Lab name"), max_length=150)
    lab_seats = models.IntegerField(_(""))
    students = models.ManyToManyField("lab.Student", verbose_name=_("students_lab"))

    

    class Meta:
        verbose_name = _("Lab")
        verbose_name_plural = _("Labs")

    def __str__(self):
        return self.lab_name

    def get_absolute_url(self):
        return reverse("lab_detail", kwargs={"pk": self.pk})

