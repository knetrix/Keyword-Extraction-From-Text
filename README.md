## Textrank ve RAKE Algoritması ile Metinlerden Anahtar Kelime Çıkarma Projesi

### Özet

Anahtar kelimeler, doküman içeriğindeki konuyu anlamamızı büyük ölçüde kolaylaştırır. Doküman içeriğinin tamamını okumaya gerek kalmadan doküman hakkında çıkarımlar yapılabilir. Anahtar kelimeler; arama motoru optimizasyonu (SEO) işlemlerinde, yorum ve sosyal medya analizlerinde, dokümanın konusunun bulunması ve daha sonra konuya göre doküman sınıflandırma işlemleri gibi birçok yerde kullanılabilir.

Çalışmanın birinci kısmında doküman üzerinde metin ön işleme işlemleri uygulanmıştır. Metin ön işleme, birbirine bağlı işlemlerden oluşmaktadır. Bu işlemler sırasıyla; metni küçük harflere dönüştürme, metindeki her bir kelimeyi ayırma, kelimelerin türlerini belirleme, kelimelerin kök halini bulma, metindeki etkisiz kelimeleri bulma ve metinden çıkarma, metinden istenen türdeki kelimelerin alınması ve tekrar eden kelimelerin çıkarılmasıdır.

Çalışmanın ikinci kısmında metin ön işleme işlemleri ile elde edilen kelimeler kullanılarak otomatik anahtar kelime çıkarma algoritmaları ile metinden anahtar kelimeler çıkarılmaya çalışılmıştır. Bu çalışmada otomatik anahtar kelime çıkarma algoritmalarından TextRank ve RAKE kullanılmıştır. TextRank algoritması ile kelimelerin değerleri hesaplanmıştır. RAKE algoritması ile metin, dokümandaki etkisiz kelimelere göre kelime gruplarına ayrılmıştır. Kelime gruplarının değerini bulabilmek için TextRank algoritması ile hesaplanan kelime değerleri kullanılmıştır. Son olarak kelime gruplarının değerleri büyükten küçüğe sıralanarak nihai anahtar kelimeler bulunmuştur.

Çalışma İngilizce ve Türkçe dokümanları desteklemektedir. İngilizce dokümanlarda TextRank ve RAKE algoritması birlikte kullanılmıştır. Bu nedenle anahtar kelimelerde birden fazla kelime bulunabilmektedir. Türkçe dokümanlarda ise sadece TextRank algoritması kullanılmıştır. Bunun nedeni RAKE algoritmasının Türkçe dokümanlarda iyi performans vermemesidir.

Çalışmada işlemlerin görselleştirilmesi amacıyla arayüz geliştirilmiştir. Arayüz üzerinden dil seçimi yapıldıktan sonra gerekli formatta doküman dosyası verildiğinde, bulunan anahtar kelimeler sıralanmış şekilde arayüzde gösterilmektedir. Ayrıca sonuçlar arayüz aracılığı ile veritabanına kayıt edilebilmekte ve veritabanı, arayüz üzerinden gerekli butona basılarak web tarayıcısı aracılığı ile görüntülenebilmektedir.


### Kullanım
Python **Python 3.8.0** veya üstü gerekiyor.

1. Repoyu ```git clone``` komutunu kullanarak indirin.
2. İndirdiğiniz proje klasöründe CLI açın.
3. pipenv yoksa, onu yüklemeniz gerekir (Komut: ```pip install pipenv```).
4. ```python -m pipenv install--python 3.8.0``` (Başka bir Python sürümü kullanıyorsanız buraya onu yazın)
5. ```pipenv shell```
6. ```python main.py```

**Not:** Program ilk çalıştırıldığında yaklaşık 1,2 GB indirecektir. Bu tek seferlik bir işlemdir.

### Örnek Metinler ve Anahtar Kelimeler

#### Metin 1

Attorneys general of 44 US states and territories told Facebook CEO Mark Zuckerberg to ditch plans to create a version of Instagram for children. They wrote a letter stating social media is detrimental to children “who are not equipped to navigate the challenges of having a social media account. ” They also said that Facebook has not protected children in the past, such as when they created a version of Facebook Messenger for children. They described that children were able to bypass the restrictions to join group chats with strangers who were not approved by their parents. Facebook responded it was exploring the idea of Instagram for children, it would protect their safety and privacy, and it would not show advertising.

Anahtar Kelimeler

1. facebook ceo mark zuckerberg 
2. facebook messenger 
3. social media account
4. child



##### Metin 2

Managers of the best football clubs in Europe have a plan. They want to make a European Super League. The best and biggest teams will be in the new league. The idea starts more than 30 years ago. The clubs want to start the league in 2021. Many people worry that it will change the world of football. 6 British teams sign the deal. Some of these teams are Arsenal, Chelsea, and Liverpool. 6 other teams from Spain and Italy sign, too. Some are Real Madrid, Barcelona, and Juventus. Then football fans get very angry last week. They do not agree with the new league. Some players from the best teams are also not happy. The British prime minister wants to make a new law. This law will make it impossible to make the new league.

Anahtar Kelimeler

1. best football club
2. best team
3. new league
4. british team 
5. biggest team
6. new law
7. british prime minister
8. european super league



#### Metin 3

A Black Hawk is a helicopter. Soldiers use it. Last week, the helicopter flies without pilots. It happens at Fort Campbell, US. There are two flights. One flight is 30 minutes long. The helicopter flies through a city. It is not a real city. A computer makes it. Then, the helicopter lands. The helicopter uses special technology. The technology makes it possible to fly without a pilot. A computer controls it. The technology is very good for pilots. The helicopter can fly at night. It can fly when the weather is bad. Pilots can do other things.

Aanahtar Kelimeler

1. helicopter
2. pilot
3. real city
4. special technology
5. Fort Campbell
6. Black Hawk
7. computer


[Daha Fazla Bilgi için Blog Sayfama Bakabilirsiniz.](https://www.networkous.com/2022/05/textrank-rake-algoritmasi-metinden-anahtar-kelime-cikarma.html)
