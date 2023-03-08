from django.db import models


# Create your models here.


class Bolimlar(models.Model):
    nomi = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nomi}"



    class Meta:
        verbose_name = 'Bolim'
        verbose_name_plural = 'Bolim'

    


class Ish(models.Model):
    bolim = models.ForeignKey(Bolimlar, on_delete=models.CASCADE)
    ism = models.CharField(max_length=100)
    familiya = models.CharField(max_length=100)
    yosh = models.DateField(help_text='Yil | Oy | Kun')
    manzil = models.CharField(max_length=100)
    ostasini_ismi = models.CharField(max_length=100, help_text='Otasini ismi kiritilsin ...')
    onasini_ismi = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.ism} {self.familiya} {self.manzil} {self.ostasini_ismi} {self.onasini_ismi}"    



    class Meta:
        verbose_name = 'Ishchi'
        verbose_name_plural = 'Ishchilar'



