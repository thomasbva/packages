# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 09:48:19 2023

@author: treyb
"""

# Make sure to change directory where other .py file exists

import unittest
from booklover import BookLover 
import pandas as pd


class BookLoverTestSuite(unittest.TestCase):

    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        
        book_obj = BookLover('Trey', 'treyb@gmail.com', 'Non-Fiction')
        book_obj.add_book('The Great Gatsby', 3)
        book_obj.has_read('The Great Gatsby')

        self.assertEquals(book_obj.book_list['book_name'][0], 'The Great Gatsby')
        self.assertEquals(book_obj.book_list['book_rating'][0], 3)

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        
        book_obj = BookLover('Trey', 'treyb@gmail.com', 'Non-Fiction')
        book_obj.add_book('Lord of the Flies', 3)
        book_obj.add_book('Lord of the Flies', 3)

        self.assertEquals(len(book_obj.book_list['book_name']), 1)
        
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        
        book_obj = BookLover('Trey', 'treyb@gmail.com', 'Non-Fiction')
        book_obj.add_book('1984', 5)
        
        self.assertTrue(book_obj.has_read('1984'))
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        
        book_obj = BookLover('Trey', 'treyb@gmail.com', 'Non-Fiction')
        book_obj.add_book('The Giver', 4)

        self.assertFalse(book_obj.has_read('Brave New World'))        

    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        
        book_obj = BookLover('Trey', 'treyb@gmail.com', 'Non-Fiction')
        book_obj.add_book('Beloved', 3)
        book_obj.add_book('The Iliad', 5)

        self.assertEquals(book_obj.num_books_read(), 2) 

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        
        book_obj = BookLover('Trey', 'treyb@gmail.com', 'Non-Fiction')
        book_obj.add_book('The Iliad', 5)
        book_obj.add_book('The Maze Runner', 5)
        book_obj.add_book('Beloved', 3)
        book_obj.add_book('The Giver', 2)
        
        self.assertEquals(len(book_obj.fav_books()), 2) 

if __name__ == '__main__':

    unittest.main(verbosity=3)