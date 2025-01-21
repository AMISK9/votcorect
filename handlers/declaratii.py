import os
from keyboard import back_to_menu_keyboard

async def send_declaratii(update, context):
    chat_id = update.effective_chat.id

    # Căile către video-uri
    video_paths = {
        "intelepciunea_ruseasca": "media/videos/1.mp4",
        "nanochipuri": "media/videos/2.mp4",
        "putin": "media/videos/3.mp4",
        "omul_nu_a_ajuns_pe_luna": "media/videos/4.mp4",
        "lucian_blaga": "media/videos/5.mp4",
    }

    # Verificăm dacă toate fișierele video există
    for key, path in video_paths.items():
        if not os.path.exists(path):
            print(f"[EROARE] Video-ul lipsește: {path}")
            await context.bot.send_message(
                chat_id=chat_id,
                text=f"Video-ul lipsește pentru secțiunea: {key}",
            )
            return

    # 1. Înțelepciunea rusească
    with open(video_paths["intelepciunea_ruseasca"], "rb") as video:
        await context.bot.send_video(
            chat_id=chat_id,
            video=video,
            caption=(
                "*Înțelepciunea rusească*\n\n"
                "Georgescu a susținut că „șansa României este înțelepciunea rusească”, o afirmație controversată care sugerează o orientare pro-Rusia.\n\n"
                "*Refutare:*\n"
                "Înțelepciunea rusească nu poate justifica acțiuni agresive și încălcarea drepturilor omului. România trebuie să-și mențină poziția în cadrul UE și NATO.\n\n"
                "*Sursă:*\n"
                "[Rusia și imperiul rus](https://rm.coe.int/imperiul-rus-fise-de-informare-despre-istoria-romilor/16808b1a79)"
            ),
            parse_mode="Markdown"
        )

    # 2. Nanocipuri în sucuri
    with open(video_paths["nanochipuri"], "rb") as video:
        await context.bot.send_video(
            chat_id=chat_id,
            video=video,
            caption=(
                "*Nanocipuri în sucuri*\n\n"
                "Georgescu a afirmat că sucurile conțin nanocipuri, o teorie nefondată care sugerează un control tehnologic asupra populației.\n\n"
                "*Refutare:*\n"
                "Nu există nicio dovadă științifică sau reglementare care să susțină afirmația că sucurile ar conține nanocipuri. "
                "De asemenea, diferența dintre nanoparticule și nanocipuri este esențială – nanoparticulele sunt un termen general în nanotehnologie, în timp ce nanocipurile sunt concepte neverificate, nefundamentate științific.\n\n"
                "*Sursă:*\n"
                "[Nanotehnologia în industria alimentară](https://www.tiktok.com/@cristian.presura/video/7444191243980066080)"
            ),
            parse_mode="Markdown"
        )

    # 3. Aprecierea pentru Putin
    with open(video_paths["putin"], "rb") as video:
        await context.bot.send_video(
            chat_id=chat_id,
            video=video,
            caption=(
                "*Aprecierea pentru Putin*\n\n"
                "Georgescu a exprimat apreciere pentru Vladimir Putin, un lider care a fost implicat în multiple "
                "controverse internaționale, inclusiv în invadarea Ucrainei și încălcarea drepturilor omului.\n\n"
                "*Refutare:*\n"
                "Vladimir Putin este cunoscut pentru regimul său autoritar și agresiunile externe, iar susținerea unui astfel de lider "
                "este incompatibilă cu valorile democratice ale României.\n\n"
                "*Sursă:*\n"
                "[Politica externă a Rusiei sub Putin](https://www.contributors.ro/politica-externa-rusa-si-originea-lumii-rusesti/)"
            ),
            parse_mode="Markdown"
        )

    # 4. Omul nu a ajuns pe Lună
    with open(video_paths["omul_nu_a_ajuns_pe_luna"], "rb") as video:
        await context.bot.send_video(
            chat_id=chat_id,
            video=video,
            caption=(
                "*Omul nu a ajuns pe Lună*\n\n"
                "Georgescu a susținut că omul nu a ajuns pe Lună, o teorie a conspirației care contrazice dovezile științifice și misiunile spațiale ale NASA.\n\n"
                "*Refutare:*\n"
                "Faptele și dovezile științifice demonstrează că omul a ajuns pe Lună în 1969, iar misiunile Apollo au fost documentate pe larg.\n\n"
                "*Sursă:*\n"
                "[Istoria misiunii Apollo 11](https://www.descopera.ro/istorie/18213655-apollo-11-o-cronologie-a-primei-aselenizari)"
            ),
            parse_mode="Markdown"
        )

    # 5. Lucian Blaga este pe bancnota de 200 RON
    with open(video_paths["lucian_blaga"], "rb") as video:
        await context.bot.send_video(
            chat_id=chat_id,
            video=video,
            caption=(
                "*Lucian Blaga este interzis in Romania*\n\n"
                "Georgescu a afirmat că Lucian Blaga este interzis în România, dar de fapt acesta este pe bancnota de 200 RON și este studiat în școli.\n\n"
                "*Refutare:*\n"
                "Lucian Blaga este una dintre cele mai importante figuri culturale ale României și este onorat pe bancnota de 200 RON și în cadrul educațional românesc.\n\n"
                "*Sursă:*\n"
                "[Lucian Blaga - Cine este?](https://www.libertatea.ro/lifestyle/lucian-blaga-biografie-3404878)"
            ),
            parse_mode="Markdown"
        )

    # Mesaj suplimentar cu sugestia unui website dedicat declarațiilor sale
    await context.bot.send_message(
        chat_id=chat_id,
        text=(
            "Pentru o listă completă a declarațiilor controversate ale lui Călin Georgescu, vizitează website-ul: "
            "(https://www.ceazisgeorgescu.ro)"
        ),
        parse_mode="Markdown",
        reply_markup=back_to_menu_keyboard()
    )
