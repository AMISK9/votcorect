import os

from telegram import InlineKeyboardMarkup

from keyboard import back_to_menu_keyboard

async def send_biografie(update, context):
    chat_id = update.effective_chat.id

    # Căile către imagini
    image_paths = {
        "intro": "media/images/1.jpg",
        "education": "media/images/7.jpg",
        "politics_1": "media/images/2.jpg",
        "politics_2": "media/images/6.jpg",
        "influential_links": "media/images/3.jpg",
        "international_career": "media/images/4.jpg",
        "conclusion": "media/images/5.jpg",
    }

    # Verificăm dacă toate fișierele există
    for key, path in image_paths.items():
        if not os.path.exists(path):
            print(f"[EROARE] Imaginea lipsește: {path}")
            await context.bot.send_message(
                chat_id=chat_id,
                text=f"Imaginea lipsește pentru secțiunea: {key}",
            )
            return

    # Mesaj 1: Introducere cu titlul integrat + imagine
    with open(image_paths["intro"], "rb") as img:
        await context.bot.send_photo(
            chat_id=chat_id,
            photo=img,
            caption=(
                "*Un candidat „anti-sistem” cu rădăcini adânci în sistemul politic românesc*\n\n"
                "Călin Georgescu, candidat independent în turul al doilea al alegerilor prezidențiale, "
                "își construiește imaginea de om „anti-sistem”. Cu toate acestea, *trecutul său arată legături vechi și adânci* "
                "*cu structurile de putere din România*, încă din anii ’90, iar biografia sa este presărată cu controverse și contradicții."
            ),
            parse_mode="Markdown"
        )

    # Mesaj 2: Educația și oportunitățile exclusive în comunism + imagine
    with open(image_paths["education"], "rb") as img:
        await context.bot.send_photo(
            chat_id=chat_id,
            photo=img,
            caption=(
                "*Educația și accesul la oportunități exclusive în perioada comunistă*\n\n"
                "Înainte de 1990, Călin Georgescu a urmat studii în afara țării, consolidându-și experiența prin "
                "„misiuni” în Regatul Unit și Statele Unite, conform biografiei sale de pe site-ul ONU. Totuși, aceste misiuni "
                "din anii ’80 ridică mari semne de întrebare, având în vedere că, în perioada regimului comunist, *doar persoanele cu "
                "conexiuni în structurile de putere și resurse financiare consistente puteau studia sau călători în afara țării.*"
            ),
            parse_mode="Markdown"
        )

    # Mesaj 3: Implicarea în politica românească + două imagini
    with open(image_paths["politics_1"], "rb") as img:
        await context.bot.send_photo(
            chat_id=chat_id,
            photo=img,
            caption=(
                "*Implicarea în politica românească: între oportunism și controverse*\n\n"
                "După Revoluție, Georgescu a urcat rapid în structurile administrative și politice. În perioada 1992-1996, "
                "a fost consilier al ministrului mediului, fiind implicat în gestionarea problemelor legate de deșeuri. *Presa vremii "
                "menționa însă pasivitatea sa în rezolvarea crizei „afacerii reziduurilor”*, în care *România devenise o destinație "
                "pentru deșeurile Europei de Vest.*"
            ),
            parse_mode="Markdown"
        )
    with open(image_paths["politics_2"], "rb") as img:
        await context.bot.send_photo(
            chat_id=chat_id,
            photo=img,
            caption="Un alt moment cheie al implicării politice a lui Georgescu."
        )

    # Mesaj 4: Legături politice și conflicte de interese + imagine
    with open(image_paths["influential_links"], "rb") as img:
        await context.bot.send_photo(
            chat_id=chat_id,
            photo=img,
            caption=(
                "*Legături strânse cu politicieni influenți*\n\n"
                "De-a lungul carierei, Georgescu a fost asociat cu nume mari din politica românească, precum *Ion Iliescu*, "
                "*Petre Roman*, *Mircea Geoană*, *Ioan Oltean* și *Sorin Frunzăverde*. Aceste conexiuni politice i-au facilitat "
                "*ascensiunea* și i-au oferit acces la resurse strategice. Totodată, presa a relatat că Georgescu folosea o mașină cu "
                "număr diplomatic, o practică rezervată doar celor bine poziționați în structurile de putere."
            ),
            parse_mode="Markdown"
        )

    # Mesaj 5: Cariera internațională + imagine
    with open(image_paths["international_career"], "rb") as img:
        await context.bot.send_photo(
            chat_id=chat_id,
            photo=img,
            caption=(
                "*Cariera internațională: între realitate și speculație*\n\n"
                "Georgescu pretinde că a fost raportor special al ONU între 2011 și 2013, însă Consiliul ONU pentru Drepturile Omului "
                "arată că perioada sa de activitate a fost 2010-2012. Mai mult, *Ministerul Afacerilor Externe din România nu deține* "
                "*documente care să ateste cine l-a propus pentru această funcție.*"
            ),
            parse_mode="Markdown"
        )

    # Mesaj 6: Concluzie + imagine
    with open(image_paths["conclusion"], "rb") as img:
        await context.bot.send_photo(
            chat_id=chat_id,
            photo=img,
            caption=(
                "*Concluzie*\n\n"
                "Călin Georgescu nu este outsider-ul pe care încearcă să îl prezinte publicului. De la accesul privilegiat la studii "
                "în perioada comunistă, până la ascensiunea rapidă în structurile guvernamentale și conexiunile cu politicieni influenți, "
                "*trecutul său demonstrează că face parte din sistemul pe care pretinde că îl combate.*"
            ),
            parse_mode="Markdown",
        )

        # Adăugarea sursei cu hyperlink într-un reply separat
    await context.bot.send_message(
        chat_id=chat_id,
        text=(
            "Surse:\n [Snoop - Rădăcinile PSD-PD-Iliescu ale candidatului Călin Georgescu](https://snoop.ro/radacinile-psd-pd-iliescu-ale-candidatului-calin-georgescu/)\n\n"
            "CV: [Universitate din Pitești](https://www.upit.ro/_document/223510/cv_georgescu_calin.pdf)"
        ),
        parse_mode="Markdown",
        reply_markup=back_to_menu_keyboard()
    )