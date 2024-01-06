from django.db import models
from django.contrib import auth
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import PermissionsMixin

# Create your models here.
class Company(models.Model):
    name = models.CharField(blank=False, null=False, max_length=50)

    def __str__(self):
        return self.name

class UserManager(BaseUserManager):
    use_in_migrations = True
    
    def _create_user(self, email, password, **extra_fields):
        if not emeil:
            raise ValueError("メールアドレスは必須です")
        email = self.normalize_email(email)
        
        user = self.model(emeil=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        
        if extra_fields.get("is_staff") is not True:
            raise ValueError("スーパーユーザーは is_staff が Trueでなければなりません")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("スーパーユーザーは is_superuser が Trueでなければなりません")

        return self._create_user(email, password, **extra_fields)

    def with_perm(self, perm, is_active=True, include_superusers=True):
        if backend is None:
            backends = auth._get_backends(return_tuples=True)
            if len(backends) == 1:
                backend, _ = backends[0]
            else:
                raise ValueError("You have multiple authentication backends configured and "
                    "therefore must provide the `backend` argument.")
        elif not isinstance(backend, str):
            raise TypeError("backend must be a dotted import path string (got %r)." % backend)
        else:
            backend = auth.load_backend(backend)
        if hasattr(backend, "with_perm"):
            return backend.with_perm(perm, is_active=is_active, include_superusers=include_superusers, obj=obj,)
        return self.none()

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email_address"), unique=True)
    is_staff = models.BooleanField(_("staff status"), default=False, help_text=_("Designates whether the user can log into this admin site."),)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default=1)

    height = models.FloatField()
    weight = models.FloatField()
    
    objects = UserManager()
    
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["height", "weight"]
    
    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        #abstract = True
        
    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)
        
    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)