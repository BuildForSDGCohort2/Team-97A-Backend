from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import reverse

CLOTHS = "CLOTHS"
DOCUMENTS = "DOCUMENTS"
GROCERY = "GROCERY"
OTHER = "OTHER"

CATEGORY_CHOICES = ((CLOTHS, "Cloths"), (DOCUMENTS, "Documents"),
                    (GROCERY, "Grocery"), (OTHER, "Other"))


class Package(models.Model):

    name = models.CharField(_("name"), max_length=50)
    weight = models.PositiveIntegerField(_("weight"))
    category = models.CharField(
        _("category"), choices=CATEGORY_CHOICES, max_length=50)

    price = models.PositiveIntegerField(_("price"))
    pick_location = models.CharField(_("pick up location"), max_length=50)
    dest_location = models.CharField(_("delivery location"), max_length=50)
    delivered_on = models.DateTimeField(_("delivery time"))
    description = models.CharField(_("description"), max_length=250)

    owner = models.ForeignKey("accounts.CustomUser", related_name="item_owner", verbose_name=_(
        "owner"), on_delete=models.CASCADE)
    carrier = models.ForeignKey("accounts.CustomUser", verbose_name=_(
        "carrier"), on_delete=models.DO_NOTHING)  # Else when a Carrier's account goes the Package goes

    security_code = models.CharField(_("security code"), max_length=20)
    # Tracker should be OnetoOneField
    tracker = models.OneToOneField("main.Tracker", verbose_name=_(
        "tracker"), null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = _("Package")
        verbose_name_plural = _("Packages")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("package_detail", kwargs={"pk": self.pk})


class Tracker(models.Model):

    is_uploaded = models.BooleanField(
        _("is uploaded"), default=False)  # Added False as default state
    in_transit = models.BooleanField(_("in transit"), default=False)
    is_delivered = models.BooleanField(_("is delivered"), default=False)

    class Meta:
        verbose_name = _("Tracker")
        verbose_name_plural = _("Trackers")

# commenting this cause there is no name in model
    # def __str__(self):
    #     return self.name

    def get_absolute_url(self):
        return reverse("tracker_detail", kwargs={"pk": self.pk})
