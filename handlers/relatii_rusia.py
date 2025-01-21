from keyboard import back_to_menu_keyboard
import os

async def send_relatii_rusia(update, context):
    chat_id = update.effective_chat.id

    # Căile către imagini
    image_paths = {
        "kremlin": "media/images/8.jpg",  # Prima imagine
        "declasificate": "media/images/9.jpg"  # A doua imagine
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

    # Mesaj 1: Declasificarea informațiilor despre campanie
    await context.bot.send_message(
        chat_id=chat_id,
        text=(
            "*Declasificarea informațiilor despre campanie*\n\n"
            "Președintele Klaus Iohannis a declasificat un set de informații primite de la serviciile de informații, care arată implicarea unui actor statal străin în promovarea lui Călin Georgescu pe platforma TikTok. "
            "Aceste conturi au fost utilizate într-o campanie bine organizată, având ca scop influențarea percepției publice și susținerea unui narativ pro-rus și anti-occidental."
        ),
        parse_mode="Markdown",
    )

    # Mesaj 2: Tiparul campaniilor similare
    await context.bot.send_message(
        chat_id=chat_id,
        text=(
            "*Tiparul campaniilor similare*\n\n"
            "Serviciile de informații au identificat un tipar de campanii similare, orchestrate pentru destabilizarea statelor democratice. "
            "Acestea urmăresc discreditarea parteneriatelor strategice euroatlantice ale României și promovarea unor orientări geopolitice mai apropiate de Rusia."
        ),
        parse_mode="Markdown"
    )

    # Mesaj 3: Exemplu - Ucraina
    with open(image_paths["kremlin"], "rb") as img:
        await context.bot.send_photo(
            chat_id=chat_id,
            photo=img,
            caption=(
                "*Exemplu - Ucraina*\n\n"
                "Un exemplu notabil este campania desfășurată în Ucraina, unde o rețea de conturi false, coordonată din Rusia, a răspândit masiv dezinformări despre războiul din Ucraina. "
                "Aceste conturi au vizat utilizatori din Germania, Franța, Polonia, Israel și Ucraina, urmărind să genereze confuzie și să influențeze opinia publică internațională."
            ),
            parse_mode="Markdown"
        )

    # Mesaj 4: Rolul lui Eugen Sechila
    with open(image_paths["declasificate"], "rb") as img:
        await context.bot.send_photo(
            chat_id=chat_id,
            photo=img,
            caption=(
                "*Rolul lui Eugen Sechila în campanie*\n\n"
                "Eugen Sechila, un fost membru al Legiunii Străine și organizator de tabere paramilitare, este un personaj central în echipa lui Călin Georgescu. "
                "Acesta este implicat activ în Asociația „Gogu Puiu și Haiducii Dobrogei”, o organizație acuzată de neo-legionarism, unde soția sa, Elena Sechila, deține funcția de președinte. "
                "Sechila a strâns semnături pentru candidatura lui Georgescu și l-a însoțit la diverse evenimente publice, contribuind direct la organizarea campaniei."
            ),
            parse_mode="Markdown"
        )

    # Mesaj 5: Documentele declasificate
    await context.bot.send_message(
        chat_id=chat_id,
        text=(
            "*Documentele declasificate*\n\n"
            "Informațiile declasificate indică o campanie orchestrată de un actor statal străin, cu scopul de a influența opinia publică din România în favoarea unui narativ pro-rus. "
            "Aceste documente detaliază legăturile directe dintre echipa lui Georgescu și grupuri externe implicate în dezinformare."
        ),
        parse_mode="Markdown"
    )

    # Mesaj cu linkuri către documentele declasificate
    await context.bot.send_message(
        chat_id=chat_id,
        text=(
            "Documentele declasificate pot fi consultate aici:\n"
            "- [Document CSAT Ministerul Afacerilor Interne](http://www.presidency.ro/files/userfiles/Documente%20CSAT/Document%20CSAT%20MAI.pdf)\n"
            "- [Document CSAT Serviciul de Informații Externe](http://www.presidency.ro/files/userfiles/Documente%20CSAT/Document%20CSAT%20SIE.pdf)\n"
            "- [Document CSAT Serviciul Român de Informații I](http://www.presidency.ro/files/userfiles/Documente%20CSAT/Document%20CSAT%20SRI%20I.pdf)"
            "- [Document CSAT Serviciul Român de Informații II](http://www.presidency.ro/files/userfiles/Documente%20CSAT/Document%20CSAT%20SRI%20II.pdf)\n"
            "- [Document CSAT Serviciul de Telecomunicații Speciale](http://www.presidency.ro/files/userfiles/Documente%20CSAT/Document%20CSAT%20STS.pdf)"
        ),
        parse_mode="Markdown",
        reply_markup=back_to_menu_keyboard()
    )