# Unwanted Music Bot
## Music bot programmed in Python with interactive player, slash commands, integration with [last.fm](https://www.last.fm/), and much more.

- Slash commands
- Integration with [last.fm](https://www.last.fm/) for scrobbles (other features coming soon).
- Player controller: fixed/extended mode with song request channel and chat (skin: default), configurable with the command: /setup
- Player controller: fixed/extended mode with song request channel in forums with support for automatic status in the voice and stage channels

* There are several other skins; see them all using the /change_skin command (you can also create your own; use the default templates in the [skins] folder (utils/music/skins/) as a reference, create a copy with a different name, and modify it to your liking).

---

<details>
<summary>
Hosting on your own PC/VPS (windows/linux)
</summary>
<br>

### Requirements:

* Python 3.9, 3.10, or 3.11<br/>
[Download from the Microsoft Store](https://apps.microsoft.com/store/detail/9PJPW5LDXLZ5?hl=pt-br&gl=BR) (Recommended for Windows 10/11 users).<br/>
[Direct download from the official website](https://www.python.org/downloads/release/python-3117/) (Check this option when installing: **Add Python to the PATH**)
* [Git](https://git-scm.com/downloads) (Do not choose the portable version)

* [JDK 17](https://www.azul.com/downloads) or higher (Windows and Linux do not need to be installed, it is downloaded automatically)

`Note: This source requires at least 512MB of RAM and 1GHz of CPU to run normally (if you run Lavalink in the same instance as the bot, assuming the bot is private).`

### Start the bot (quick guide):

* Download this source as a [zip](https://github.com/Oyukihiro/Unwanted.git) and extract it (Or use the command below in the terminal/cmd and then open the folder):
```shell
git clone https://github.com/zRitsu/MuseHeart-MusicBot.git
```
* Double-click the source_setup.sh file (or just setup if your Windows is not displaying file extensions) and wait.</br>
`If you are using Linux, use the command in the terminal:`
```shell
bash source_setup.sh
```
* A file named **example.env** will appear. Edit it and enter the bot's token in the appropriate field (you can also edit other things in this same file if you want to make specific adjustments to the bot).</br>

* Now, just open the source_start_win.bat file to start the bot if your system is Windows. If it's Linux, double-click start.sh (or, if you prefer, run the bot using the command below):
```shell
bash source_start.sh
```

### Notes:

* To update your bot, double-click update.sh (Windows). For Linux, use the command in the shell/terminal:
```shell
bash source_update.sh
```
`When updating, there's a chance that any manual changes you made will be lost (if it's not a fork of this source)...`<br/>

`Note: If you're running the source directly from a Windows machine (and have Git installed), just double-click the source_update.sh file.`
</details>

## Special thanks and credits:

* [DisnakeDev](https://github.com/DisnakeDev) (disnake) and Rapptz for the original [discord.py](https://github.com/Rapptz/discord.py)
* [Pythonista Guild](https://github.com/PythonistaGuild) (wavelink)
* [Lavalink-Devs](https://github.com/lavalink-devs) (lavalink and lavaplayer)
* [DarrenOfficial](https://lavalink-list.darrennathanael.com/) Lavalink serverlist (Users who have published their lavalink servers are listed in the about command along with website/link).
* [zRitsu](https://github.com/zRitsu/MuseHeart-MusicBot) Original Code developer
