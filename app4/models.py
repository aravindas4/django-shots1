from django.db import models, transaction


class Blog(models.Model):
    name = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=5)

    def __str__(self):
        return self.name


class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    rating = models.IntegerField(default=5)

    def __str__(self):
        return self.headline

    def some(self):
        cls = self.__class__
        with transaction.atomic():
            instance = cls.objects.select_for_update().get(pk=self.pk)
            instance.status = self.PARSING_STATUS.FAILED
            instance.reason = "Unable to fetch the resume"
            instance.save(update_fields=["status", "updated_at", "reason"])
            return None

    def transact(self, *fields, **field_dict):
        cls = self.__class__
        with transaction.atomic():
            # Locking the object for transaction
            instance = cls.objects.select_for_update().get(pk=self.pk)

            # fields to be updated
            update_fields = fields

            # Set values for fields
            for key, value in field_dict.items():
                setattr(instance, key, value)
                update_fields.append(key)
                # Triggers signal
                instance.save(update_fields=update_fields)

        return instance
