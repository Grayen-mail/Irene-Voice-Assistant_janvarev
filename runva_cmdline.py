import traceback

from vacore import VACore
import time
import logging

logger = logging.getLogger(__name__)

# ------------------- main loop ------------------
if __name__ == "__main__":
    cmd_core = VACore()
    cmd_core.init_with_plugins()
    print("Command-line interface for VoiceAssistantCore.")

    # почему бы сразу не отладить какую-то команду?
    time.sleep(0.5) # небольшой таймаут
    cmd = "привет"
    try:
        cmd_core.execute_next(cmd,cmd_core.context)
    except Exception as e:
        if cmd == "привет":
            print("Ошибка при запуске команды 'привет'. Скорее всего, проблема с TTS.")
        # import traceback
        # traceback.print_exc()
        logger.exception(e)


    exit(0) # если нужно - закомментируйте и можно будет работать с командной строкой

    print("Enter command (user text like 'привет') or 'exit'")
    while True:
        try:
            cmd = input("> ")
            if cmd == "exit":
                break
        except Exception as e:
            logger.exception(e)

        cmd_core.execute_next(cmd,cmd_core.context)