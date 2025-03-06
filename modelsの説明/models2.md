# models.pyの理解2

※わかりやすさのために、厳密には正しくない表現・説明が含まれてるかもしれません。  
※参考としてるリンクは脱線しがちなので余力があれば読むという形で大丈夫です。

## 理解すると良いポイント

### models.pyの書き方

例えば、本に関するデータベース(DB)を作成するために以下のように書きます。

```python
# コード例2-1

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
```

見ての通り、**Pythonのクラス**を用いるのですが、このようにDB設計用に書かれたクラスを**モデル**といいます。

Pythonで見たことあるクラスのコード例と比べて違和感があるかもしれないです。
注目してほしいことは、**このクラスがmodels.Modelを継承していること**です。

djangoでモデルを作成するときは、基本的にModelという親クラスを継承して書きます。  
[ソースコード](https://github.com/django/django/blob/main/django/db/models/base.py)の460行目にModelという名前のクラスが書かれているのがわかると思います。

今は、そのような内部のことはあまり意識せず、
```python
# コード例2-2

from django.db import models

class モデル名(models.Model):
    """
    モデルの中身
    """
```
というようにコードを書けばいいと理解してください。  
１行目は、Modelという親クラスが外部のファイルに書かれているので、それをmodels.pyで使えるようにするためのimport文です。  
importがイマイチ分からなかったら、一旦おまじないようなものだと思ってください。  
(というか、ありがたいことにmodels.pyにはデフォルトで書かれています)

このような形でModelという親クラスを継承していることで、最初にあげたコード例2-1のような書き方でモデルを作成することが可能になっています。

次は、さきほどのコード例2-2で濁したモデルの中身について説明します。

コード例2-1を見てもらえばよいのですが、基本的には
```python
# コード例2-3

from django.db import models

class モデル名(models.Model):
    カラム名 = 対応するフィールド
    カラム名 = 対応するフィールド
    ・
    ・
    ・
    カラム名 = 対応するフィールド
```

という形式で書いていきます。
フィールドについての説明は、次回に回しますが、コード例2-1を見てください。
例えば、titleやauthorというカラムには、CharFieldというフィールドが対応していて、
published_dateというカラムには、DateFieldというフィールドが対応していて、
priceというフィールドには、DecimalFieldというフィールドが対応していると、とりあえずおぼてみてください。