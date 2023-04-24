# GD&T Sapmasi Hesaplama Programı
# GD&T Tolerance Calculator

EN
There are two different dimensioning and sizing methods in technical drawing. These; coordinate based and Geometric Dimensioning and Sizing. With this program, it gives the GD&T tolerance value of a position information you measure manually or by CMM. In other words, it converts the coordinate-based tolerance value to the GD&T tolerance value.

TR
Teknik resimde iki farklı ölçülendirme ve boyutlandırma metodu vardır. Bunlar; koordinat bazlı ve Geometrik Ölçülendirme ve Boyutlandırma. Bu program ile CMM veya manuel olarak ölçtüğünüz bir konum bilgisinin GD&T tolerans değerini vermektedir. Bir başka deyişle koordinat bazlı tolerans değerini GD&T tolerans değerine çevirmektedir.

Bir parçanın teknik resme göre kontrolünde konum bilgisi ölçümleri, referanslar dikkate alınarak koordinat bazlı olarak yapılır.
Measuring of a location of a hole or pin in a technical drawing can make with coordinate system according to references.

![image](https://user-images.githubusercontent.com/34970413/233940242-c9107c18-37d3-4d32-a9aa-2ea0d4f3bbac.png)

Örnek tablolarda görebileceğiniz üzere her iki durumda da koordinat sistemine göre ölçüm sonuçları ve sapmaları verilmiştir. Fakat bu değerler, GD&T standardına göre verdiğimiz konum toleransı için herhangi bir şey ifade etmemektedir. 

As you can see at the examples, this values are based on coordinates system and showing as the deviation with actual and nominal location. Calculation of the deviation does not make sense on its own according to GD&T.

![image](https://user-images.githubusercontent.com/34970413/233940288-f2fbd563-1b3d-4b63-a912-c696b49e92dc.png)

Farkın temel sebebi, koordinat sisteminde tolerans bölgesi ‘ Kare ’ iken, GD&T sisteminde tolerans bölgesinin ‘ Daire ’ şeklinde tanımlanmasıdır. (Bu iki durum arasında matematiksel bir ilişki bulunmaktadır. ) 	Bu nedenle eğer teknik resimde GD&T standardı kullanıldıysa gelen ölçüm raporlarının sonuçları, hesaplanmış gerçek değerleri ile birlikte değerlendirilmelidir. GD&T tolerans değerine dönüştürülmelidir.

The main reason for the difference is that while the tolerance zone is 'Square' in the coordinate system, the tolerance zone is defined as 'Circle' in the GD&T system. (There is a mathematical relationship between these two cases.) Therefore, if the GD&T standard is used in the technical drawing, the results of the incoming measurement reports should be evaluated together with the calculated real values. It must be converted to a GD&T tolerance value.

![image](https://user-images.githubusercontent.com/34970413/233940327-1b41a3c8-dfb1-4c18-809b-aa654fcce4bf.png)

Bu kontrol için ‘GD&T Sapması Hesaplama Programı’ kullanabilirsiniz ☺ Aşağıda mevcut ara yüzü görebilirsiniz.
Application screen

<img width="765" alt="image" src="https://user-images.githubusercontent.com/34970413/233940414-cc109564-283c-4cf2-a28a-1888d9fd80d5.png">

Önceki sayfada paylaşılmış raporda verilen Ø60 ve Ø70 ölçülerinin konumları rapordaki değerler ile kontrol edilmiş ve tolerans içinde olup olmadığı incelenmiştir. 
The positions of the Ø60 and Ø70 dimensions given in the report shared on the previous page were checked with the values in the report and it was examined whether they were within the tolerance.

<img width="815" alt="image" src="https://user-images.githubusercontent.com/34970413/233940498-d71b218d-dd79-4362-a1b5-6ffe69d0e183.png">

Notlar bölümünde görebileceğiniz üzere;

Birkaç ölçümden sonra girdi satırına ‘ tumsonuclar ’ yazarsanız, başlangıçtan itibaren yaptığınız tüm ölçümlerin liste şeklinde çıktısını alabilirsiniz.
Ondalık ayıracı için  ‘ nokta  . ’ kullanılması gerekmektedir. 
Programı kapatmak için girdi satırına ‘kapat’ yazınız.

As you can see in the Notes section;

If you write ‘ tumsonuclar ' in the input line after a few measurements, you can output all the measurements you have made from the beginning in the form of a list.
. ’ must be used for decimal separator.
Type 'kapat' in the input line to close the program.

![image](https://user-images.githubusercontent.com/34970413/233940861-016f23d9-dcdc-45ea-9658-c4e8a9628292.png)

Program ile ilgili olumlu ve olumsuz tüm görüşlerinizi almaktan memnuniyet duyarım. Programı geliştirmek adına her türlü katkıya açığım. Programa ait kodları isteyenlere gönderebilirim.
Teşekkürler

I would be pleased to receive all your positive and negative comments about the program. I am open to any contribution to improve the program. I can send the code of the program to those who want it.

Thanks
Ümit Kirenci
u.kirenci@gmail.com



