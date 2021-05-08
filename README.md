# Torrent To Google Drive Telegram Bot
Telegram bot to stream torrent files to Google Drive using Google Colab.


<a href="https://colab.research.google.com/github/spireon-ex10/Torrent-To-Google-Drive-Downloader/blob/master/Torrent_To_Google_Drive_Downloader_v2.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

### What is the purpose of it?
1. Since it is a Telegram bot ,you can access it from anywhere ,it will neither use your data or space.
2. Because of the Google Servers high download and upload speed ,you can stream torrents fast.
3. You can download torrent upto 75 gb without any problem.

### Tutorial
1. Contact @BotFather in your Telegram messenger to create new telegram bot
1. To get a token, send BotFather a message that says <code>/newbot</code> and paste token into **config.cfg** file.
2. When asked for a name and username  for your new bot choose username such as something that ends with the word <code>_bot</code>. For example <code>drivebottyl3r_bot</code>
3. If your chosen name is available, BotFather will send you a token
4. To set Description for your bot in BotFather do the following:
    - Send <code>/setdescription</code> to BotFather
    - Select the bot for which you are writing a Description
    - Change the description and send it to BotFather 
5. Ok now you're ready to go.
6. Create new folder in google drive and copy all the files from folder **Telegram_bot** to the newly created folder
7. Open<a href="https://colab.research.google.com/notebooks/intro.ipynb#recent=true"/></a> and upload **GDriveuploader.ipynb** file or  Click the badge which says **Open in Colab**
8. Run the whole notebook (**Runtime > Run all**)
9. Follow directions there.

After download finishes the downloaded files will be in there in your drive in a folder named "**Experiment**"

### Dependencies:
1. requests
2. lxml
3. beautifulsoup4
4. https://www.libtorrent.org/


# Screenshots
![TELEGRAMSS](https://github.com/nastyzera/Torrent-Drive-Telegram-Bot-Using-Colab/raw/master/Screenshots/TelegramBotScreenshot.jpeg)
![COLABSS](https://github.com/nastyzera/Torrent-Drive-Telegram-Bot-Using-Colab/raw/master/Screenshots/ColabScreenshot.jpeg)

### TODO
1. Concurrent torrent download
2. Progressbar of the download.
3. Cancel current download

# This whole repo is against Google Colab policy and you shouldn't be using it.
> **Why are hardware resources such as T4 GPUs not available to me?**
The best available hardware is prioritized for users who use Colaboratory interactively rather than for long-running computations. Users who use Colaboratory for long-running computations may be temporarily restricted in the type of hardware made available to them, and/or the duration that the hardware can be used for. We encourage users with high computational needs to use Colaboratory’s UI with a local runtime.
Please note that using Colaboratory for cryptocurrency mining is disallowed entirely, and may result in being banned from using Colab altogether.

<sub>Source: https://research.google.com/colaboratory/faq.html</sub>

### Maintained By : [Kunal Dongare](https://github.com/ogkunald)
