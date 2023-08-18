#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 06:09:35 2023

@author: lukaspentowsk_snhu
"""
from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    
    #Initializing the MongoClient.  This helps to access the
    #MongoDB databases and collections.  This will access the
    #AAC database and animals collection, using the user 'aacuser'
    
    def __init__(self, USER, PASS):
        USER = USER
        PASS = PASS
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30707
        DB = "AAC"
        COL = "animals"
        
        self.client = MongoClient('mongodb://%s:%s@%s:%d' %(USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        
    #A method that inserts a document into a specified MongoDB
    #database and collection, using a dictionary (data).  Returns
    #True if successful and False if not
    
    def create(self, data):
        if data is not None:
            result = self.database.animals.insert_one(data)
            if result != 0:
                return True
            else:
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")
    
    #A method that queries for documents from a specified MongoDB
    #database and collection.  
    def read(self, searchData):
        if searchData is not None:
            #Using {"_id": False} removes the _id field from the list
            result = self.database.animals.find(searchData, {"_id": False})
       
        else:
            result = self.database.animals.find({}, {"_id": False})
            
        return result
    
    #A method that queries for documents from the specified MongoDB
    #database and collection then updates the specified values. newData shall
    #be in the form of a dictionary
    def updateOne(self, searchData, newData):
        if searchData is not None:
            result = self.database.animals.update_one(searchData, {"$set": newData})
            return result.modified_count
        else:
            raise Exception("Nothing to update, because search parameter is empty")
            
    #A method that queries for multiple documents from the specified MongoDB
    #database and collection then updates all with the specified values. newData
    #shall be in the form of a dictionary
    def updateMany(self, searchData, newData):
        if searchData is not None:
            result = self.database.animals.update_many(searchData, {"$set": newData})
            return result.modified_count
        else:
            raise Exception("Nothing to update, because search parameter is empty")
            
    #A method to delete one item from the specified MongoDB database and collection
    def deleteOne(self, searchData):
        if searchData is not None:
            result = self.database.animals.delete_one(searchData)
            return result.deleted_count
        else:
            raise Exception("Nothing to delete, because search parameter is empty")
            
    #A method to delete multiple items from the specified MongoDB database and collection
    def deleteMany(self, searchData):
        if searchData is not None:
            result = self.database.animals.delete_many(searchData)
            return result.deleted_count
        else:
            raise Exception("Nothing to delete, because search parameter is empty")
            
