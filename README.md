# CloudSEK_Sankal-Yadav_Backend-intern_assignment
This is a minimal web path brute-forcer (written in Python) with optimized memory and CPU usage.<br />
## Pre-requisites
* Python(version 3.0 or above)<br />

## Steps for installing
* Download the repository<br />
* Open terminal in the folder path<br />
* Run the commands as shown in the example below.<br />

## Input format :
### Sample Input: <br />
* In terminal type the following: <br />
python cloudSEK_Sankal.py https://github.com https://google.com https://amazon.com wordlist.txt 200 302 404 406 429 

## Output: 
### Sample Output:<br />

https://github.com/.git/config [Status code 404]<br />
https://github.com/.htaccess [Status code 404]<br />
https://github.com/info [Status code 404]<br />
https://github.com/admin [Status code 404]<br />
https://github.com/backup.zip [Status code 406]<br />
cloudSEK_Sankal.py executed in 0.4366 seconds.<br />



https://google.com/backup.zip [Status code 404]<br />
https://google.com/admin [Status code 404]<br />
https://google.com/.htaccess [Status code 404]<br />
https://google.com/info [Status code 404]<br />
https://google.com/.git/config [Status code 404]<br />
cloudSEK_Sankal.py executed in 0.3169 seconds.<br />



https://amazon.com/.htaccess [Status code 404]<br />
https://amazon.com/backup.zip [Status code 404]<br />
https://amazon.com/.git/config [Status code 404]<br />
https://amazon.com/admin [Status code 404]<br />
https://amazon.com/info [Status code 404]<br />
cloudSEK_Sankal.py executed in 2.3032 seconds.<br />
