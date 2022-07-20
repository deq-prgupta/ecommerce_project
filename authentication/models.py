from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.contrib.auth.base_user import BaseUserManager,AbstractBaseUser
# Create your models here.

# class ExtendUser(models.Model):
#     TYPE = (
#         ('Admin'),('Shopuser'),('customer')
#     )
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     date_of_birth = models.DateField(verbose_name="DOB")
#     gender = models.CharField(max_length=10)
#     address = models.CharField(max_length=100)
#     user_type = models.CharField(choices=TYPE)
#     creation_date = models.DateField(default=date.today)


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username,phno , password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')
        if not phno:
            raise ValueError('Users must have a contact number')
        if not password:
            raise ValueError('Password cannot be Empty')
        user = self.model(
		email=self.normalize_email(email),
		username=username,
		phno = phno,
		)
        user.set_password(password)
        user.save(using=self._db)
        return user
        
    def create_superuser(self, email,phno, username, password):
        user = self.create_user(
			email=self.normalize_email(email),
			username=username,
			password=password,
			phno = phno,
		)
        user.user_type = 'Admin'
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
	

class Accounts(AbstractBaseUser):
    TYPE = (
        ('Admin','Admin'),('Shopuser','Shopuser'),('Customer','Customer')
    )
    email = models.EmailField(verbose_name="email",max_length=100,unique=True,primary_key=True)
    username = models.CharField(max_length=70)
    phno = models.CharField(max_length=20)
    date_joined	= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login	= models.DateTimeField(verbose_name='last login', auto_now=True)
    date_of_birth = models.DateField(verbose_name="DOB",default=date.today)
    gender = models.CharField(max_length=10,blank=True)
    address = models.CharField(max_length=100,blank=True)
    user_type = models.CharField(max_length=70 ,choices=TYPE,default='Customer')
    creation_date = models.DateField(default=date.today)
    is_active				= models.BooleanField(default=True)
    is_staff				= models.BooleanField(default=False)
    is_admin				= models.BooleanField(default=False)
    is_superuser			= models.BooleanField(default=False)



    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','phno']
    EMAIL_FIELD='email'
    
    objects = MyAccountManager()
    
    def __str__(self):
        return self.email
        
    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_superuser

	# Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True

