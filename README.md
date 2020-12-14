# python_instargram_crawler


## this project is not completed.


Make Python Instargram Crawler

I referred to:   https://github.com/huaying/instagram-crawler
it is pretty structure project (it just my opinion)

Some problem. selenium isn't work, this project can't find input[name=username] in instargram login page.

i guess, that Cause webpage delayed loading attribute. 
so I put it in this line. [driver.implicitly_wait(5)]

~~~
driver.get(~~~)
driver.implicitly_wait(5)
driver.find~~~().send_keys() ~~ blahblah
~~~

As a result, succes to login instagram. 
but, huaying/instagram-crawler project, The has not yet worked.(i don't know problem. but i guess. related late loading issue.

