# models.pyの理解3

※わかりやすさのために、厳密には正しくない表現・説明が含まれてるかもしれません。  
※参考としてるリンクは脱線しがちなので余力があれば読むという形で大丈夫です。

## 理解すると良いポイント

### フィールドとはなにか

　コード例2-3で、モデルの中身はフィールド名と、それに対応するフィールドの型や性質を書くと説明しました。
といっても、あまりイメージがつかないと思うので、順を追って説明します。
コード例3-1として**再掲**しておきますね。

```python
# コード例3-1

from django.db import models

class モデル名(models.Model):
    フィールド名 = 対応するフィールドの型や性質を指定
    フィールド名 = 対応するフィールドの型や性質を指定
    ・
    ・
    ・
    フィールド名 = 対応するフィールドの型や性質を指定
```

まず、**データには「型」という概念が存在します。**  
pythonだと、データにはint型、float 型、str 型、bool 型と色々と種類があったと思います。  
扱いたいデータが数値なのか、文字なのか、あるいはtrueかfalseで表される真偽値なのか、データの種類はとても重要なことなのです。

参考:[pythonのデータ型](https://kino-code.com/python_introductory-and-applied05/)  
→pythonのデータ型について解説しています。でも、今はそれぞれのデータ型について、詳しく理解するのは後回しでよいです。

djangoでは、そのデータの型をwebアプリの開発に適したようにフィールドという形で進化させています。    
例えば、メールアドレスをデータとして扱いたいときに、EmailFieldというフィールドを使うと、メールアドレス用としてデータを扱うことができます。  
このフィールドを使うと、例えばメールアドレスとして登録したいデータに、@(アットマーク)が含まれていなかったときとかに不正なデータとして弾くことができます。  
すごいでしょ!!  
djangoが、pythonのフレームワーク(FW)で、効率的に開発ができるようにしているというのはこういうところにも現れているんです。  
**(ちなみに、メールアドレスは和製英語で海外だと通じないです。emailといいます。これは変数の命名において大事なので、覚えた方が良いです。)**

```python
# コード例3-2

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
```

これも最初に上げたコードの再掲なのですが、
例えばtitleやauthorというフィールドは、CharFieldを使ったものとして定義し、
published_dateというフィールドには、DateFieldを指定し、priceというフィールドにはDecimalFiledというものを

どんなFiledがあるかは、以下の記事などがおすすめですが、当然使用頻度には差が
あり、よく使うやつから覚えていけばよいです。

参考：[フィールドの種類](https://qiita.com/shun_sakamoto/items/9b3c8f0575d549d7b77b)