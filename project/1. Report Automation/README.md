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
Mendefinisikan kelas LibraryItem dengan atribut dasar title, upc, dan subject.
<pre><code>
class LibraryItem():
  def __init__(self, title=None, upc=None, subject=None):
    self.title = title
    self.upc = upc
    self.subject = subject
</pre></code>
#### 1.2 Book (Constructor) - Child <br>
Mendefinisikan kelas Book dengan atribut tambahan isbn, authors, dan dds_number.
<pre><code>
class Book(LibraryItem):
  def __init__(self, title, upc, subject, isbn, authors, dds_number):
    LibraryItem.__init__(self,title, upc, subject)
    self.isbn = isbn
    self.authors = authors
    self.dds_number = dds_number
</pre></code>
#### 1.3. Magazine (Constructor) - Child <br>
Mendefinisikan kelas Magazine dengan atribut tambahan volume dan issue.
<pre><code>
class Magazine(LibraryItem):
    def __init__(self, title, upc, subject, volume, issue):
        LibraryItem.__init__(self,title, upc, subject)
        self.volume = volume
        self.issue = issue
</pre></code>
#### 1.4. DVD (Constructor) - Child <br>
Mendefinisikan kelas Dvd dengan atribut tambahan actors, director, dan genre.
<pre><code>
class Dvd(LibraryItem):
    def __init__(self, title, upc, subject, actors, director,genre):
        LibraryItem.__init__(self,title, upc, subject)
        self.actors = actors
        self.director = director
        self.genre = genre
</pre></code>
#### 1.5. CD (Constructor) - Child <br>
Mendefinisikan kelas Cd dengan atribut tambahan artist.
<pre><code>
class Cd(LibraryItem):
    def __init__(self, title, upc, subject, artist):
        LibraryItem.__init__(self,title, upc, subject)
        self.artist = artist
</pre></code>
        
### 2. Create Class Catalog
Mendefinisikan kelas Catalog dengan metode search untuk mencari item berdasarkan input tertentu.
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
Membuat instance dari kelas Book, Magazine, Dvd, dan Cd dengan berbagai data contoh.

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
Mencetak informasi dari objek book1, magazine1, dan dvd1.
<pre><code>
print(book1)
print(magazine1)
print(dvd1)
print(cd1)
</pre></code>

### 4. Collect Data of Each Type
Mengelompokkan item berdasarkan jenisnya (buku, majalah, dvd, cd).

<pre><code>
book = [book1, book2, book3]
magazine = [magazine1, magazine2, magazine3]
dvd =[dvd1, dvd2, dvd3]
cd = [cd1, cd2]
</pre></code>

### 5. Collect All Data
Mengumpulkan semua item ke dalam satu daftar catalog_all.

<pre><code>
catalog_all = [book, magazine, dvd, cd]
</pre></code>

### 6. Printing All Items
Mencetak informasi semua item yang ada dalam catalog_all.
</pre></code>
for catalog in catalog_all:
    for item in catalog:
        print(item.title)
        print(item.subject)
        print (type(item))
        print('\n')
</pre></code>

### 7. Search
- Mendefinisikan variabel input_search dengan nilai "Anaconda".
- Melakukan pencarian item dalam catalog_all yang sesuai dengan input_search dan mencetak informasi item tersebut.

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

### 8. Catalog Search Method
Menggunakan metode search dari kelas Catalog untuk mencari item berdasarkan input_search.
Catalog(catalog_all).search(input_search)
</pre></code>
        
## Contact
Ridwan Bayu Erlangga - @readonebe14 - ridwanbayuerlangga@gmail.com

Project Link : <br>
[Report Automation using Python](https://github.com/readonebe14/learn-project/blob/portfolio/project/1.%20Report%20Automation/Project1%20-%20Report%20Automation.ipynb)

