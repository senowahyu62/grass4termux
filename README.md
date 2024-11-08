<p align="center">
	<img src="https://telegra.ph/file/09910c07cd4637fd64727.jpg" width="65%" style="margin-left: auto;margin-right: auto;display: block;">
</p>
<h1 align="center">M4L1K-0FC</h1>

# Running node grass in termux

Link registrasi https://app.getgrass.io/register?referralCode=k7qX2xNrCMRvVaR
#
Di bawah ini saya akan memberi tahu kalian langkah demi langkah secara rinci cara menjalankan ekstensi Grass Anda di Termux.
#
Aplikasi yang perlu di install:
1. Termux
2. Kiwi Browser, dsb (untuk masuk mode developer)
#
Disclaimer ON! ⚠️

If you do anything to your GetGrass account, you do it at your own risk!

## Command:

1. Perintah paling awal (wajib):

       pkg update && pkg upgrade (enter)

2. Required install:

       pkg install python (enter)
   #
       pip install loguru (enter)
   #
       pip install websockets (enter)
   #
       pkg install git (enter)
   #
       pkg install openssh (enter)
   #   
       pkg install nmap (enter)


4. Login SSH
Setelah run kode dibawah ini, ketik password nya:

       passwd (enter)

##### Clone node folder from github: 

    git clone https://github.com/M4L1K0FC/grasstermux4zhen (enter)

    cd grasstermux (enter)

Run SSH:

    sshd (enter)

Check your device userID (jgn lupa disalin):

    whoami (enter)

Check your IP (buat cek ip kalian, jgn lupa disalin):

    ifconfig (enter)

Check your PORT (buat cek port, default bisa pakai 8080 & 8022 sebenernya):

    nmap (ip address kalian) (enter)

Run your ssh
(ssh YourUserID@YourIP -p Port)
###### example: 

    ssh u0_a763@10.200.83.228 -p 8022 (enter)

Lalu submit password kalian tadi setuju login ke SSH, kalian akan otomatis kembali ke folder awal, lalu masuk ke folder grass4termux :

    cd grass4termux (enter)

4. Cara dapetin user id untuk running nodenya

1. Buka website Grass Network di software Kiwi Browser(atau bisa di software lain).
2. Login ke akun Grass Network kalian. Otomatis setelah login kalian akan langsung ada pada tampilan dasboard.
3. Klik bagian titik 3 di kanan atas pada browser kalian(Kiwi Browser), setelah itu pencet bagian Developer Tools.
4. Setelah masuk pada Developer tools tampilan awalnya kemungkinan kosong & tidak ada codingannya. Nah caranya kalian balik ke tab Grass Network tadi, terus refresh di bagian dashboard, kalau sudah kembali lagi ke tab developer toolsnya otomatis disitu sudah muncul codenya.
5. Pada bagian menu Element, Console, Sources, Network(kalau yang muncul cuma Element & Console kalian bisa klik » di sebelah kanannya. Setelah itu pencet bagian Network, terus pada bagian filter(kolom pencarian) kalian ketik user. Setelah itu akan muncul:

retrieveUser (pilih ini boleh)
retrieveUser (pilih ini boleh sama aja)
retrieveUserSettings
retrieveUserSettings 

Nah pada keempat file itu kalian bebas pilih yang retrieveUser pertama atau kedua, kalian tahan/klik kanan pada bagian retrieveUser-nya sampai muncul "Open in new tab" setelah itu kalian klik. Lalu akan muncul kode seperti ini.

{"result":{"data":{"referralCount":9,"parentReferrals":["rahasia","rahasia"],"userRole":"USER","totalUptime":361442,"hasDesktopDevice":true,"referralCode":"k7qX2xNrCMRvVaR","entity":"UserProfile","email":"rahasia@gmail.com","referredBy":"rahasia","created":"rahasia","isVerified":true,"isWalletAddressVerified":true,"lastRewardClaimed":"rahasia","modified:" rahasia","qualifiedReferrals":rahasia,"totalPoints":rahasia,"username":"4zhen","userId":"[Disini Nanti Ada Kode User ID Kalian, bisa kalian saling & simpan]","walletAddress":"sigma male rahasia"}}}

Setelah itu kalian kembali lagi ke termux 

# Kembali ke termux
edit file no_proxy.py:

    nano no_proxy.py (enter)

##### Kodenya kalian scroll pakai panah kebawah sampai Nemu penggalan program seperti dibawah:
#
async def main():

 #TODO Modify user_id
 
  _user_id = 'UserID Kalian' 
  
  await connect_to_wss(_user_id)
    
#
Isi bagian _user_id = 'with your userid'

Setelah itu bisa disave dengan

Tekan tombol CTRL pada bagian bar termux, setelah itu ketik huruf X di keyboard, lalu Y, lalu Enter. 
#
5. Run python

       python no_proxy.py (enter)

Selesai sudah connect, jangan lupa kasih reward ke developer nya hadeh 

* [`M4L1K0FC`](https://github.com/M4L1K0FC)