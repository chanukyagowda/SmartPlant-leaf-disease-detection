# -*- coding: utf-8 -*-
"""
Created on Thu May  6 20:53:12 2021

@author: ravi
"""

import boto3
import botocore

#BUCKET_NAME = 'my-bucket' # replace with your bucket name


s3 = boto3.client('s3', aws_access_key_id='AKIAWPXZRZQSL4VHNFAI' , aws_secret_access_key='5ZbJvTEDasVKrbdGUQHxn+u79sDVmq5i9yNAMUB7')
print('connection established')
s3.download_file('smartleaf','img01.JPG','img01.JPG')
print('file downloaded as image file')

from keras.models import load_model
model = load_model('train_model.h5')
       
#Compiling the model
model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
(model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy']))
#Making New Prediction
import numpy as np
from keras.preprocessing import image
#im = Image.open('self.load')   
test_image = image.load_img('img01.JPG',target_size = (64,64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image,axis = 0)
result = model.predict(test_image)

print(result[0])

import smtplib

TO = 'chanukyatechking@gmail.com'
SUBJECT = 'SMART LEAF NOTIFICATION'
#TEXT = 'Here is a message from python.'

# Gmail Sign In
gmail_sender = 'smartleaf07@gmail.com'
gmail_passwd = 'Smartplant@07'


server = smtplib.SMTP("smtp.gmail.com", 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(gmail_sender, gmail_passwd)

if result[0] == 0:
    print('Captured Image is Healthy Leaf')
    TEXT = 'Captured Image is Healthy Leaf'
    BODY = '\r\n'.join(['To: %s' % TO,
                    'From: %s' % gmail_sender,
                    'Subject: %s' % SUBJECT,
                    '', TEXT])
    server.sendmail(gmail_sender, [TO], BODY)
    print ('email sent')
else:
    print('Captured Image is Disease Leaf')
    TEXT = 'Captured Image is Disease Leaf'
    BODY = '\r\n'.join(['To: %s' % TO,
                    'From: %s' % gmail_sender,
                    'Subject: %s' % SUBJECT,
                    '', TEXT])
    server.sendmail(gmail_sender, [TO], BODY)
    print ('email sent')