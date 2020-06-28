from bot import telegram_chatbot
import re
import libtorrent as lt
import time
import datetime

ses = lt.session()
ses.listen_on(6881, 6891)
params = {
    'save_path': '/content/drive/My Drive/Torrent/',
    'storage_mode': lt.storage_mode_t(2),
    'paused': False,
    'auto_managed': True,
    'duplicate_is_error': True}


bot = telegram_chatbot("config.cfg")
pattern='magnet:\?xt=urn:btih:[a-zA-Z0-9]*'
def make_reply(msg):
    result=re.match(pattern,msg)
    if result:
        print(msg)
        handle = lt.add_magnet_uri(ses, msg, params)
        ses.start_dht()

        begin = time.time()
        print(datetime.datetime.now())

        print ('Downloading Metadata...')
        while (not handle.has_metadata()):
            time.sleep(1)
        print ('Got Metadata, Starting Torrent Download...')

        print("Starting", handle.name())
        startreply=('Download started for',handle.name())
        bot.send_message(startreply,from_)
        while (handle.status().state != lt.torrent_status.seeding):
            s = handle.status()
            state_str = ['queued', 'checking', 'downloading metadata', \
                    'downloading', 'finished', 'seeding', 'allocating']
            print ('%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s ' % \
                    (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, \
                    s.num_peers, state_str[s.state]))
            time.sleep(5)

        end = time.time()
        print(handle.name(), "COMPLETE")

        print("Elapsed Time: ",int((end-begin)//60),"min :", int((end-begin)%60), "sec")

        print(datetime.datetime.now())
        reply='Download Finished You can find downloaded file @ https://drive.google.com/drive/folders/1OXqhU4UX0e_eEcQME6ZG_GFB03ioknjb?usp=sharing'

    return reply

update_id = None
while True:
    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = str(item["message"]["text"])
            except:
                message = None
            from_ = item["message"]["from"]["id"]
            reply = make_reply(message)
            bot.send_message(reply, from_)
