# models.pyの理解5

※わかりやすさのために、厳密には正しくない表現・説明が含まれてるかもしれません。  
※参考としてるリンクは脱線しがちなので余力があれば読むという形で大丈夫です。

## 理解すると良いポイント

### フィールドの使い方を知る

これまでの説明で、モデルに対する理解がかなり深まったのではないでしょうか。  
すると、実際にモデルを作成するうえで、Fieldに対する理解が大事であることに気づくと思います。  
modelsのFieldには、CharFiledであったり、DateFieldであったり、ImageFieldであったり、いろいろなものがこれまでに登場したと思います。  
各フィールドにどんなFieldを選択肢し、Fieldの()の部分に、どのような指定をすれば良いかが開発で大事になるのは明らかでしょう。

今までよく見たコード例で振り返ってみましょう。

```python
# コード例5-1

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
```

例えば、**CharFieldは、とても良く使われるFieldですが、max_lengthというものを指定する必要があります。**  
CharFieldは文字を扱うFieldで、max_lengthは、その最大文字数を指定しています。  
例5-1でいうと、タイトルは200文字までということですね。  

なぜ指定しないといけないかは、データ型のマッピングという難しい話になるので割愛する(それを知るよりもっと先に知るべきことがある！)のだけど、**大事なのはFiledごとに使い方があることを意識することです。**

(豆知識)max_lengthなどのFiledごとに指定する引数を、フィールドオプションをいいます。全く覚える必要はないです。会話するときに便利かなで、名称なんて知らなくてもコードはかけます。

実用的な、よく使われるFieldは、コード例がネットに落ちているので、探してみると良いでしょう。  
公式ドキュメントにも、なにか良い情報が落ちているかもしれません。

[公式ドキュメント](https://docs.djangoproject.com/ja/5.1/ref/models/fields/#django.db.models.CharField)