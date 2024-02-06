Bu Python projesi, Android Debug Bridge (ADB) aracını kullanarak Android cihazınızı kablosuz veya USB üzerinden bağlayarak kameranızı uzaktan kullanmanıza olanak tanır. Proje, telefonun kamerasından veya bilgisayarınızın kamerasından video çekmeyi sağlar.

  

Kurulum Adımları:

----

  

Python Kurulumu:

1. ADB Kurulumu:
- ADB (Android Debug Bridge) aracını kullanarak Android cihazınızı bilgisayarınıza bağlamak için öncelikle ADB'nin yüklü olması gerekiyor.
- Android Studio veya SDK Platform Tools gibi bir kaynaktan ADB'yi edinebilirsiniz.
- İndirdiğiniz dosyalar arasında bulunan adb.exe dosyasının yolunu adb_path değişkenine doğru şekilde belirtin.


2. Gerekli Kütüphanelerin Kurulumu:
- Gerekli Python kütüphanelerini yüklemek için terminal veya komut istemcisine şu komutu yazın: ``` pip install opencv-python numpy```

3. Telefonunuzu Bağlama:
- Telefonunuzu kablosuz veya USB üzerinden bağlamak için programı çalıştırdıktan sonra gerekli seçimleri yapın.
- Kablosuz bağlantı için telefonun IP adresini (192.168.0.11 gibi) ve port numarasını belirtin.
- USB bağlantısı için telefonunuzun USB hata ayıklama modunu etkinleştirin ve USB kablosu aracılığıyla bilgisayarınıza bağlayın.

4. Kamerayı Kullanma:
- Program, telefonun kamerasını veya bilgisayarınızın kamerasını kullanma seçeneği sunar.
- Seçiminizi yapın ve programın sizden kamerayı kullanma izni istemesini bekleyin.

5. Mikrofonu Kullanma:
- Program, telefonun mikrofonunu veya bilgisayarınızın mikrofonunu kullanma seçeneği sunar.
- Seçiminizi yapın ve programın sizden mikrofonu kullanma izni istemesini bekleyin.

6. Programı Kapatma:
- Program, seçtiğiniz cihazları kullanarak video çekimini gerçekleştirecek ve sonlandıracaktır.
- Programı kapatmak için herhangi bir tuşa basın.

Bu adımları takip ederek, telefonunuzun kamerasını uzaktan kontrol etmek için bu projeyi kolayca kullanabilirsiniz.

  
  
  

ADB Nasıl Kurulur ve Bağlanır?

----

  

ADB Kurulumu:


  

1. SDK Platform Tools sayfasından işletim sistemine uygun ZIP dosyasını indirin.

2. ZIP dosyasını bir klasöre çıkartın.

3. Klasördeki adb.exe dosyasının yolunu belirleyin.

Telefonu Bağlama:
- A. Kablosuz Bağlantı:
	- Telefonunuzun ayarlarından "Geliştirici Seçenekleri"ni etkinleştirin.
	- "USB Hata Ayıklama"yı açın ve "Ağ Bağlantısı üzerinden ADB"yi etkinleştirin.
	- Bilgisayarınızda terminal veya komut istemcisine şu komutu yazarak telefonunuzu bağlayın:```adb connect 192.168.0.1:5555```  # Telefonun IP adresi ve port numarasını belirtin.

  

 - USB Bağlantısı:
	- Telefonunuzun ayarlarından "Geliştirici Seçenekleri"ni etkinleştirin.
	- "USB Hata Ayıklama"yı açın ve telefonunuzu USB kablosu ile bilgisayarınıza bağlayın.
	- Bilgisayarınızda terminal veya komut istemcisine şu komutu yazarak telefonunuzu bağlayın: ```adb devices```
	- Başarıyla bağlandıysanız, artık Python programınızı çalıştırabilir ve Android cihazınızın kamerasını uzaktan kontrol edebilirsiniz.
