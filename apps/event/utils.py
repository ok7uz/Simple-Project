from infobip_channels.sms.channel import SMSChannel


response_url = 'https://connect-us-vebster.neftlify.app/response/?user_id={user_id}&event_id={event_id}'
channel = SMSChannel.from_auth_params({
    "base_url": "vv84lr.api.infobip.com",
    "api_key": "ec4510d13f4a61ebdcf3a25835560cb3-0ce36fc2-ff14-4df2-a23f-9b0485fdc95c"
})


def send_sms(user, relatives, event):
    user_name = f'{user.first_name} + {user.last_name}'
    
    for relative in relatives:
        channel.send_sms_message({
            "messages": [{
                "destinations": [{'to': relative.phone_number}],
                "from": "InfobipSMS",
                "text": f"Salom {relative.name}! {user_name} sizni {event.title}ga taklif qilyapti. "
                         "Quyidagi havola orqali o`z ovozingizni bering. "
                         + response_url.format(user_id=relative.id, event_id=event.id)
            }]
        })
