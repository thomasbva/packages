# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 09:15:13 2023

@author: treyb
"""

import pandas as pd
import numpy as np

class BookLover:
    name = ''
    email = ''
    fav_genre = ''
    book_list = pd.DataFrame({})
    num_books = 0
    
    def __init__(self, name, email, fav_genre):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre

        
    def add_book(self, book_name, rating):
        if len(self.book_list)==0:
            new_book = pd.DataFrame({
                'book_name': [book_name], 
                'book_rating': [rating]})
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books += 1
        elif self.book_list['book_name'].str.contains(book_name).any() == False:
            new_book = pd.DataFrame({
                'book_name': [book_name], 
                'book_rating': [rating]})
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books += 1
        else:
            print('Book already exists')
            
            
    def has_read(self, book_name):
        if self.book_list['book_name'].str.contains(book_name).any():
            return True
        else:
            return False
        
    def num_books_read(self):
        return self.num_books
    
    def fav_books(self):
        return self.book_list[self.book_list['book_rating'] > 3]
        
