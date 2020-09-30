from django.db import IntegrityError


class InsufficientBalance(IntegrityError):
    """Raised when a wallet has insufficient balance for withdrawal.
    We're subclassing from `django.db.IntegrityError`
    so that it is automatically rolled-back during django's
    transaction lifecycle.
    """