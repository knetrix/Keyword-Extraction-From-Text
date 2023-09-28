<p align="center">
    <img src="/gui.jpg">
</p>

<p align="center">
    <img src="/gui-result.jpg">
</p>

<p align="center">
    <img src="/database.jpg">
</p>

# English
## Keyword Extraction Project from Texts with Textrank and RAKE Algorithm

Keywords greatly facilitate our understanding of the topic matter in the document content. Inferences can be made about the document without having to read the entire content of the document. Keywords can be used in many places such as search engine optimization (SEO), comment and social media analysis, finding the topic of the document and then classifying the document according to the topic.

In the first part of the study, text preprocessing processes were applied on the document. Text preprocessing consists of interconnected processes. These processes are respectively; converting the text to lowercase letters, separating each word in the text, determining the types of words, finding the root form of words, finding and removing ineffective words from the text, taking the desired type of words from the text and removing repetitive words.

In the second part of the study, keywords are tried to extract from the text with automatic keyword extraction algorithms using the words obtained by text preprocessing. In this study, TextRank and RAKE from automatic keyword extraction algorithms were used. The values of the words were calculated with the TextRank algorithm. With the RAKE algorithm, the text is divided into word groups according to the ineffective words in the document. Word values calculated by TextRank algorithm were used to find the value of word groups. Finally, the values of word groups were sorted from large to small and the final keywords were found.

The study supports English and Turkish documents. TextRank and RAKE algorithm are used together in English documents. For this reason, keywords can contain more than one word. In Turkish documents, only TextRank algorithm is used, because the RAKE algorithm does not perform well in Turkish documents.

Interface has been developed in order to visualize the processes in the study. When the document file is given in the required format after the language selection is made through the interface, the keywords found are displayed on the interface in order. In addition, the results can be saved to the database through the interface and the database can be viewed via a web browser by clicking the necessary button on the interface.


### Usage
Python **Python 3.8.0** or higher version required.

1. Download this repo using ``git clone`` command.
2. Open the **CLI** in the project folder you downloaded.
3. If Pipenv doesn't exist, you must install it (Command: ```pip install pipenv```).
4. ```python -m pipenv install --python 3.8.0``` (If you are using another python version, write it here)
5. ```pipenv shell```
6. ```python main.py```

**Note:** When the program is first run, it will download about 1.2 GB. This is a one time operation.

### Sample Texts and Keywords

#### Text 1

Attorneys general of 44 US states and territories told Facebook CEO Mark Zuckerberg to ditch plans to create a version of Instagram for children. They wrote a letter stating social media is detrimental to children “who are not equipped to navigate the challenges of having a social media account. ” They also said that Facebook has not protected children in the past, such as when they created a version of Facebook Messenger for children. They described that children were able to bypass the restrictions to join group chats with strangers who were not approved by their parents. Facebook responded it was exploring the idea of Instagram for children, it would protect their safety and privacy, and it would not show advertising.

Keywords:

1. facebook ceo mark zuckerberg 
2. facebook messenger 
3. social media account
4. child


#### Text 2

Managers of the best football clubs in Europe have a plan. They want to make a European Super League. The best and biggest teams will be in the new league. The idea starts more than 30 years ago. The clubs want to start the league in 2021. Many people worry that it will change the world of football. 6 British teams sign the deal. Some of these teams are Arsenal, Chelsea, and Liverpool. 6 other teams from Spain and Italy sign, too. Some are Real Madrid, Barcelona, and Juventus. Then football fans get very angry last week. They do not agree with the new league. Some players from the best teams are also not happy. The British prime minister wants to make a new law. This law will make it impossible to make the new league.

Keywords

1. best football club
2. best team
3. new league
4. british team 
5. biggest team
6. new law
7. british prime minister
8. european super league


#### Text 3

A Black Hawk is a helicopter. Soldiers use it. Last week, the helicopter flies without pilots. It happens at Fort Campbell, US. There are two flights. One flight is 30 minutes long. The helicopter flies through a city. It is not a real city. A computer makes it. Then, the helicopter lands. The helicopter uses special technology. The technology makes it possible to fly without a pilot. A computer controls it. The technology is very good for pilots. The helicopter can fly at night. It can fly when the weather is bad. Pilots can do other things.

