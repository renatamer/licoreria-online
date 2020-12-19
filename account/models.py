from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class AccountManager(BaseUserManager):
	# def create_user(self, email, username, first_name, last_name, password=None):
	def create_user(self, email, username, password=None):
		if not email:
			raise ValueError('Los usuarios deben tener un email')
		if not username:
			raise ValueError('Los usuarios deben tener un nombre de usuario')
		# if not first_name:
		# 	raise ValueError('Los usuarios deben tener un nombre')
		# if not last_name:
		# 	raise ValueError('Los usuarios deben tener un apellido')

		user = self.model(
			email=self.normalize_email(email),
			username=username,
			# first_name=first_name,
			# last_name=last_name,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	# def create_superuser(self, email, username, first_name, last_name, password):
	def create_superuser(self, email, username, password):
		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
			username=username,
			# first_name=first_name,
			# last_name=last_name,
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user

class Account(AbstractBaseUser):
	email					= models.EmailField(verbose_name="email", max_length=60, unique=True)
	username				= models.CharField(max_length=30, unique=True)
	# first_name				= models.CharField(max_length=30)
	# last_name				= models.CharField(max_length=30)
	date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
	is_admin				= models.BooleanField(default=False)
	is_active				= models.BooleanField(default=True)
	is_staff				= models.BooleanField(default=False)
	is_superuser			= models.BooleanField(default=False)

	USERNAME_FIELD = 'email'
	# REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
	REQUIRED_FIELDS = ['username']

	objects = AccountManager()

	def __str__(self):
		# return self.email + ", " + self.username + ", " + self.first_name
		return self.email + ", " + self.username

	# para revisar permisos, todos los usuarios admin tienen permisos
	def has_perm(self, perm, obj=None):
		return self.is_admin

	# tiene el usuario permiso para ver la app? (SI)
	def has_module_perms(self, app_label):
		return True
