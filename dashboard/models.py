from django.db import models

# Create your models here.



class Lession(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return f'{self.name}'



class LessionScore(models.Model):
    lession = models.ForeignKey(to=Lession, on_delete=models.PROTECT)
    score = models.IntegerField(null=False)


    def __str__(self):
        return f'{self.Lession.name} - {self.name}' 



    def avrage(self):
        text = ''

        for lession in Lession.objects.all():
            avg = 0
            sum = 0
            counter = 0
            for scorelession in LessionScore.objects.all():
                if scorelession.lession.id == lession.id:
                    sum += scorelession.score
                    counter += 1
            if counter != 0:    
                avg = sum/counter

            text += str(avg) + ','

        return text

