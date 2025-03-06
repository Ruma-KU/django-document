Djangoの `AbstractUser` を継承したカスタムユーザーモデルの例を示します。  
ここでは、**プロフィール画像 (`profile_image`) と自己紹介 (`bio`) を追加** しています。

---

### **カスタムユーザーモデル**
```python
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.username
```

---

### **解説**
1. **`AbstractUser` を継承**  
   - Djangoのデフォルトの `User` モデルの基本的な機能（`username`, `email`, `password` など）を引き継ぎつつ、カスタマイズが可能。
   
2. **追加フィールド**
   - `profile_image` → プロフィール画像（`upload_to='profile_images/'` で画像の保存先を指定）
   - `bio` → 自己紹介（500文字まで）

3. **`__str__` メソッド**
   - `print(user)` のようにすると `username` を表示。

---

### **このモデルを使うための設定**
`settings.py` に以下を追加：
```python
AUTH_USER_MODEL = 'yourapp.CustomUser'  # yourapp を実際のアプリ名に変更
```

---

これで `CustomUser` を使ったユーザー認証が可能になります！ 🎉