from app import app
import os
if __name__=='main':
    port = int(os.gentenv('PORT'),'5000')
    app.run(host='0.0.0.0', port = port)

