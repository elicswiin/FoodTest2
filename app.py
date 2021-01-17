# from Project import app

# GET/POST ข้อมูลกับ http (รับข้อมูลจาก USER ด้วย WEBHOOK) 
# โดย GET จากเพื่อน หรือ http แล้ว POST ไปให้ Line API
# ดังนั้น Webhook เป็นตัวกลาง ระหว่าง USER กับ Server

from flask import Flask, request, abort # send_from_directory

app = Flask(__name__) # Instant

@app.route('/')
def hello():
  return 'Hi win'
def hello_Nat():
  return 'Hi Thanaphol'

@app.route('/tao55')
def hello_Nat():
  return 'Hi Natthamon'

@app.route('/webhook', methods=['POST','GET'])
def webhook():
  if request.method == 'POST':
    print(request.json)
    return 'This is method POST'

  elif request.method == 'GET':
    return 'This is method GET'
    

if __name__ == '__main__':
  app.run(port=200)