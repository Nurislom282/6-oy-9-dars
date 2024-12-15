from django.db import models
from django.core.validators import FileExtensionValidator

class Turlar(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Gullar turinikiriting")


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "GulTuri"
        verbose_name_plural = "GulTurlari"


class Gul(models.Model):
    name = models.CharField(max_length=175,verbose_name="Gul nomi")
    info = models.TextField(null=True,blank=True,verbose_name='Gul Haqida malumot')
    photo = models.ImageField(upload_to='gul/photos/', blank=True, null=True, verbose_name="Gul Rasmi")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan vaqti")
    turi = models.ForeignKey(Turlar,on_delete=models.CASCADE)
    published = models.BooleanField(default=True, verbose_name="Saytga chiqarish",
                                    help_text="Agar galochka qo'ysangiz sayta chiqaradi!!!")
    video = models.FileField(upload_to="post/videos/", validators=[
        FileExtensionValidator(['mp4', 'avi'], message="Faqat mp4 va avi formatidagilarni kiritolasiz!")
    ], null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Gul'
        verbose_name_plural = 'Gullar'
        ordering = ['-created', '-pk']