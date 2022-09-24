from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError("사용자 계정을 만들어주세요")
        user = self.model(
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
        
    def create_superuser(self, username, password=None):
        user = self.create_user(
            username=username,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField("사용자 계정", max_length=30, unique=True)
    password = models.CharField("비밀번호", max_length=150)
    fullname = models.CharField("사용자 이름", max_length=20)
    ip_address = models.GenericIPAddressField(null=True)
    
    join_date = models.DateTimeField("가입일자", auto_now_add=True)

    # 계정 비활성화 여부
    is_active = models.BooleanField(default=True)
    # admin 제어
    is_admin = models.BooleanField(default=False)
    
    # id로 지정할 필드
    USERNAME_FIELD = "username"
    
    REQUIRED_FIELDS = []
    
    # UserModel Custom
    objects = UserManager()
    
    def __str__(self):
        return self.username
    
    # 특정 테이블의 crud 권한을 설정
    def has_perm(self, perm, obj=None):
        return True
    
    # 특정 app에 접근 가능 여부를 설정
    def has_module_perms(self, app_label):
        return True
    
    # admin 권한 설정
    @property
    def is_staff(self):
        return self.is_admin