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
Disclaimer ON! ⚠️⚠️⚠️⚠️

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

       passwd

##### Clone node folder from github: 

    git clone https://github.com/M4L1K0FC/grasstermux4zhen

    cd grasstermux

Run SSH:

    sshd

Check your device userID (jgn lupa disalin):

    whoami

Check your IP (buat cek ip kalian, jgn lupa disalin):

    ifconfig

Check your PORT (buat cek port, default bisa pakai 8080 & 8022 sebenernya):

    nmap (ip address kalian)

Run your ssh
(ssh YourUserID@YourIP -p Port)
###### example: 

    ssh u0_a763@10.200.83.228 -p 8022

Lalu submit password kalian tadi setuju login ke SSH, kalian akan otomatis kembali ke folder awal, lalu masuk ke folder grass4termux :

    cd grass4termux

4. Cara dapetin user id untuk running nodenya

1. Buka website Grass Network 
//launch Devtool,

//refresh dashboard getgrass,

//open Devtool page,

//open page network, Search for "user" in devtools search.

//click {!}RetrieveUser

//Go to response tab.

//copy user id

# back to termux 
edit file no_proxy.py:

    nano no_proxy.py

##### Look for the line that contains:
#
async def main():

 #TODO Modify user_id
 
  _user_id = ''
  
  await connect_to_wss(_user_id)
    
#
fill in the _user_d = 'with your userid'

Save 

Click the CTRL button, then X, then Y, then Enter. 
#
5. run python

       python no_proxy.py