Keywords

1. helicopter
2. pilot
3. real city
4. special technology
5. Fort Campbell
6. Black Hawk
7. computer

If you like the project, don't forget to give star :blush:

---

# Turkish
## Textrank ve RAKE Algoritması ile Metinlerden Anahtar Kelime Çıkarma Projesi

### Özet

Anahtar kelimeler, doküman içeriğindeki konuyu anlamamızı büyük ölçüde kolaylaştırır. Doküman içeriğinin tamamını okumaya gerek kalmadan doküman hakkında çıkarımlar yapılabilir. Anahtar kelimeler; arama motoru optimizasyonu (SEO) işlemlerinde, yorum ve sosyal medya analizlerinde, dokümanın konusunun bulunması ve daha sonra konuya göre doküman sınıflandırma işlemleri gibi birçok yerde kullanılabilir.

Çalışmanın birinci kısmında doküman üzerinde metin ön işleme işlemleri uygulanmıştır. Metin ön işleme, birbirine bağlı işlemlerden oluşmaktadır. Bu işlemler sırasıyla; metni küçük harflere dönüştürme, metindeki her bir kelimeyi ayırma, kelimelerin türlerini belirleme, kelimelerin kök halini bulma, metindeki etkisiz kelimeleri bulma ve metinden çıkarma, metinden istenen türdeki kelimelerin alınması ve tekrar eden kelimelerin çıkarılmasıdır.

Çalışmanın ikinci kısmında metin ön işleme işlemleri ile elde edilen kelimeler kullanılarak otomatik anahtar kelime çıkarma algoritmaları ile metinden anahtar kelimeler çıkarılmaya çalışılmıştır. Bu çalışmada otomatik anahtar kelime çıkarma algoritmalarından TextRank ve RAKE kullanılmıştır. TextRank algoritması ile kelimelerin değerleri hesaplanmıştır. RAKE algoritması ile metin, dokümandaki etkisiz kelimelere göre kelime gruplarına ayrılmıştır. Kelime gruplarının değerini bulabilmek için TextRank algoritması ile hesaplanan kelime değerleri kullanılmıştır. Son olarak kelime gruplarının değerleri büyükten küçüğe sıralanarak nihai anahtar kelimeler bulunmuştur.

Çalışma İngilizce ve Türkçe dokümanları desteklemektedir. İngilizce dokümanlarda TextRank ve RAKE algoritması birlikte kullanılmıştır. Bu nedenle anahtar kelimelerde birden fazla kelime bulunabilmektedir. Türkçe dokümanlarda ise sadece TextRank algoritması kullanılmıştır. Bunun nedeni RAKE algoritmasının Türkçe dokümanlarda iyi performans vermemesidir.

Çalışmada işlemlerin görselleştirilmesi amacıyla arayüz geliştirilmiştir. Arayüz üzerinden dil seçimi yapıldıktan sonra gerekli formatta doküman dosyası verildiğinde, bulunan anahtar kelimeler sıralanmış şekilde arayüzde gösterilmektedir. Ayrıca sonuçlar arayüz aracılığı ile veritabanına kayıt edilebilmekte ve veritabanı, arayüz üzerinden gerekli butona basılarak web tarayıcısı aracılığı ile görüntülenebilmektedir.


### Kullanım
Python **Python 3.8.0** veya Üstü Gerekiyor.

1. Repoyu ```git clone``` Komutunu Kullanarak İndirin.
2. İndirdiğiniz Proje Klasöründe CLI Açın.
3. Pipenv Yoksa Onu Yüklemeniz Gerekir (Komut: ```pip install pipenv```).
4. ```python -m pipenv install --python 3.8.0``` (Başka Bir Python Sürümü Kullanıyorsanız Buraya Onu Yazın)
5. ```pipenv shell```
6. ```python main.py```

**Not:** Program İlk Çalıştırıldığında Yaklaşık 1,2 GB İndirecektir. Bu Tek Seferlik Bir İşlemdir.

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

Anahtar Kelimeler

1. helicopter
2. pilot
3. real city
4. special technology
5. Fort Campbell
6. Black Hawk
7. computer

Projeyi beğendiyseniz yıldız vermeyi unutmayın. :blush:
