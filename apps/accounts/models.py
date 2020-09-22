from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name',
                       'username',  'phone_number', 'address']

    def __str__(self):
        return self.username


# moved user verification model from main to account cause it is concerned with the account
class UserVerification(models.Model):

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    NIN = models.CharField(_("National Identification Number"), max_length=11)
    BVN = models.CharField(max_length=11)
    upload_id = models.ImageField(
        _("upload id"), upload_to='ids/')
    bank_name = models.CharField(_("bank name"), max_length=50)
    bank_account_number = models.CharField(
        _("bank account number"), max_length=10)

    class Meta:
        verbose_name = _("user Verification")
        verbose_name_plural = _("user Verifications")

    # def __str__(self):
    #     return self.name

    def get_absolute_url(self):
        # Edited according to the new url config
        return reverse("users-verify", kwargs={"pk": self.pk})
