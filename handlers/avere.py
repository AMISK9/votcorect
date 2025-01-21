import os
from keyboard import back_to_menu_keyboard

async def send_avere(update, context):
    chat_id = update.effective_chat.id

    # Căile către imagini
    image_paths = {
        "vanzare_corbeanca": "media/images/c.png",
        "investitii_austria": "media/images/a.png",
        "vila_alland": "media/images/d.png",
        "achizitii_romania": "media/images/b.jpeg",
        "concluzii": "media/images/e.jpeg",
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

    # Mesaj 1: Vânzarea vilei din Corbeanca
    with open(image_paths["vanzare_corbeanca"], "rb") as img:
        await context.bot.send_photo(
            chat_id=chat_id,
            photo=img,
            caption=(
                "*Vânzarea vilei din Corbeanca: începutul primului milion*\n\n"
                "În 2011, *familia Georgescu a vândut o vilă din Corbeanca pentru aproape 1 milion de euro.* "
                "Cumpărătorul, Husein Ozghen, era un om de afaceri apropiat de *gruparea Mazăre-Constantinescu*, "
                "binecunoscută pentru corupție, retrocedări ilegale și afaceri dubioase pe litoralul românesc."
            ),
            parse_mode="Markdown"
        )

    # Mesaj 2: Investițiile în Austria
    with open(image_paths["investitii_austria"], "rb") as img:
        await context.bot.send_photo(
            chat_id=chat_id,
            photo=img,
            caption=(
                "*Investițiile în Austria: bani din România, vile pe coline*\n\n"
                "După vânzările din România, *familia Georgescu a început o serie de investiții imobiliare în Austria.* "
                "Prima achiziție, realizată în iunie 2011, a fost un *apartament în apropierea Vienei, pentru 110.000 de euro.* "
                "Clădirea a fost ulterior demolată, iar pe teren a fost construită *o vilă nouă.*"
            ),
            parse_mode="Markdown"
        )

    # Mesaj 3: Vila din Alland
    with open(image_paths["vila_alland"], "rb") as img:
        await context.bot.send_photo(
            chat_id=chat_id,
            photo=img,
            caption=(
                "*Vila din Alland*\n\n"
                "În noiembrie 2011, *familia Georgescu a cumpărat o vilă în Alland pentru 410.000 de euro.* "
                "În 2017, *aceasta a fost vândută pentru 950.000 de euro*, aproape dublu față de prețul de achiziție. "
                "Aceste tranzacții imobiliare au marcat apogeul investițiilor lor în Austria."
            ),
            parse_mode="Markdown"
        )

    # Mesaj 4: Întoarcerea în România și achizițiile recente
    with open(image_paths["achizitii_romania"], "rb") as img:
        await context.bot.send_photo(
            chat_id=chat_id,
            photo=img,
            caption=(
                "*Întoarcerea în România și achizițiile recente*\n\n"
                "În 2022, *familia Georgescu a achiziționat o proprietate de 3900 mp în Brașov și un teren de 7000 mp în Argeș.* "
                "*În octombrie 2024, au cumpărat o vilă în Mogoșoaia pentru 560.000 de euro*, o sumă semnificativ mai mare decât cea declarată în conturile lor bancare oficiale."
            ),
            parse_mode="Markdown"
        )

    # Mesaj 5: Concluzii
    with open(image_paths["concluzii"], "rb") as img:
        await context.bot.send_photo(
            chat_id=chat_id,
            photo=img,
            caption=(
                "*Concluzii*\n\n"
                "Deși *Călin Georgescu susține public că „a locuit cu chirie” și abia acum „a reușit să-și cumpere o casă în România”*, "
                "dovezile arată un istoric de tranzacții profitabile și legături cu grupări controversate. "
                "În plus, *declarația sa că a cheltuit 0 lei pentru campania prezidențială ridică întrebări serioase despre sursele de finanțare ale activităților sale politice.*"
            ),
            parse_mode="Markdown"
        )

    # Adăugarea sursei cu hyperlink într-un reply separat
    await context.bot.send_message(
        chat_id=chat_id,
        text=(
            "Surse:\n[RISE Project - Cum a făcut Călin Georgescu primul milion](https://www.riseproject.ro/investigations/uncategorized/cum-a-facut-calin-georgescu-primul-milion-cu-gruparea-mazare/?tztc=1)\n\n"
            "Declaratie de avere: [Biroul Electoral Central](https://prezidentiale2024.bec.ro/wp-content/uploads/2024/10/da_Georgescu.pdf)"
        ),
        parse_mode = "Markdown",
        reply_markup = back_to_menu_keyboard())

