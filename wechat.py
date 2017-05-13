#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from flask import Flask,request, make_response
import hashlib
import string
import xml.etree.ElementTree as ET
import json
import time
import requests
import random
 
app = Flask(__name__)

@app.route("/wx", methods=['GET', 'POST'])
def wechat_auth():

		
	if request.method == 'GET':
		token = 'xxx' # your token
		query = request.args  # GET parameters
		signature = query.get('signature', '')
		timestamp = query.get('timestamp', '')
		nonce = query.get('nonce', '')
		echostr = query.get('echostr', '')
		s = [timestamp, nonce, token]
		s.sort()
		s = ''.join(s)
		sha1str = hashlib.sha1(str.encode(s)).hexdigest()

		if ((sha1str) == signature ):	
			return make_response(echostr)
		else:
			return ('hello')


	else:
		appid = 'xxx'
		appsecret = 'xxx'
		token_url = """https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s"""
		getUrl = token_url % (appid, appsecret)
		res = requests.get(getUrl)
		access_token = res.json()['access_token']
	
		rec=request.stream.read()
		xml_rec=ET.fromstring(rec)
		tou = xml_rec.find('ToUserName').text
		fromu = xml_rec.find('FromUserName').text
		mtype = xml_rec.find('MsgType').text
		tim = time.time()
		return_text = ""
        
		url = 'xxx'
		
        # return templates
		textTpl = """<xml>
            <ToUserName><![CDATA[%s]]></ToUserName>
            <FromUserName><![CDATA[%s]]></FromUserName>
            <CreateTime>%s</CreateTime>
            <MsgType><![CDATA[%s]]></MsgType>
            <Content><![CDATA[%s]]></Content>
            </xml>"""
			
		articleTpl = """<xml>  
			<ToUserName><![CDATA[%s]]></ToUserName>  
			<FromUserName><![CDATA[%s]]></FromUserName>  
			<CreateTime>%s</CreateTime>  
			<MsgType><![CDATA[news]]></MsgType>  
			<ArticleCount>2</ArticleCount>  
			<Articles>  
			<item>  
			<Title><![CDATA[%s]]></Title>   
			<Description><![CDATA[%s]]></Description>  
			<PicUrl><![CDATA[%s]]></PicUrl>  
			<Url><![CDATA[%s]]></Url>  
			</item>  
			<item>  
			<Title><![CDATA[%s]]></Title>  
			<Description><![CDATA[%s]]></Description>  
			<PicUrl><![CDATA[%s]]></PicUrl>  
			<Url><![CDATA[%s]]></Url>  
			</item>  
			</Articles>  
			</xml>"""
		
		if(mtype == 'event'):
			mevent = xml_rec.find('Event').text
			if(mevent == 'subscribe'):
                
                #Push Article as Welcome Message
                
				echostr = articleTpl % (fromu, tou, tim, 'xxx', 'xxx','http://cdn4.infoqstatic.com/statics_s2_20170502-0319/resource/articles/machine-translation-bottleneck-trend/zh/smallimage/yestone_879128676.jpg','http://www.infoq.com/cn/articles/sentiment-analysis-machine-learning-R','xxx','xxx','http://cdn1.infoqstatic.com/statics_s2_20170502-0319/resource/articles/sentiment-analysis-machine-learning-R/zh/smallimage/Snap4.jpg','http://www.infoq.com/cn/articles/machine-translation-bottleneck-trend')
				return(echostr)
				
				
                
        # app logic (API call)
		elif(mtype == 'text'):
			content = xml_rec.find('Content').text

	
			data = {"query":content,"user_id":"142857"}
			data = json.dumps(data, ensure_ascii=False).encode("UTF-8")
			headers = {'Content-Type': 'application/json'}
			res = requests.post(url, data, headers=headers)
			
			content2 = res.text
			content2 = content2.replace("\n", "")
			content2 = json.loads(content2)
			list_of_json = content2[0]
			length_of_json = len(list_of_json)
		
			if(list_of_json[0]['entity_id'] == '0' and list_of_json[0]['name']=='$'):
				return_text = random.choice(list_of_answers)
			
			elif(length_of_json<=5):
				for i in range(length_of_json):
					return_text += list_of_json[i]['name'] + '\n'
			else:
				return_text += str(length_of_json)
				for i in range(5):
					return_text += list_of_json[i]['name'] + '\n'

		
		else:
			return_text = "xxx"
			
		
		echostr = textTpl % (fromu, tou, tim, 'text', return_text)
		return(echostr)

if __name__ == "__main__":
    app.run()
