print("""
******************************************
//\\ GD&T Sapması Hesaplama Programı //\\
Bu program, 2D koordinat bilgisi alınarak yapılan konum ölçümlerinin
GD&T sistemindeki karşılığını vermektedir.
""")
print("""
Notlar:
1 - Tüm sonuçların listesini almak için değer kısmına 'tumsonuclar' giriniz.
2 - Hesaplamayı sonlandırmak için "kapat" değerini giriniz.
3 - Ondalık ayıracı olarak "." kullanınız.
4 - Sıfır ile başlayan ondalıklı sayıları, başında sıfır olmadan girebilirsiniz. (Ör: .05, .1 , .025)
""") 
print("""
                                                Versiyon: 0.2.6
                                                                                                
******************************************
""")

hesaplama = 1
sonuclistesi=list()

while True:
    
    deltax=str(input("X doğrultusundaki sapmayı giriniz:"))
    if deltax == "tumsonuclar":
            for i in sonuclistesi:
                print(i)
            continue
    if deltax == 'kapat':
        print('Program Kapatıldı.')
        break
    try:
        deltax=float(deltax)
    except ValueError:
        print('Şakacı seni :) Lütfen ondalıklı bir sayı değeri giriniz.')
        continue
    deltay=str(input("Y doğrultusundaki sapmayı giriniz:"))
    if deltay == "tumsonuclar":
            for i in sonuclistesi:
                print(i)
            continue
    if deltay == 'kapat':
        print('Program Kapatıldı.')
        break
    try:
        deltay=float(deltay)
    except ValueError:
        print('Şakacı seni :) Lütfen ondalıklı bir sayı değeri giriniz.')
        continue
    
    GDT_Sapması = 2*((deltax**2+deltay**2)**0.5) # Changes X-Y Co-Ordinates Deviations into Diameter of Position Tolerance
    print("[{}. sonuç]:".format(hesaplama), "GD&T Sapması=",'{:.3f}'.format(GDT_Sapması))

    hesaplama = hesaplama + 1
    sonuclistesi.append(GDT_Sapması)
    
    

