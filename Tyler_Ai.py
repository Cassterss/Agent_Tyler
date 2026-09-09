from wake import wake_up
from recording import record_command, deleted
from whisper_ai import speak_to_text
from speech import chose_things
classes = {
    "OPEN_BROWSER":0,
    "CLOSE_BROWSER":1,
    "VPN_ON ":2,
    "VPN_OFF":3,
    "OPEN_CHATGPT":4,
    "OPEN_YOUTUBE":5,
    "SHOW_RAM_USAGE":6,
    "OPEN_TELEGRAM":7,
    "SLEEP_PC":8,
    "SHOW_VPN_PING":9,
    "SHOW_DISK_C_FREE":10,
    "SHOW_CPU_USAGE":11,
    "SHOW_GPU_USAGE":12,
    "OPEN_PC_MENU":13,
    "OPEN_DISCORD":14,
    "OTHER":15,

}
while True:
    wake = wake_up()
    if wake == True:
        audio = record_command()
        text = speak_to_text(audio)
        text = text.lower()
        text = text.replace("тайлер", "")
        text = text.replace(",", "")
        text = text.replace(".", "")
        text = text.strip()
        deleted(audio)
        thing_is = chose_things(text)
        if thing_is == 0:
            print("Браузер открыт")
        elif thing_is == 1:
            print("Браузер закрыт")
        elif thing_is == 2:
            print("Впн включен")
        elif thing_is == 3:
            print("Впн выключен")
        elif thing_is == 4:
            print("Чат гпт окрыт")
        elif thing_is == 5:
            print("ютуб открыт")
        elif thing_is == 6:
            print("оперотивка показана")
        elif thing_is == 7:
            print("телега открыта")
        elif thing_is == 8:
            print("Пк во сне")
        elif thing_is == 9:
            print("смотреть пинг впн")
        elif thing_is == 10:
            print("Диск память")
        elif thing_is == 11:
            print("проц показан")
        elif thing_is == 12:
            print("видюха показана")
        elif thing_is == 13:
            print("инфа о пк")
        elif thing_is == 14:
            print("дискорд открыт")
        elif thing_is == 15:
            None

            

