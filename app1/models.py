from django.db import models


class Account(models.Model):
    account_number = models.CharField(max_length=255)
    approved_amount = models.PositiveIntegerField(default=0)
    reason = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.account_number


class LoanApplication(models.Model):

    class Status(models.TextChoices):
        SUBMITTED = 'SUBMITTED', 'Submitted',
        REJECTED = 'REJECTED', 'Rejected'
        APPROVED = 'APPROVED', 'Approved'

    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=255, choices=Status.choices, default=Status.SUBMITTED)

    def __str__(self):
        return str(self.account)
