from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import reverse
from .errors import InsufficientBalance
from django.db import transaction

CLOTHS = "CLOTHS"
DOCUMENTS = "DOCUMENTS"
GROCERY = "GROCERY"
OTHER = "OTHER"

CATEGORY_CHOICES = ((CLOTHS, "Cloths"), (DOCUMENTS, "Documents"),
                    (GROCERY, "Grocery"), (OTHER, "Other"))

# for piority choice field on package model
HIGH = 'HIGH'
MEDIUM = 'MEDIUM'
LOW = 'LOW'
PRIORITY_CHOICES = ((HIGH, 'HIGH'), (MEDIUM, 'MEDIUM'), (LOW, 'LOW'))


class Package(models.Model):

    name = models.CharField(_("name"), max_length=50)
    weight = models.PositiveIntegerField(_("weight"))
    category = models.CharField(
        _("category"), choices=CATEGORY_CHOICES, max_length=50)

    price = models.PositiveIntegerField(_("price"))
    pick_address = models.CharField(_("pick up address"), max_length=50)
    dest_address = models.CharField(_("delivery address"), max_length=50)
    delivered_on = models.DateTimeField(
        _("delivery time"), blank=True, null=True)

    description = models.CharField(_("description"), max_length=250)

    owner = models.ForeignKey("accounts.CustomUser", related_name="item_owner", verbose_name=_(
        "owner"), on_delete=models.CASCADE)
    carrier = models.ForeignKey("accounts.CustomUser", verbose_name=_(
        "carrier"), on_delete=models.DO_NOTHING, null=True, blank=True)  # Else when a Carrier's account goes the Package goes

    security_code = models.CharField(
        _("security code"), max_length=20, null=True, blank=True)
    # Tracker should be OnetoOneField
    tracker = models.OneToOneField("main.Tracker", verbose_name=_(
        "tracker"), null=True, blank=True, on_delete=models.SET_NULL)

    origin = models.CharField(_("package origin city"), max_length=50)
    destination = models.CharField(
        _("package destination city"), max_length=50)
    priority = models.CharField(
        _('Package Priority'), choices=PRIORITY_CHOICES, max_length=50)
    delivery_period = models.PositiveIntegerField(_("delivery period"))
    package_image = models.ImageField(
        _("Package image"), upload_to='package_images/', default='package_images/default.png')
    recievers_first_name = models.CharField(
        _("recievers first name"), max_length=20)
    recievers_last_name = models.CharField(
        _("recievers last name"), max_length=20)
    recievers_phone_number = models.CharField(
        _("recievers phone number"), max_length=20)

    class Meta:
        verbose_name = _("Package")
        verbose_name_plural = _("Packages")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("package_detail", kwargs={"pk": self.pk})


class Tracker(models.Model):

    is_confirmed = models.BooleanField(
        _("is confirmed"), default=False)  # Added False as default state
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


class Wallet(models.Model):
    user = models.OneToOneField(
        to='accounts.CustomUser', on_delete=models.CASCADE, related_name='wallet')
    current_balance = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}\'s wallet'

    @transaction.atomic
    def deposit(self, amount):
        """Deposits a amount to the wallet.
        Also creates a new transaction with the deposit
        amount.
        """
        self.transactions.create(
            amount=amount, running_balance=self.current_balance + amount,  is_credit=True)
        self.current_balance += amount
        self.save()

    @transaction.atomic
    def withdraw(self, amount):
        """Withdraw's a amount from the wallet.
        Also creates a new transaction with the withdraw
        amount.
        Should the withdrawn amount is greater than the
        balance this wallet currently has, it raises an
        :mod:`InsufficientBalance` error. This exception
        inherits from :mod:`django.db.IntegrityError`. So
        that it automatically rolls-back during a
        transaction lifecycle.
        """
        if amount > self.current_balance:
            raise InsufficientBalance('This wallet has insufficient balance.')

        self.transactions.create(
            amount=-amount, running_balance=self.current_balance - amount, is_credit=False)
        self.current_balance -= amount
        self.save()

    @transaction.atomic
    def transfer(self, wallet, value):
        """Transfers an value to another wallet.
        Uses `deposit` and `withdraw` internally.
        """
        self.withdraw(value)
        wallet.deposit(value)


class Transaction(models.Model):
    wallet = models.ForeignKey(
        Wallet, on_delete=models.DO_NOTHING, related_name='transactions')
    amount = models.IntegerField(default=0)
    # current balance of wallet during transaction
    running_balance = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    is_credit = models.BooleanField()
