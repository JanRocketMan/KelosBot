from tempfile import NamedTemporaryFile
from flask import request, jsonify, send_from_directory, after_this_request, render_template
from app import app
from splinter import Browser
import time
from mmodel import KeLoss
import time




predicter = KeLoss()





@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/api/hi')
def send_hi():
    return 'hi'


@app.route('/api/addres', methods = ['POST'])
def get_request():
    global predicter
    msg = request.form['msg']
    info = predicter.get_post(msg)
    print("DBG:INFO_LIST:",info)
    text_red = info[0]
    percents = info[1]
    groop_id, post_id = info[2]
    print(groop_id,post_id)
    a ='https://vk.com/wall-'+str(groop_id)+'?own=1&w=wall-'+str(groop_id)+'_'+str(post_id) # Тут будет функция от нейронки :_)
    while True:
        fil = open('buffer', 'w')
        fil.write(a)
        fil.close()
        time.sleep(6)
        fil = open('buffer', 'r')
        hash = fil.read()
        if len(hash) > 5 and len(hash) < 39:
            print("Duck yeah! ", hash)
            fil.close()
            fil = open('buffer', 'w')
            fil.write('')
            fil.close()
            break
        else:
            fil.close()
            time.sleep(1)
            continue
    print("DBG:VALUES:", text_red, percents)
    return str(hash) + '~!~' + str(groop_id) + '~!~' + str(post_id) + '~!~'+ str(text_red)+'~!~' + str(percents)
    #with open('url.txt','w',encoding="utf-8") as fl:
    #    print("DBG:WRITE:FL:",a)
    #    fl.write(a)
    #time.sleep(30)
    #with open('hash.txt','r',encoding="utf-8") as fl:
    #    if len(fl.read())<5:
    #        print('НЕА')
    #    else:
    #        print('О да оно работает!!11!!!')
    #        res = fl.read()
    #        print('Это хеш: '+ res)
    # return str(res)+ ' '+str(groop_id)+' '+str(post_id)





@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('static/js', path)


@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('static/css', path)


@app.route('/fonts/<path:path>')
def send_fonts(path):
    return send_from_directory('static/fonts', path)


@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('static/img', path)
