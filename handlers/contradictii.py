import os
from keyboard import back_to_menu_keyboard

async def send_contradictii(update, context):
    chat_id = update.effective_chat.id

    # Căile către video-uri
    video_paths = {
        "nato": "media/videos/6.mp4",
        "ue": "media/videos/7.mp4"
    }

    # Verificăm dacă fișierele video există
    for key, path in video_paths.items():
        if not os.path.exists(path):
            print(f"[EROARE] Video-ul lipsește: {path}")
            await context.bot.send_message(
                chat_id=chat_id,
                text=f"Video-ul lipsește pentru secțiunea: {key}",
            )
            return

    # 1. Mesajul care contrazice NATO și UE
    with open(video_paths["nato"], "rb") as video:
        await context.bot.send_video(
            chat_id=chat_id,
            video=video,
            caption=(
                "*Contrazicerea: NATO și siguranța României*\n\n"
                "Călin Georgescu a spus la un moment dat că *„nu ne interesează NATO, pentru ce să stai într-un club care nu acordă siguranța țării tale?”*. "
                "Apoi a venit și a afirmat că *„Am fost acuzat că vreau să scot România din NATO și din UE. Fals! Nu am spus acest lucru niciodată!”*.\n\n"
                "\n\n"
                "*Declarațiile sunt contradictorii și confuze!* Pe de-o parte, Georgescu susține că NATO nu ar oferi siguranță, "
                "dar pe de altă parte afirmă că nu vrea să scoată România din NATO.\n\n"
                "*Refutare:*"
                "\n*NATO este o alianță defensivă crucială pentru România și asigură siguranța națională. Alianța garantează protecția împotriva oricăror amenințări externe.* "
                "România beneficiază de protecție extinsă datorită apartenenței la NATO, iar această siguranță nu poate fi pusă la îndoială."
            ),
            parse_mode="Markdown"
        )

    # 2. Mesajul pro-UE și contra Rusiei
    with open(video_paths["ue"], "rb") as video:
        await context.bot.send_video(
            chat_id=chat_id,
            video=video,
            caption=(
                "*Contrazicerea: Uniunea Europeană și legăturile cu Rusia*\n\n"
                "Călin Georgescu a afirmat în trecut că *„șansa României este în înțelepciunea rusească”* și că *„economia a scăzut de când suntem în UE”*. "
                "Mai târziu, s-a contrazis și a spus că *„nu am nicio legătură cu Rusia”*.\n\n"
                "\n\n"
                "Într-o parte a declarațiilor sale, *Georgescu susține că „economia a scăzut de când suntem în UE” și propune înțelepciunea rusească. "
                "Mai apoi, spune că nu are nicio legătură cu Rusia și se distanțează de afirmațiile anterioare.*"
                "\n\n"
                "*Refutare:*"
                "\n*Economia României a crescut semnificativ în cadrul Uniunii Europene. Statisticile economice arată o dezvoltare constantă, iar țara noastră nu a fost niciodată mai prosperă.* "
                "De asemenea, Uniunea Europeană a adus beneficii majore în termeni de infrastructură, piețe de export și dezvoltarea standardelor de viață."
            ),
            parse_mode="Markdown",
            reply_markup=back_to_menu_keyboard()
        )

