class Entrepreneur(models.Model):
      name = models.CharField(max_length=30)
      age = models.IntegerField()
      company_name = models.CharField(max_length=50)
      description = modles.TextField()

      class Meta:
           verbose_name_plural= "entrepreneurs"

      def __str__(self):
          return f"{self.name} is {self.age} years old and he owns {self.conpany_name}"


entre_deatils = Entrepreneur.objects.get(name = "python")

entre_details.name= "Cplusplus"
entre_details.save()


harland = entre_details.objects.all()
harland.objects.filter(age=17).delete()
