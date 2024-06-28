# DE - Report Automation using Python

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)

<style>
        pre {
            background-color: #f4f4f4;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 5px;
            overflow-x: auto;
        }
        code {
            font-family: 'Courier New', Courier, monospace;
            color: #d14;
        }
</style>

## Description
The first project is creating Report Automation. I started the project on November 12, 2023. I developed the Python source code using Google Colab from the use case provided in the following link: https://subscription.packtpub.com/book/programming/9781784398781/1/ch01lvl1sec15/case-study

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Contact](#contact)

## Installation
Steps to install :<br>
1. 

## Usage
### 1. Create Constructor Parent & Child


1.1.  Library Item (Constructor) - Parent <br>
<pre><code>
class LibraryItem():
  def __init__(self, title=None, upc=None, subject=None):
    self.title = title
    self.upc = upc
    self.subject = subject
</pre></code>
1.2 Book (Constructor) - Child <br>
class Book(LibraryItem):
  def __init__(self, title, upc, subject, isbn, authors, dds_number):
    LibraryItem.__init__(self,title, upc, subject)
    self.isbn = isbn
    self.authors = authors
    self.dds_number = dds_number
1.3. Magazine (Constructor) - Child <br>
class Magazine(LibraryItem):
    def __init__(self, title, upc, subject, volume, issue):
        LibraryItem.__init__(self,title, upc, subject)
        self.volume = volume
        self.issue = issue
1.4. DVD (Constructor) - Child <br>
class Dvd(LibraryItem):
    def __init__(self, title, upc, subject, actors, director,genre):
        LibraryItem.__init__(self,title, upc, subject)
        self.actors = actors
        self.director = director
        self.genre = genre
1.5. CD (Constructor) - Child <br>
class Cd(LibraryItem):
    def __init__(self, title, upc, subject, artist):
        LibraryItem.__init__(self,title, upc, subject)
        self.artist = artist

### 2. Create Class Catalog


class Catalog():
    def __init__(self, catalog=None):
        self.catalog = catalog
    def search(self, input_search):
        list_result = []
        for catalog in catalog_all:
            for item in catalog:
                if input_search.lower() in item.title.lower():
                    if type(item) == Magazine:
                        list_result.append('Title:'+ item.title+ 'Volume'+ item.volume)
                    elif type(item) == Book:
                        list_result.append('Title:'+ item.title+ 'DDS Number:'+ item.dds_number)
                    elif type(item) == Dvd:
                        list_result.append('Title:'+ item.title+ 'Genre:'+ item.genre)
                    elif type(item) == Cd:
                        list_result.append('Title:'+ item.title+ 'Artist:'+ item.artist)
                    else:
                        pass
        return list_result

### 3. Create Main


<!--self, title, upc, subject, isbn, authors, dds_number-->
book1 = Book (
    'Anaconda',
    None,
    'Anaconda Test',
    '1234-456',
    'Ridwan',
    '12314124515'
)
book2 = Book (
    'Piton',
    None,
    'Piton Test',
    '789-1011',
    'Bayu',
    '8975645614'
)
book3 = Book (
    'Sanca',
    None,
    'Sanca Test',
    '564-321',
    'Erlangga',
    '5423178542'
)

4. 


## Contact
Ridwan Bayu Erlangga - @readonebe14 - ridwanbayuerlangga@gmail.com

Project Link : <br>
[Report Automation using Python](https://github.com/readonebe14/learn-project/blob/portfolio/project/1.%20Report%20Automation/Project1%20-%20Report%20Automation.ipynb)

