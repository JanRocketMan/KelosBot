from splinter import Browser
import time, getpass

with open('buffer', 'w') as f:
    print("Hoi")

with Browser('chrome') as browser:
        url = "https://vk.com/dev/Post"
        browser.visit(url)
        login='89222204466'
        browser.find_by_id('email').fill(login)
        browser.find_by_id('pass').fill(getpass.getpass())


        button = browser.find_by_id('login_button')
        button.click()
        browser.visit(url)
        while True:
            fil = open('buffer',  'r')
            a = fil.read()
            fil.close()
            if len(a) > 38:
                print("Duck yeah!", a)
                browser.find_by_id('wall_post').fill(a)
                time.sleep(2)
                code = browser.find_by_id('code').value
                code =code.split("'")
                hashcode = code[-2]
                if len(hashcode) > 5:
                    fil = open('buffer', 'w')
                    fil.write(hashcode)
                    fil.close()
                    time.sleep(2)
                else:
                    continue# можно че-то вставить
            else:
                time.sleep(1)
                continue

            #with open('buffer', 'r') as fl:
            #    a = 'nop'
            #    if len(fl.read())<40:
            #        time.sleep(1)
            #        print("Nothing found...")
            #        continue
            #    else:
            #        a = fl.read()
            #        print("DBG:FL:", fl)
            #        print("DBG:GETPOST", a)
            #        browser.find_by_id('wall_post').fill(a)
            #        time.sleep(2)
            #        code = browser.find_by_id('code').value
            #        code =code.split("'")
            #        hashcode = code[-2]
            #        with open('hash.txt', 'w', encoding='utf-8') as fl:
            #            fl.write(hashcode)
#
#            with open('url.txt','w',encoding="utf-8") as fl:
#                fl.write('')
#
