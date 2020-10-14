
<h1 align="center" img="https://www.google.com/url?sa=i&url=https%3A%2F%2Fid.m.wikipedia.org%2Fwiki%2FBerkas%3ALogo_Unib.png&psig=AOvVaw3a5blSKtUOxykLiWxuydyC&ust=1602751265115000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCMDd3fDXs-wCFQAAAAAdAAAAABAD"><h1> 
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
    python 3.5+
    virtualenv
    
## Quick start
    sudo su
    git clone https://github.com/azhari33/nacm.git
    cd nacm
    virtualenv -p python3 env
    source env/bin/activate
    pip3 install -r requirements.txt
    cd nacm
    python3 manage.py runserver 0.0.0.0:8000
    akses via browser <ip:8000>
 
 ## Readme
    Pastikan server dapat terhubung ke perangkat yang dituju (router,switch,dll)
    Pastikan perangkat tujuan (router,switch) menggunakan protokol SSH versi 2
    Untuk perangkat cisco aktifkan scp server "ip scp server enable"
 
___

#### 1. Main Page
![Image of index](https://drive.google.com/file/d/1iJ85jbJt_iJAE21ALVdbCb2xjxZMEBLf/view?usp=sharing)

#### 2. Routing
![Image of routing](https://drive.google.com/file/d/12AgJE3va-pnVZqgbyatD5mJaWrTQ7Mst/view?usp=sharing)

#### 3. Backup
![Image of backup](https://drive.google.com/file/d/1drZVZkcGWYoqxwyn1jL9OGwm8LjIO57Q/view?usp=sharing)

#### 4. Restore
![Image of vlan](https://drive.google.com/file/d/1_-uUI8VrhOXypov8xYFTts8Nd9Cqjvyv/view?usp=sharing)

___

** Keperluan tugas akhir
azhari.ramadhan0902@gmail.com
