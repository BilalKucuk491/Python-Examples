# -*- coding: utf-8 -*-
"""
Created on Sat May 30 13:16:48 2020

@author: BİLAL
"""


import sqlite3

baglanti = sqlite3.connect("personel.db")
isaretci = baglanti.cursor()

def tablo_olustur():
    isaretci.execute("create table if not exists students(name TEXT,lastname TEXT,school_number İNT)")
    baglanti.commit()

def tablo_veri_ekleme(name,lastname,school_number):
    #isaretci.execute("insert into ogrenciler values('Aysel','Kurşun',7000 )")
    #isaretci.execute("insert into ogrenciler values('{}','{}',{})".format(isim,soyad,maas)) 
    isaretci.execute("insert into students values(?,?,?)",(name,lastname,school_number)) 
    baglanti.commit()
    
tablo_olustur()  
isim = input("You are name : ")
soyad = input("You are lastname : ")
maas = input("School number : ")
tablo_veri_ekleme(name,lastname,school_number)

baglanti.close()
   
