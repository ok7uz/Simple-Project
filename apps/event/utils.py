from infobip_channels.sms.channel import SMSChannel


def send_sms(user, relatives, event):
    user_name = f'{user.first_name} {user.last_name}'
    response_url = 'https://answer-connect-us.netlify.app/?user_id={user_id}&event_id={event_id}'
    channel = SMSChannel.from_auth_params({
        "base_url": "vv84lr.api.infobip.com",
        "api_key": "ec4510d13f4a61ebdcf3a25835560cb3-0ce36fc2-ff14-4df2-a23f-9b0485fdc95c"
    })
    
    for relative in relatives:
        sms = channel.send_sms_message({
            "messages": [{
                "destinations": [{'to': relative.phone_number}],
                "from": "InfobipSMS",
                "text": f"{user_name} sizni {event.title}ga taklif qilyapti. "
                         "\nOvoz berish: " + response_url.format(user_id=relative.id, event_id=event.id)
            }]
        })
        print(sms)
