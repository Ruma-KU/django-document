# models.pyの理解4

※わかりやすさのために、厳密には正しくない表現・説明が含まれてるかもしれません。  
※参考としてるリンクは脱線しがちなので余力があれば読むという形で大丈夫です。

## 理解すると良いポイント

### AbstractUserについての基礎

前回までの記事で、モデルの基本的な書き方はわかったと思います。  
しかし、モデルの中でも、ユーザーに関するモデルは、どんあアプリでも使うものです。  
アカウントの管理に関わってくるので、超重要です。  
なので、djangoではより効率的にかけるようにdjangoはさらなる工夫をしてくれています。  


その一つが、**AbstractUser**というモデルです。  
通常、モデルは、models.Modelを継承することによって作成しますが、
ユーザーモデルに関しては、AbstractUserを継承することでより楽に書くことができます。

簡単なコード例は、こんな感じです。

```python
# コード例4-1

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True)
```

このコード例では、ユーザーについて扱っているモデルなのに、profile_image(プロフィール画像)とbio(自己紹介文)というフィールドしか定義されていないように見えます。  
いやいや、もっとユーザー情報には大事なことがありますよね。  
username(名前)やemail(メールアドレス)やpassword(パスワード)などなど。  
実は、これらのフィールドは、**AbstractUserを継承した時点で既に定義されているのです。**  

つまり、ユーザー情報について、ユーザーネームやメールアドレスなど、どのアプリでも使うようにな情報は個々の開発者がわざわざフィールドを定義しなくても、コードを書かなくてもいいようになっているということです。  
労力の削減と開発効率の向上です。  
これについては、pythonのクラスの継承とはなにかを復習してみてください。

AbstractUserがどんなフィールドをあらかじめ定義してくれているかは、ソースコードを確認するとよいです。

参考:[AbstractUser](https://github.com/django/django/blob/main/django/contrib/auth/models.py)

行数が多くて、探すのが大変なので、一応この記事の末尾に主要部だけ貼りますね。

確かに、usernameやemailを定義してくれてる。これを継承すれば、自分はusernameやemailについて書かなくてもよくなっている。  
これが継承のすごさです。  
クラスの便利さが感じられてくるでしょうか。  

注意深い人は、あれ、パスワードが定義されてないじゃんと気づくかもしれません。   
ここからは発展的な話なのですが、AbstractUserはAbstractBaseUserを継承していることがわかります。  
このAbstractBaseUserの方に、パスワードは定義されているんですね。  
こういうのを、**多重継承**といいます。  
AbstractBaseUserの簡単なコードも貼っておきますね。  
また、AbstractBaseUser自身は通常のモデルと同じように、models.Modelを継承しているのもわかります。  
AbstractUserも、子クラスになっているから特殊なだけで、元は通常のモデルと同じということがわかりますね。



```python
# コード例4-2 AbstractUser(主要部)

class AbstractUser(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    Username and password are required. Other fields are optional.
    """

    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    email = models.EmailField(_("email address"), blank=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    """
    以下省略
    ・
    ・
    ・
    """
```

```python
# コード例4-3 AbstractBaseUser(主要部)

class AbstractBaseUser(models.Model):
    password = models.CharField(_("password"), max_length=128)
    last_login = models.DateTimeField(_("last login"), blank=True, null=True)

```