#!/usr/bin/python3


from flask import Flask, request
from threading import Thread
import subprocess



app = Flask(__name__) 

#starts flwr client using received arguments
@app.route('/deploy', methods=['GET', 'POST'])
def startcli():
    
    src= request.form.get('src')
    model= request.form.get('model')
    sink= request.form.get('sink')
    print(src+model+sink)
    # prefix = "python3 -m flwr_example.factory."+src+"_"+model+"_cli"
    # suffix = " --server="+" --partition="+partition+" --clients="+"50"
    # # print(prefix+suffix)
    # # _ = subprocess.Popen(prefix+suffix, shell=True)
    # clithread= Thread(target=cli, args=(prefix, suffix,))
    # clithread.start()
    return 'ok', 200 


# def server(algo, fracfit, minfit, minav, numround):
#     pass
   
# def cli(prefix, suffix):
#     pass 


if __name__=='__main__':
    
    app.run(host='0.0.0.0',port=8000)