from twilio.rest import TwilioRestClient 

account_sid = os.environ['ACCOUNT_SID']
auth_token = os.environ['AUTH_TOKEN']
caller=os.environ['TWILIO_PHONE']
receiver=os.environ['GRANTEE']

def receive_texts(ACCOUNT_SID=account_sid, AUTH_TOKEN=auth_token):
	client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 	 
	message = client.messages.get('SM9ab8d5a6fd7b72387de6c869f529ccbc') 
	text_body = message.body
	print text_body