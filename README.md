Pastebin Archive Reader (P.A.R)
===

P.A.R is a Python script that reads and downloads all files from Pastebin.com. You can choose to download all Python files, C++ files... It is destined to be run all days on a server.

1) Open up your GNU/Linux terminal or your command line in Windows                                                           
2) Go to the script directory and do :
<code>python PAR.py the_language_archive_you_want_to_download the_extension_of_your_files</code>

Example : 
<code>python PAR.py python .py</code> to download all Python files from http://pastebin.com/archive/python 
or <code>python PAR.py  .txt</code> to download all files from http://pastebin.com/archive/ ...

Here's the full list :
<code>
bash,
c,
csharp,
cpp,
css,
html,
html5,
java,
javascript,
lua,
text,
objc,
perl,
php,
python,
rails
</code>

<h4>Warning !</h4> Files are downloaded in the script directory, so don't run it on your desktop...
