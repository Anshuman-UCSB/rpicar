from flask import Flask, render_template
from Driver import Driver
app = Flask(__name__)

driver = Driver()
driver.stop()

#rendering the HTML page which has the button
@app.route('/')
def home():
    return render_template('home.html')

#background process happening without any refreshing
@app.route('/background_process_test')
def background_process_test():
    print ("Hello")
    return ("nothing")

@app.route('/up')
def up():
    driver.forwards()
    print ("up clicked")
    return ("nothing")
    
@app.route('/down')
def down():
    driver.backwards()
    print ("down clicked")
    return ("nothing")
    
@app.route('/left')
def left():
    driver.left()
    print ("left clicked")
    return ("nothing")
    
@app.route('/right')
def right():
    driver.right()
    print ("right clicked")
    return ("nothing")
    
@app.route('/stop')
def stop():
    driver.stop()
    print ("stop clicked")
    return ("nothing")


if __name__ == "__main__":
    app.run()