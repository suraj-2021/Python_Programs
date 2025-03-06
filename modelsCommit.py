class MyModelForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = '__all__'

    def save(self, commit=True):
        instance = super().save(commit=False)
        if instance.pk:  # Check if the instance already exists
            old_instance = MyModel.objects.get(pk=instance.pk)
            if old_instance.field1 != instance.field1:
                log_change(f"Field1 changed from {old_instance.field1} to {instance.field1}")
        if commit:
            instance.save()
        return instance
