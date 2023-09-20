anket_sonucu=1
ekleme_yapmak=2
anket_icerigi_gosterme=3
kac_tane_var=4
isimle_silme=5
yasla_silme=6
cikis=7
#kullanıcının girmesiyle her bir metoda yönlendirecek değerleri tanımladım

def main():
    secim=0 #while'ın içine girmesi için secimin ilk değerini 0 yaptım            
    while secim!=cikis:
        try:
            secim=menu_gosterme()#kullancının menüyü gördükten sonra tuşladığı değer seçime atanacak
            #ve girdiği seçimdeki metot çalıştırılacak
            if secim==anket_sonucu:
                anket_sonucu_ogrenme()
            if secim==ekleme_yapmak:
                ankete_ekleme_yapma()
            if secim==anket_icerigi_gosterme:
                anket_icerigi()
            if secim==kac_tane_var:
                kac_tane()
            if secim==isimle_silme:
                isim_ile_silme()
            if secim==yasla_silme:
                yas_ile_silme()
        except ValueError:
           print('lütfen ',anket_sonucu ,' ile ',cikis,' arasında bir secim tuslayiniz ')
           #eğer kullanıcı min ve max değerleri aşarsa uyarı ile tekrar menüye yönlendirilir

def menu_gosterme():
    print('-------------------------------')
    print('1.Katılımcıların Yas ortalamasını Ogrenmek icin ')
    print('2.Katılımcı Ekleme yapmak icin ')
    print('3.Tüm Katılımcıları görüntülemek için')
    print('4.Belirlediğiniz yaştan katılımcı sayısını görüntülemek için')
    print('5.Belirlediğiniz isimli katılımcıları silmek için')
    print('6.Belirlediğiniz yaştaki katılımcıları silmek için')
    print('7.Cikis yapmak için ')
    print('-------------------------------')
    print()
    
    secim=int(input('seciminizi tuslayiniz ')) #girilen değer seçime atanır
    
    if(secim<anket_sonucu or secim>cikis): #eger tuşlaması 1den küçük ya da 7den büyükse
        print('lütfen ',anket_sonucu ,' ile ',cikis,' arasında bir secim tuslayiniz ')
        print('tekrar menüye yönlendiriliyorsunuz')
        secim=menu_gosterme()

    return secim
def yas_degerleri_listesi_olusturma():#yaş listesini her metotta birden fazla kere oluşturmak yerine metot tanımladım
    icerik=dosya_okuma()#dosya okuma metoduna yönlendirilir
    yas_degerleri=[]
    st=""
    for satir in range(len(icerik)):
        ayrilmis=icerik.split('\n')#satırlara ayırarak her bi satırdaki elemanı listeye atadık
    for bosluklar in ayrilmis:
        st=st+bosluklar+' ' #böylece satırlar arasında \n yerine boşluk koyduk ki boşluğa göre split yapmamız kolaylaşsın
                            #bütün satırları yan yana getirerek tek metin haline getirdim
    for karakter in st:
        ayrilmis_st=(st.split(' '))   
    for eleman in ayrilmis_st:
        try:
            x =int(eleman)#integera dönüştürürüz eğer sayısal değerse zaten if bloğunun içine girer
            if(isinstance(x, int)):#türü integer mı 
                yas_degerleri.append(x)  #yaş değerini bulduğumuz için listemize ekleriz                     
        except ValueError:#string değerler int olamayacağı için verecekleri hatayı except ile önledim
            continue
    return yas_degerleri

def anket_sonucu_ogrenme():
    toplam=0
    icerik=dosya_okuma()
    if(len(icerik)==0):        
        print('dosya bostur')
    else:   
        yas_degerleri= yas_degerleri_listesi_olusturma()        
        for yas in yas_degerleri:
            toplam =toplam+yas
        print('toplam:',toplam)
        if len(yas_degerleri)!=0:
            ortalama=toplam/len(yas_degerleri)#0a bölünme hatası almayız zaten
                                              #elsein içine girmesi için içerikte bir değer olması şart
            print('ortalama:',ortalama)
        else:
            print('ankete henüz kimse katılmamış')            
        return yas_degerleri

def ankete_ekleme_yapma():   
    icerik=dosya_okuma()
    ad=input('adınızı giriniz ')
    soyad=input('soyadınızı giriniz ')
    yas=int(input('ankete dahil olacak yaşınızı giriniz '))
    
    if(len(icerik)!=0):
        yas_dizisi=yas_degerleri_listesi_olusturma()
        eski_toplam=sum(yas_dizisi)
        yeni_toplam=eski_toplam+yas
        yas_dizisi.append(yas)
        yeni_ort=yeni_toplam/len(yas_dizisi)
        print('-----------------------')
        print('güncel yaş toplamı:' + str(yeni_toplam))
        print('güncel yaş ortalama:' + str(yeni_ort))
    else:
        print('-----------------------')
        print('güncel yaş toplamı:' + str(yas))
        print('güncel yaş ortalama:' + str(yas))
        
    dosya=open('anketdosyası.txt','a')
    dosya.write(ad+' ')#kullancının girdiği ad soyad ve yaş değerlerini dosyaya ekliyoruz
    dosya.write(soyad+' ')
    dosya.write(str(yas)+'\n')
    print('tekrar menüye yönlendiriliyorsunuz ')
    dosya.close()
    
