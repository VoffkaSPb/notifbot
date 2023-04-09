import os
import requests
import json
import time

# Twitch API
twitch_client_id = os.getenv('sxmx7f6mbpfzxyldfckpjvpcxn5eae')
twitch_api_url = f"https://api.twitch.tv/helix/streams?user_login={os.getenv('1fader1')}"

# VK API
vk_access_token = os.getenv('vk1.a.5R1dZCR2Et3BAtw1ait8UjeB1w5KdxOPbaZExt6AwLsl7j7nGtK2-JkbiTSE4iT3pVpLJyK082VPR8cP0ULkGnflFH2rSNek9w0Xp99Zin0ycmo_wt77F3jALOT1k9MT9NgadoACs3UkjqedLCZBsx_7LeLTa-y0bB8QNtGrqw2ai2OcJzr_2KK-0F6yH25BXnp1PIIlBAxqNDo7FBmUCg')
vk_group_id = os.getenv('faderstream')

# Функция отправки сообщения в группу ВКонтакте
def send_vk_message(message, attachments=None):
    params = {
        'access_token': vk1.a.5R1dZCR2Et3BAtw1ait8UjeB1w5KdxOPbaZExt6AwLsl7j7nGtK2-JkbiTSE4iT3pVpLJyK082VPR8cP0ULkGnflFH2rSNek9w0Xp99Zin0ycmo_wt77F3jALOT1k9MT9NgadoACs3UkjqedLCZBsx_7LeLTa-y0bB8QNtGrqw2ai2OcJzr_2KK-0F6yH25BXnp1PIIlBAxqNDo7FBmUCg,
        'v': '5.131',
        'owner_id': f'-{faderstream}',
        'message': message,
        'attachments': attachments
    }
    response = requests.post('https://api.vk.com/method/wall.post', params=params)
    return response.json()

# Функция проверки трансляции на Twitch
def check_twitch_stream():
    headers = {'Client-ID': twitch_client_id}
    response = requests.get(twitch_api_url, headers=headers)
    data = json.loads(response.text)
    if data['data']:
        return data['data'][0]['started_at']
    else:
        return None

# Главная функция
def main():
    while True:
        twitch_stream_start_time = check_twitch_stream()

        if twitch_stream_start_time:
            message = "Привет, началась трансляция на Twitch! Переходите по ссылке: https://twitch.tv/1fader1"
            send_vk_message(message)
        
        time.sleep(60)

if __name__ == '__main__':
    main()
