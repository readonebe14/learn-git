# DE - Report Automation using Python

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)

<!--
<style>
        pre {
            background-color: #f4f4f4;
            padding: 20px;
            border: 1px solid #ddd;
            border-radius: 5px;
            overflow-x: auto;
            position: relative;
            margin: 20px 0;
        }
        code {
            font-family: 'Courier New', Courier, monospace;
            color: #d14;
        }
</style>
-->

## Description
The first project is creating Report Automation. I started the project on November 12, 2023. I developed the Python source code using Google Colab from the use case provided in the following link: https://subscription.packtpub.com/book/programming/9781784398781/1/ch01lvl1sec15/case-study

## Table of Contents
- [Installation](#installation)
- [Explanation](#explanation)
- [Contact](#contact)

## Installation
Steps to install :<br>
#### 1. Python: Python 3.x version is recommended.
#### 2. Jupyter Notebook: To run the notebook itself.
<pre><code>
pip install notebook
</pre></code>

## Explanation
### 1. Create Constructor Parent & Child
#### 1.1. Library Item (Constructor) - Parent
Defines the <code>LibraryItem</code> class with the basic attributes <code>title</code>, <code>upc</code>, and <code>subject</code>.
<pre><code>
class LibraryItem():
  def __init__(self, title=None, upc=None, subject=None):
    self.title = title
    self.upc = upc
    self.subject = subject
</pre></code>
#### 1.2 Book (Constructor) - Child <br>
Defines the <code>Book</code> class with the additional attributes <code>isbn</code>, <code>authors</code>, and <code>dds_number</code>.
<pre><code>
class Book(LibraryItem):
  def __init__(self, title, upc, subject, isbn, authors, dds_number):
    LibraryItem.__init__(self,title, upc, subject)
    self.isbn = isbn
    self.authors = authors
    self.dds_number = dds_number
</pre></code>
#### 1.3. Magazine (Constructor) - Child <br>
Defines the <code>Magazine</code> class with the additional attributes <code>volume</code> and <code>issue</code>.
<pre><code>
class Magazine(LibraryItem):
    def __init__(self, title, upc, subject, volume, issue):
        LibraryItem.__init__(self,title, upc, subject)
        self.volume = volume
        self.issue = issue
</pre></code>
#### 1.4. DVD (Constructor) - Child <br>
Defines the <code>Dvd</code> class with the additional attributes <code>actors</code>, <code>director</code>, and <code>genre</code>.
<pre><code>
class Dvd(LibraryItem):
    def __init__(self, title, upc, subject, actors, director,genre):
        LibraryItem.__init__(self,title, upc, subject)
        self.actors = actors
        self.director = director
        self.genre = genre
</pre></code>
#### 1.5. CD (Constructor) - Child <br>
Defines the class <code>Cd</code> with the additional attribute <code>artist</code>.
<pre><code>
class Cd(LibraryItem):
    def __init__(self, title, upc, subject, artist):
        LibraryItem.__init__(self,title, upc, subject)
        self.artist = artist
</pre></code>
        
### 2. Create Class Catalog
Defines the <code>Catalog</code> class with a search method to search for items based on certain input.
<pre><code>
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
</pre></code>
        
### 3. Create Instance
Create instances of <code>Book</code>, <code>Magazine</code>, <code>Dvd</code>, and <code>Cd</code> classes with various example data.

#### 3.1. Main Book
<pre><code>
###self, title, upc, subject, isbn, authors, dds_number
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
</pre></code>

#### 3.2. Main Magazine
<pre><code>
### title, upc, subject, volume, issue
magazine1 = Magazine(
    'Kompas',
    None,
    'Edisi November',
    'Volume 1',
    '-'
)
magazine2 = Magazine(
    'Lampu Merah',
    None,
    'Edisi Oktober',
    'Volume 2',
    'Tidak Ada'
)
magazine3 = Magazine(
    'Warta Kota',
    None,
    'Edisi Desember',
    'Volume 3',
    '-'
)
</pre></code>

#### 3.3. Main DVD
<pre><code>
### title, upc, subject, actors, director, genre
dvd1 = Dvd(
    'Petualang Sherina',
    None,
    'Petualang Sherina Test',
    'Sherina',
    'Reza',
    'Action'
)
dvd2 = Dvd(
    'Mission Impossible',
    None,
    'Mission Imposible Test',
    'Tom Cruise',
    'George',
    'Action'
)
dvd3 = Dvd(
    'Tiga Dara',
    None,
    'Tiga Dara Test',
    'Chitra',
    'Jaya',
    'Drama Romantic'
)
</pre></code>

#### 3.3. Main CD
<pre><code>
### title, upc, subject, artist
cd1 = Cd(
    'Musik 90an',
    None,
    'Musik 90an Test',
    'Pas Band'
)
cd2 = Cd(
    'Dewa19',
    None,
    'Dewa 19 Test',
    'Dewa 19'
)
</pre></code>

#### 3.a. Checking Main after created
Prints information from the <code>book1</code>, <code>magazine1</code>, <code>dvd1</code> and <code>cd1</code> objects.
<pre><code>
print(book1)
print(magazine1)
print(dvd1)
print(cd1)
</pre></code>

### 4. Collect Data of Each Type
Group items by type (<code>books</code>, <code>magazines</code>, <code>dvd</code>, <code>cd</code>).

<pre><code>
book = [book1, book2, book3]
magazine = [magazine1, magazine2, magazine3]
dvd =[dvd1, dvd2, dvd3]
cd = [cd1, cd2]
</pre></code>

### 5. Collect All Data
Collects all items into one list <code>catalog all</code>.
<pre><code>
catalog_all = [book, magazine, dvd, cd]
</pre></code>

### 6. Printing All Items
Prints information on all items in <code>catalog_all</code>.
<pre><code>
for catalog in catalog_all:
    for item in catalog:
        print(item.title)
        print(item.subject)
        print (type(item))
        print('\n')
</pre></code>

### 7. Search
- Defines the <code>input_search</code> variable with the value "Anaconda".
- Search for items in <code>catalog_all</code> that match <code>input_search</code> and print the item information.

<pre><code>
input_search = 'Anaconda'

for catalog in catalog_all:
    for item in catalog:
        if input_search.lower() in item.title.lower():
            if type(item) == Magazine:
                print('Title:', item.title, 'Volume', item.volume)
            elif type(item) == Book:
                print('Title:', item.title, 'DDS Number:', item.dds_number)
            elif type(item) == Dvd:
                print('Title:', item.title, 'Genre:', item.genre)
            elif type(item) == Cd:
                print('Title:', item.title, 'Artist:', item.artist)
</pre></code>

### 8. Catalog Search Method
Use the search method from the <code>Catalog</code> class to search for items based on <code>input_search</code>.
<pre><code>
Catalog(catalog_all).search(input_search)
</pre></code>
        
## Contact
- Name          : Ridwan Bayu Erlangga 
- Github        : @readonebe14 
- Email         : ridwanbayuerlangga@gmail.com
- LinkedIn      : [Ridwan Bayu Erlangga](https://www.linkedin.com/in/ridwanbayuerlangga/)

Project Link : [Report Automation using Python](https://github.com/readonebe14/learn-project/blob/portfolio/project/1.%20Report%20Automation/Project1%20-%20Report%20Automation.ipynb)

