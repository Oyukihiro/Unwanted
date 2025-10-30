# -*- coding: utf-8 -*-
import itertools
from os.path import basename

import disnake

from utils.music.converters import fix_characters, time_format, get_button_style, music_source_image
from utils.music.models import LavalinkPlayer
from utils.others import PlayerControls


class ClassicStaticSkin:

    __slots__ = ("name", "preview")

    def __init__(self):
        self.name = basename(__file__)[:-3] + "_static"
        self.preview = "https://media.discordapp.net/attachments/554468640942981147/1047187412343853146/classic_static_skin.png"

    def setup_features(self, player: LavalinkPlayer):
        player.mini_queue_feature = False
        player.controller_mode = True
        player.auto_update = 0
        player.hint_rate = player.bot.config["HINT_RATE"]
        player.static = True

    def load(self, player: LavalinkPlayer) -> dict:

        data = {
            "content": None,
            "embeds": []
        }

        embed = disnake.Embed(color=player.bot.get_color(player.guild.me), description="")

        queue_txt = ""

        embed.description = f"[**{player.current.title}**]({player.current.uri or player.current.search_uri})\n\n"
        embed.set_image(url=player.current.thumb)
        embed_top = None

        if not player.paused:
            (embed_top or embed).set_author(
                name="Playing Now:",
                icon_url=music_source_image(player.current.info["sourceName"])
            )
        else:
            (embed_top or embed).set_author(
                name="On Hold:",
                icon_url="https://cdn.discordapp.com/attachments/480195401543188483/896013933197013002/pause.png"
            )

        if player.current.is_stream:
            duration = "🔴 **⠂Livestream**"
        else:
            duration = f"⏰ **⠂Duration:** `{time_format(player.current.duration)}`"

        txt = f"{duration}\n" \
              f"💠 **⠂Uploader:** `{player.current.author}`\n"

        if not player.current.autoplay:
            f"🎧 **⠂Requested by:** <@{player.current.requester}>\n"
        else:
            try:
                mode = f" [`Recomendation`]({player.current.info['extra']['related']['uri']})"
            except:
                mode = "`Recomendation`"
            txt += f"👍 **⠂Added via:** {mode}\n"

        if player.current.playlist_name:
            txt += f"📑 **⠂Playlist:** [`{fix_characters(player.current.playlist_name, limit=20)}`]({player.current.playlist_url})\n"

        if qsize := len(player.queue):

            data["content"] = "**Músicas na fila:**\n```ansi\n" + \
                              "\n".join(f"[0;33m{(n+1):02}[0m [0;34m[{time_format(t.duration) if not t.is_stream else '🔴 stream'}][0m [0;36m{fix_characters(t.title, 45)}[0m" for n, t in enumerate(
                                  itertools.islice(player.queue, 15)))

            if qsize > 15:
                data["content"] += f"\n\n[0;37mE mais[0m [0;35m{qsize}[0m [0;37mmúsicas{'s'[:qsize^1]}.[0m"

            data["content"] += "```"

        elif len(player.queue_autoplay):

            data["content"] = "**Upcoming recommended songs:**\n```ansi\n" + \
                              "\n".join(f"[0;33m{(n+1):02}[0m [0;34m[{time_format(t.duration) if not t.is_stream else '🔴 stream'}][0m [0;36m{fix_characters(t.title, 45)}[0m" for n, t in enumerate(
                                  itertools.islice(player.queue_autoplay, 15))) + "```"

        if player.command_log:
            txt += f"{player.command_log_emoji} **⠂Last Interaction:** {player.command_log}\n"

        embed.description += txt + queue_txt

        if player.current_hint:
            embed.set_footer(text=f"💡 Tip: {player.current_hint}")
        else:
            embed.set_footer(
                text=str(player),
                icon_url="https://i.ibb.co/QXtk5VB/neon-circle.gif"
            )

        data["embeds"] = [embed_top, embed] if embed_top else [embed]

        data["components"] = [
            disnake.ui.Button(emoji="⏯️", custom_id=PlayerControls.pause_resume, style=get_button_style(player.paused)),
            disnake.ui.Button(emoji="⏮️", custom_id=PlayerControls.back),
            disnake.ui.Button(emoji="⏹️", custom_id=PlayerControls.stop),
            disnake.ui.Button(emoji="⏭️", custom_id=PlayerControls.skip),
            disnake.ui.Button(emoji="<:music_queue:703761160679194734>", custom_id=PlayerControls.queue, disabled=not (player.queue or player.queue_autoplay)),
            disnake.ui.Select(
                placeholder="More option:",
                custom_id="musicplayer_dropdown_inter",
                min_values=0, max_values=1, required = False,
                options=[
                    disnake.SelectOption(
                        label="Add música", emoji="<:add_music:588172015760965654>",
                        value=PlayerControls.add_song,
                        description="Add a song/playlist to the queue."
                    ),
                    disnake.SelectOption(
                        label="Add to your favorites", emoji="💗",
                        value=PlayerControls.add_favorite,
                        description="Add the current track to your favorites."
                    ),
                    disnake.SelectOption(
                        label="Play from the beginning", emoji="⏪",
                        value=PlayerControls.seek_to_start,
                        description="Restart the current track from the beginning."
                    ),
                    disnake.SelectOption(
                        label=f"Volume: {player.volume}%", emoji="🔊",
                        value=PlayerControls.volume,
                        description="Adjust volume."
                    ),
                    disnake.SelectOption(
                        label="Mix", emoji="🔀",
                        value=PlayerControls.shuffle,
                        description="Shuffle the songs in the queue."
                    ),
                    disnake.SelectOption(
                        label="Readd", emoji="🎶",
                        value=PlayerControls.readd,
                        description="Add the played songs back to the queue."
                    ),
                    disnake.SelectOption(
                        label="Repeat", emoji="🔁",
                        value=PlayerControls.loop_mode,
                        description="Enable/Disable song/queue repeat."
                    ),
                    disnake.SelectOption(
                        label=("Disable" if player.nightcore else "Enable") + " the nightcore effect", emoji="🇳",
                        value=PlayerControls.nightcore,
                        description="Effect that increases the speed and pitch of the music."
                    ),
                    disnake.SelectOption(
                        label=("Disable" if player.autoplay else "Enable") + " automatic playback", emoji="🔄",
                        value=PlayerControls.autoplay,
                        description="System for automatically adding music when the queue is empty."
                    ),
                    disnake.SelectOption(
                        label="Last.fm scrobble", emoji="<:Lastfm:1278883704097341541>",
                        value=PlayerControls.lastfm_scrobble,
                        description="Enable/disable scrobbling/music logging on your Last.fm account."
                    ),
                    disnake.SelectOption(
                        label= ("Desativar" if player.restrict_mode else "Ativar") + " o modo restrito", emoji="🔐",
                        value=PlayerControls.restrict_mode,
                        description="Apenas DJ's/Staff's podem usar comandos restritos."
                    ),
                ]
            ),
        ]

        if (queue:=player.queue or player.queue_autoplay):
            data["components"].append(
                disnake.ui.Select(
                    placeholder="Upcoming songs:",
                    custom_id="musicplayer_queue_dropdown",
                    min_values=0, max_values=1, required = False,
                    options=[
                        disnake.SelectOption(
                            label=fix_characters(f"{n+1}. {t.single_title}", 47),
                            description=fix_characters(f"[{time_format(t.duration) if not t.is_stream else '🔴 Live'}]. {t.authors_string}", 47),
                            value=f"{n:02d}.{t.title[:96]}"
                        ) for n, t in enumerate(itertools.islice(queue, 25))
                    ]
                )
            )

        if player.current.ytid and player.node.lyric_support:
            data["components"][5].options.append(
                disnake.SelectOption(
                    label= "View lyrics", emoji="📃",
                    value=PlayerControls.lyrics,
                    description="Get lyrics for the current track."
                )
            )


        if isinstance(player.last_channel, disnake.VoiceChannel):
            data["components"][5].options.append(
                disnake.SelectOption(
                    label="Automatic status", emoji="📢",
                    value=PlayerControls.set_voice_status,
                    description="Configure the automatic status of the voice channel."
                )
            )

        return data

def load():
    return ClassicStaticSkin()
