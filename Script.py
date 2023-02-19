class script(object):
    START_TXT = """<b>Hello 👋 {},

My Name Is <a href='t.me/TkEntertainment_Bot'>Tk Entertainment Bot</a>. I Work Only In <a href="https://t.me/Tk_movies_adda">Tk Entertainment</a> Group So You Can't Get My Services By Adding Me To Your Group So Don't Waste Your Time & Data 😉

For More Information Click ℹ️ Help</b>"""

    HELP_TXT = """<b>Hello 👋 {},

I Can Guide You Through All Of <a href='t.me/newuniquemovies_bot'>Tk Entertainment Bot</a>'s Cool Features & How To Properly Use Them. Use The Buttons Below To Navigate Through All Of The Modules</b>"""

    TK_ENTERTAINMENT = """
ミ★ TK ENTERTAINMENT ★彡

👉 Search Of New & Old Movies/Series
👉 Avilable In Many Sizes & Languages 
👉 Receivable In Various Quality"""
    
    ALIVE_TXT = """Help: <b>Alive</b>

- To Find Out If I'm Dead Or Not

<b>Commands and Usage:</b>

★ /alive - Check I'm Alive Or Not."""

    IMDB_TXT = """Help: <b>IMDB</b>

- A Module To Get The Movie Informations. Use This Module To Get Movie Informations

<b>Commands and Usage:</b>

★ /imdb  - Get The Film Information From IMDB Source.
★ /search  - Get The Film Information From Various Sources."""

    LINK_TXT = """Help: <b>Invite Link</b>

- You Can Easily Find Group Invitation Link

<b>Commands and Usage:</b>

★ /link - To Get Group Or Channel Link"""

    INFO_TXT = """Help: <b>IDs</b>

- A Module To Fetch Telegram User, Group, Channel & Sticker Info

<b>Commands and Usage:</b>

★ /id - To Get Telegram User ID
★ /info - To Get User Information
★ /json - To Get All Info
★ /stickerid - To Get TG Sticker ID"""

    DONATE_TXT = """Hello 👋 {},

To Support My Works, Please Feel Free To Donate Any Amount You Like 💸

UPI 🆔 Details

Google pay 📲 joynathnet4@oksbi
Phonepe 📲 bijoy.nath@ybl

Thank You For Showing Interest In My Works 🙏"""

    MUSIC_TXT = """Help: <b>Music</b>

Music Download Modules, For Those Who Love Music.

• /song Or /mp3 [Song Name] - Download Song From YouTube 
• /video or /mp4 [song Name] - Download Video From YouTube"""

    IMDB_TEMPLATE_TXT = """
 <b>🎬 Title:</b> <a href={url}>{title}</a> [{year}] —<b>{kind}</b>

<b>📆 Release:</b> <a href={url}/releaseinfo>{release_date}</a>
<b>🌟 Rating:</b> <a href={url}/ratings>{rating} / 10</a>\n(Based On <code>{votes}</code> User Ratings)

<b>🎭 Genres:</b> #{genres}
<b>📀 Runtime:</b> <code>{runtime} minutes</code>

<b>☀️ Languages:</b> #{languages}
<b>🌎 Country of Origin:</b> #{countries}
<b>🎥 Director:</b> {director}"""
    
    STATUS_TXT = """<b>Total Files:</b> <code>{}</code>
<b>Total Users:</b> <code>{}</code>
<b>Total Chats:</b> <code>{}</code>
<b>Used Storage:</b> <code>{}</code> MiB
<b>Free Storage:</b> <code>{}</code> MiB"""

    LOG_TEXT_G = """🎬 Group = {}(<code>{}</code>)
👥 Total Members = <code>{}</code>
👤 Added By - {}"""

    LOG_TEXT_P = """🆔 ID - <code>{}</code>
👤 Name - {}"""

    ALRT_TXT = """Hello 👋 {}, This Is Not Your Message 🤗\n\nRequest Your Own ✍️\n\n©️ TK ENTERTAINMENT"""

    OLD_ALRT_TXT = """Hello 👋 {}, You Are Using One Of My Old Messages, Please Request Again 🙏"""

    CUDNT_FND = """I Couldn't Find Anything Related To {} Did You Mean Any One Of These..?"""

    I_CUDNT = """Hello 👋 {},\n\nI Couldn't 🔍 Find {} You Asked For 🤷\n\nClick [GOOGLE] [IMDB] On Any Button And Find The Correct Movie/Series Name And Enter It Here 💯\n\nIf You Do Not Receive The Movie/Series Even After Entering The Correct Name Then Your Requested Movie/Series Does Not Exit In My Database 🗄"""

    I_CUD_NT = """Couldn't Find Any Related To {}.Please Check Your Spelling On GOOGLE Or IMDB"""

    MVE_NT_FND = """This Movie Not Found In DataBase"""

    TOP_ALRT_MSG = """Checking For Movie In DataBase..."""

    MELCOW_ENG = """<b>Hello 👋 {}, Welcome To {} 💐</b>"""
   
    SPELL_HELP = """
☑️ DO
👉 Type Only In English

❌ DON'T
👉 Avoid Symbols (/.,:;'"-)
👉 Avoid Requesting Same Movie/Series Repeatedly
👉 Avoid Requesting Unreleased Movie/Series"""
    
    REPRT_MSG = """Report Sent To Admin"""

    CAPTION = """<b>
🎬 𝐓𝐢𝐭𝐥𝐞 - <code>{file_name}</code>
✯ ━━━━━ ✧ ━━━━━ ✯
🔘 𝐉𝐨𝐢𝐧
👉 <a href='https://t.me/Tk_movies_adda'>𝐓𝐤 𝐄𝐧𝐭𝐞𝐫𝐭𝐚𝐢𝐧𝐦𝐞𝐧𝐭</a>
👉 <a href='https://t.me/+fMFyfuUUod03NDVl'>𝐓𝐤 𝐄𝐧𝐭𝐞𝐫𝐭𝐚𝐢𝐧𝐦𝐞𝐧𝐭 𝐔𝐩𝐝𝐚𝐭𝐞𝐬</a>
✯ ━━━━━ ✧ ━━━━━ ✯
➠ 𝐇𝐞𝐫𝐞 𝐈𝐬 𝐘𝐨𝐮𝐫 #𝐑𝐞𝐪𝐮𝐞𝐬𝐭
✯ ━━━━━ ✧ ━━━━━ ✯
👋 ʜᴇʏ !!
ᴋɪɴᴅʟʏ ᴀᴅᴅ ʏᴏᴜʀ ꜰʀɪᴇɴᴅꜱ, 
ᴀꜰᴛᴇʀ ɢᴇᴛᴛɪɴɢ ᴍᴏᴠɪᴇꜱ/ꜱᴇʀɪᴇꜱ.
ɪᴛ ᴡɪʟʟ ʜᴇʟᴘ ᴜꜱ ɢʀᴏᴡɪɴɢ 🙏
✯ ━━━━━ ✧ ━━━━━ ✯
⬆️ 𝐔𝐩𝐥𝐨𝐚𝐝𝐞𝐝 𝐁𝐲
👉 <a href='https://t.me/Pr0fess0r99'>𝐏𝐑𝟎𝐅𝐄𝐒𝐒𝟎𝐑 𝟗𝟗</a>
✯ ━━━━━ ✧ ━━━━━ ✯
𝐉𝐨𝐢𝐧 🎗️ 𝐒𝐡𝐚𝐫𝐞 🎗️ 𝐒𝐮𝐩𝐩𝐨𝐫𝐭
✯ ━━━━━ ✧ ━━━━━ ✯</b>"""

    LOGO = """PR0FESS0R 99"""
    
    RESTART_TXT = """
Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ !

📅 Dᴀᴛᴇ : 2023-02-18
⏰ Tɪᴍᴇ : 13:48:05 PM
🌐 Tɪᴍᴇᴢᴏɴᴇ : Asia/Kolkata
🛠️ Bᴜɪʟᴅ Sᴛᴀᴛᴜs: v2.7.1 [ Sᴛᴀʙʟᴇ ]"""
