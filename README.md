Pastebin Archive Reader (P.A.R)
===

P.A.R is a Python script that reads and downloads all files from Pastebin.com. You can choose to download all Python files, C++ files... It is destined to be run all days on a server.

1) Open up your GNU/Linux terminal or your command line in Windows                                                           
2) Go to the script directory and do :
<code>python PAR.py programming_language_name files_extension path/where/scripts/will/be/downloaded</code>

Example : 
<code>python PAR.py python .py /home/anon/scripts/</code> to download all Python files from http://pastebin.com/archive/python

or

<code>python PAR.py / .txt C:/users/anon/Desktop/files/</code> to download all files from http://pastebin.com/archive/

<h5>/!\</h5>
<ul>
<li>C++ = cpp</li>
<li>C# = csharp</li>
</ul>

Consult http://pastebin.com/ for more infos.

3) Files are being downloaded

<h4>Requirements</h4>
<ul>
<li>Python-requests ---> http://docs.python-requests.org/en/latest/user/install/#install</li>
<li>BeautifulSoup ---> http://www.crummy.com/software/BeautifulSoup/#Download</li>
</ul>
