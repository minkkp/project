from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.db import models 

class UserManager(BaseUserManager):    
    use_in_migrations = True    
    def create_user(self, user_id,password,user_area):              
        user = self.model(            
            user_id = user_id,        
            user_area = user_area,
        )        
        user.set_password(password)        
        user.save(using=self._db)        
        return user    
     
    def create_superuser(self,user_id,password):        
        user = self.create_user(            
            user_id = user_id,            
            password = password,
            user_area = '',
        )        
        print(user.user_date)

        user.is_admin = True         
        user.save(using=self._db)    
        return user 
    
class User(AbstractBaseUser):    
    user_date = models.DateTimeField(auto_now_add=True,null=True)    
    user_id = models.CharField(primary_key=True,max_length=15, null=False, blank=False, unique=True)
    # user_pw = AbstractBaseuser에서 기본 제공    
    user_area = models.CharField(primary_key=False,max_length=15, null=True, blank=True, unique=False)

    is_active = models.BooleanField(default=True)    
    is_admin = models.BooleanField(default=False)    
    is_superuser = models.BooleanField(default=False)    
    is_staff = models.BooleanField(default=False)     
    
    objects = UserManager()

    USERNAME_FIELD = 'user_id'    
    REQUIRED_FIELDS = []

    @property
    def is_staff(self):
        return self.is_admin
    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True