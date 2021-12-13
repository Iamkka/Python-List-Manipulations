# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 14:14:55 2021

@author: Iamkka
"""

import sys
status_program = True
while status_program == True:

    #inisialisasi sets
    
    produk = ['Oreo','Chitato','Taro']
    produk_set = set(produk)
    
    
    #mulai program
    
    a = input('Siapakah nama Anda = ')
    print("Selamat datang " + a + "!")
    print("--------------------------------")
    
    #menu pilihan, ketikkan angka
    
    print("Silahkan pilih menu (cth: 1): ")
    print("1. Lihat list Produk")
    print("2. Tambah Produk")
    print("3. Update Produk")
    print("4. Hapus Produk")
    print("5. Cari Produk")
    
    pilih = input("Pilih Menu: ")
    
    #function
    
    def list_produk():
        print(set(produk))
        
    def tambah_produk():
        adding = input("Ketikkan nama produk yang ingin ditambah: ")
        produk_set.add(adding)
        print(produk_set)  
        
    def update_produk():
        updating = input("Ketikkan nama produk yang ingin diubah: ")
        produk_set.update(set([updating]))
        print(produk_set) 
        
    def hapus_produk():
        deleting = input("Ketikkan nama produk yang ingin dihapus: ")
        produk_set.remove(deleting)
        print(produk_set)  
        
    def cari_produk():
        searching = input("Produk yang ingin dicari: ")
        searched = searching in produk_set
        print(searched)
        
        
    #jika pilih menu no x, maka ke fungsi x
        
    if pilih == "1":
        list_produk()
        
        replay_program = print(input('Ingin mengulang program (yes/no):').lower())
        
        if replay_program == 'yes':
            status_program = True
        elif replay_program == 'no':
            raise SystemExit()
            
    elif pilih == "2":
        tambah_produk()
        
        replay_program = print(input('Ingin mengulang program (yes/no): ').lower())
        
        if replay_program == 'yes':
            status_program = True
        else:
            raise SystemExit()
            
    elif pilih == "3":
        update_produk()
        
        replay_program = print(input('Ingin mengulang program (yes/no): ').lower())
        
        if replay_program == 'yes':
            status_program = True
        else:
            raise SystemExit()
            
    elif pilih == "4":
        hapus_produk()
        
        replay_program = print(input('Ingin mengulang program (yes/no): ').lower())
        
        if replay_program == 'yes':
            status_program = True
        else:
            raise SystemExit()
            
    elif pilih == "5":
        cari_produk()
        
        replay_program = print(input('Ingin mengulang program (yes/no): ').lower())
        
        if replay_program == 'yes':
            status_program = True
        else:
            raise SystemExit()
            
    else:
        print("Silahkan pilih menu dengan angka yang tertera.")
        replay_program = print(input('Ingin mengulang program (yes/no): ').lower())
        
        if replay_program == 'yes':
            status_program = True
        elif replay_program == 'no':
            raise SystemExit()