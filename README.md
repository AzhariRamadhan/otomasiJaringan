
<p align="center">
    <img width="100" height="100" src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Logo_Unib.png/472px-Logo_Unib.png">
</p>
<h1 align="center">NACM</h1>
<h2 align="center">Network Automation Configuration Management</h2>

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![GitHub release](https://img.shields.io/github/release/Naereen/StrapDown.js.svg)](https://GitHub.com/Naereen/StrapDown.js/releases/)
[![Github all releases](https://img.shields.io/github/downloads/Naereen/StrapDown.js/total.svg)](https://GitHub.com/Naereen/StrapDown.js/releases/)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)
[![ForTheBadge built-by-Azhari](http://ForTheBadge.com/images/badges/built-by-developers.svg)](https://GitHub.com/Naereen/)


Fitur NACM:
- **Routing**: Konfigurasi dasar routing static, dynamic OSPF, RIPv1, RIPv2, dan BGP
- **Vlan**: Konfigurasi vlan id 
- **Code Based**: Mengirimkan konfigurasi berbasis text ke perangkat tujuan
- **Backup**: Backup konfigurasi perangkat
- **Restore**: Restore konfigurasi perangkat
- **Setting**: Menambah dan menghapus konfigurasi vendor

___

# Instalasi
## Requirement
    python 3
    virtualenv
    
## Quick start
    sudo su
    git clone https://github.com/AzhariRamadhan/otomasiJaringan.git
    cd otomasiJaringan
    python3 -m venv env
    source env/bin/activate
    pip install -r requirements.txt
    cd automation
    python manage.py runserver 
    akses via browser <ip:8000>
 
 ## Readme
    Pastikan server dapat terhubung ke perangkat yang dituju (router,switch,dll)
    Pastikan perangkat tujuan (router,switch) menggunakan protokol SSH versi 2
    Untuk perangkat cisco aktifkan scp server "ip scp server enable"
 
___

#### 1. Main Page
![image](https://drive.google.com/uc?export=view&id=1iJ85jbJt_iJAE21ALVdbCb2xjxZMEBLf)

#### 2. Routing
![image](https://drive.google.com/uc?export=view&id=12AgJE3va-pnVZqgbyatD5mJaWrTQ7Mst)

#### 3. Backup
![image](https://drive.google.com/uc?export=view&id=1drZVZkcGWYoqxwyn1jL9OGwm8LjIO57Q)

#### 4. Restore
![image](https://drive.google.com/uc?export=view&id=1_-uUI8VrhOXypov8xYFTts8Nd9Cqjvyv)

___

** Keperluan tugas akhir
azhari.ramadhan0902@gmail.com
