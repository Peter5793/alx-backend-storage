# NoSQL

The projects here deal specifically with NoSQL

## Learning objectives
### General

* What NoSQL means
* What is difference between SQL and NoSQL
* What is ACID
* What is a document storage
* What are NoSQL types
* What are benefits of a NoSQL database
* How to query information from a NoSQL database
* How to insert/update/delete information from a NoSQL database
* How to use MongoDB

## Requirements
## MongoDB Command File
* All your files will be interpreted/compiled on Ubuntu 18.04 LTS using MongoDB (version 4.2)
* All your files should end with a new line
* The first line of all your files should be a comment: ```// my comment```
* A ```README.md``` file, at the root of the folder of the project, is mandatory
* The length of your files will be tested using ```wc```

## Installation of MongoDB 4.2 in Ubuntu 18.04

```
$ wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add -
$ echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" > /etc/apt/sources.list.d/mongodb-org-4.2.list
$ sudo apt-get update
$ sudo apt-get install -y mongodb-org
...
$  sudo service mongod status
mongod start/running, process 3627
$ mongo --version
MongoDB shell version v4.2.8
git version: 43d25964249164d76d5e04dd6cf38f6111e21f5f
OpenSSL version: OpenSSL 1.1.1  11 Sep 2018
allocator: tcmalloc
modules: none
build environment:
    distmod: ubuntu1804
    distarch: x86_64
    target_arch: x86_64
$
$ pip3 install pymongo
$ python3
>>> import pymongo
>>> pymongo.__version__
'3.10.1'
```

For this project i used windows and used the installation guide in the link attached [link]!(https://alx-intranet.hbtn.io/rltoken/NsSPUtCi8ilcou6wofRu1Q)