def anket_icerigi():
    dosya=open('anketdosyası.txt','r')
    sonraki_satir=dosya.read()    
    if (len(sonraki_satir)!=0):
        print('Dosyanın içindeki veriler sıralanıyor')
        while sonraki_satir!='':
            #icerik=dosya.readline()       
            print('-----------------------------------')        
            sonraki_satir=sonraki_satir.rstrip('\n')
            print(sonraki_satir)
            sonraki_satir=dosya.readline()
        print('tekrar menüye yönlendiriliyorsunuz')
    else:
        print('dosyada veri bulunmuyor \neklemek için 2 numaralı seçeneği kullanabilirsiniz')
    dosya.close()

def kac_tane():#kullanıcıdan alınan sayıdaki elemandan kaç tane olduğunu bulma
    icerik=dosya_okuma()    
    if (len(icerik)!=0):
        yas_degerleri=yas_degerleri_listesi_olusturma()
        aranilan=int(input('Hangi yaştan kaç tane olduğunu öğrenmek istiyorsunuz? '))
        sayac=0
        for sira in yas_degerleri:
            if(sira==aranilan):
                sayac=sayac+1
        if(sayac==0):
            print(aranilan,'yaşında ankete katılan kimse yoktur')    
        else:
            print('aradığınız ',aranilan,' yaşında ankete katılan ',sayac,' tane kişi vardır. ')
        return sayac
    else:
        print('dosyada veri bulunmuyor \neklemek için 2 numaralı seçeneği kullanabilirsiniz')
               #iki print yapmak yerne \n kullandım

def isim_ile_silme():
    icerik=dosya_okuma()
    if(len(icerik)!=0):  
        for satir in range (len (icerik)):  
            ayrilmis=icerik.split('\n')#satırları ayırarak liste oluşturduk
        ad=input('silmek istediğiniz kişinin adını giriniz: ')
        soyad=input('silmek istediğiniz kişinin soyadını giriniz: ')
        silinmek_istenen=ad+' '+soyad+' '#2. boşluğu yaşla arasında boşluk olduğu için ekledim
        sayac=0 #bu sayacı ayrilmis listesinden eleman silerke lazım olan index için kullanıyoruz
        bulma=0#bulunma durumunu kontrol eder
        st=""    
        for eleman in ayrilmis:     
            for harf in eleman:
                try:
                    x=int(harf)
                    if(isinstance(x, int)): #int değer görmesi isim bitmiş kişinin yaşına geçmişiz demek bu yüzden kontrol burada yapılır
                        if(st==silinmek_istenen):
                            bulma=bulma+1
                            ayrilmis.pop(sayac)
                            break  #silinmek isteneni bulduğumuz için daha fazla burada bu eleman içinde dönmeye gerek yok sonraki elemana geçiyoruz                  
                except ValueError:
                    st=st+harf #string değer gördükçe harf harf ekleyecek
            sayac=sayac+1#bir sonraki elemana geçtiği için index olarak kullandığımız sayaç 1 artar
            st=""    #bir sonraki elemanı kontrol edeceğimiz için st'yi boş yapacağız
        dosya=open('anketdosyası.txt','w')
        for eleman in ayrilmis:#eleman silinebileceği için düzenlenen ayrilmis listemizi dosyayı boşaltıp tekrar yazıcaz
              if eleman!='':
                 eleman=eleman+'\n'
                 dosya.write(eleman) 
        dosya.close()
        if(bulma==0):
            print(silinmek_istenen+'adında ankete katılan kimse yoktur')
        else:        
            print(silinmek_istenen+'silinmiştir')        
    else:
        print('ankete kimse katılmamaıştır')
        
def yas_ile_silme(): #isim ile silmeyle aynı mantık 
    icerik=dosya_okuma()
    if(len(icerik)!=0):  
        for satir in range(len(icerik)):  
            ayrilmis=icerik.split('\n')
        silinmek_istenen=input('silmek istediğiniz yaş değerini giriniz: ')
        sayac=0
        bulma=0
        st=""
        for eleman in ayrilmis:     
            for harf in eleman:
                try:                    
                    x=int(harf)
                    if(isinstance(x, int)):
                        st=st+str(x)
                except ValueError:
                    continue
            if(st==silinmek_istenen):
                bulma=bulma+1
                ayrilmis.pop(sayac)
            sayac=sayac+1
            st=""    
        dosya=open('anketdosyası.txt','w')
        for eleman in ayrilmis:
              if eleman!='':
                 eleman=eleman+'\n'
                 dosya.write(eleman) 
        dosya.close()
        if(bulma==0):
            print(silinmek_istenen+' yaşında ankete katılan kimse yoktur')
        else:        
            print(silinmek_istenen+' yaşındaki tüm katılımcılar silinmiştir')        
    else:
        print('hiç katılımcı yoktur')
        
def dosya_okuma():
    dosya=open('anketdosyası.txt','r')
    icerik=dosya.read()
    dosya.close()
    return icerik
main()
