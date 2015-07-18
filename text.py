from twilio.rest import TwilioRestClient
import twilio
import os

account_sid = os.environ['ACCOUNT_SID']
auth_token = os.environ['AUTH_TOKEN']
caller=os.environ['TWILIO_PHONE']
receiver=os.environ['GRANTEE']

def send_text(body=body, caller=caller, receiver=receiver):
	try:
        client = twilio.rest.TwilioRestClient(account_sid, auth_token)
		message = client.messages.create(body=body,
	    to=receiver,
	    from_=caller)
    except twilio.TwilioRestException as e:
        print e	    