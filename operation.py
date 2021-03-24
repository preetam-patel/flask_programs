from flask import Flask 
from opres import *
from excepti import *

app =Flask(__name__)
@app.route('/<name>/<int:a>/<int:b>',methods=['GET'])
def operation(name,a,b):
    obj1=Opera(a,b)
    try:
        if a>=11 or b>=11:
            raise Valuetolarge("a and b is not between 1-10")
        else:

            if name=='add' or name=="+":
                return str(obj1.add())
            

            if name=='sub' or name=="-":
                try:
                    if b>a:
                        raise Valuetosmall("b is less")
                    else:
                        return  str(obj1.sub())
                except Valuetosmall :
                    a,b==b,a
                    return  str(obj1.sub())

                   


            if name=='mul' or name=="*":
                return str(obj1.mul())

            try:
                if name=="div" :
                    if b==0:
                        raise Zeronotdivisable( "deno is zreo")
                    else:
                        return str(obj1.div())

            except Zeronotdivisable as w:
                return (str(w))

    except  Valuetolarge as q:
        return str(q)
        







if __name__ == '__main__':
   app.run(debug = True,port=5021)