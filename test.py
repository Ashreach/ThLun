from ThLun import ProgressBar, Logger, IO, bprint, Fore, Back, RESET, clear_screen, clear_line, Cursor
import time
import random


import time
from ThLun import Logger, LogLevel, Spinner, Spinners, bprint

# Logger demonstration
logger = Logger('DEBUG')

logger.info("ThLun Library Demo")
logger.warning("Warning message")
logger.debug("Debug information")
logger.critical("Critical error")
logger.trace("Trace details")
logger.error("Error occurred")
logger.success("Operation successful")
logger.log('INFO', "Custom log message")

# Cursor manipulation
print("\n=== Cursor Demo ===")
print("Moving cursor...")
Cursor.up(1)
print("Text inserted above")
Cursor.down(1)

# Progress bars demonstration
logger.info("Starting processes...")
download = ProgressBar(100, width=40, color='BLUE', char='█', empty='░')
install = ProgressBar(50, width=40, color='GREEN', char='▓', empty='░')
backup = ProgressBar(40, width=40, color='YELLOW', char='■', empty='·')

# Simulate different process speeds
while download.current < download.total or install.current < install.total or backup.current < backup.total:
    # Fast process
    if download.current < download.total and random.random() > 0.3:
        download.increment(random.randint(1, 3))
    # Medium process
    if install.current < install.total and random.random() > 0.5:
        install.increment()
    # Slow process
    if backup.current < backup.total and random.random() > 0.7:
        backup.increment()
    
    time.sleep(0.1)

logger.success("All processes completed!")

def print_thlun():
    bprint(
        "[RED]"
"___________.__    .__                \n",
"\__    ___/|  |__ |  |  __ __  ____  \n",
"  |    |   |  |  \|  | |  |  \/    \ \n",
"  |    |   |   Y  \  |_|  |  /   |  \\n",
"  |____|   |___|  /____/____/|___|  /\n",
"                \/                \/ [RESET]"
    )



def print_banner_spinner():
    bprint(
        "[SKY_BLUE1]"
        "███████╗██████╗ ██╗███╗   ██╗███╗   ██╗███████╗██████╗ ███████╗\n"
        "██╔════╝██╔══██╗██║████╗  ██║████╗  ██║██╔════╝██╔══██╗██╔════╝\n"
        "███████╗██████╔╝██║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝███████╗\n"
        "╚════██║██╔═══╝ ██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗╚════██║\n"
        "███████║██║     ██║██║ ╚████║██║ ╚████║███████╗██║  ██║███████║\n"
        "╚══════╝╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚══════╝[RESET]"
    )


def print_banner_logger():
    bprint(
        "[LIGHT_SLATE_BLUE]\n"
        "██╗      ██████╗  ██████╗  ██████╗ ███████╗██████╗ \n"
        "██║     ██╔═══██╗██╔════╝ ██╔════╝ ██╔════╝██╔══██╗\n"
        "██║     ██║   ██║██║  ███╗██║  ███╗█████╗  ██████╔╝\n"
        "██║     ██║   ██║██║   ██║██║   ██║██╔══╝  ██╔══██╗\n"
        "███████╗╚██████╔╝╚██████╔╝╚██████╔╝███████╗██║  ██║\n"
        "╚══════╝ ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝[RESET]"
    )


def print_banner_styles():
    bprint(
        "[GREEN]\n"
        "███████╗████████╗██╗   ██╗██╗     ███████╗███████╗\n"
        "██╔════╝╚══██╔══╝╚██╗ ██╔╝██║     ██╔════╝██╔════╝\n"
        "███████╗   ██║    ╚████╔╝ ██║     █████╗  ███████╗\n"
        "╚════██║   ██║     ╚██╔╝  ██║     ██╔══╝  ╚════██║\n"
        "███████║   ██║      ██║   ███████╗███████╗███████║\n"
        "╚══════╝   ╚═╝      ╚═╝   ╚══════╝╚══════╝╚══════╝[RESET]"
    )


def demo_spinner():
    spinner = Spinner(Spinners.braille, speed=0.07)
    spinner.start("Initializing...")
    time.sleep(1)

    for i in range(1, 6):
        spinner.update(
            spinner=Spinners.circle,
            message=f"Processing step {i}/5...",
        )
        time.sleep(0.7)

    spinner.update(spinner=Spinners.dots, message="Finalizing...", speed=0.05)
    time.sleep(1.5)
    spinner.stop("✓ Complete")


def demo_logger():
    log = Logger(LogLevel.TRACE)
    log.trace("Test trace")
    log.debug("Test debug")
    log.info("Test info")
    log.success("Test success")
    log.warning("Test warning")
    log.error("Test error")
    log.critical("Test critical")


def demo_bprint_styles():
    bprint("[RED]Text for styling...[RESET]")
    bprint("[GOLD1]Text for styling...[RESET]")
    bprint("[HOT_PINK_A]Text for styling...[RESET]")

    bprint("[BG_RED]Text for styling...[RESET]")
    bprint("[BG_GOLD1]Text for styling...[RESET]")
    bprint("[BG_HOT_PINK_A]Text for styling...[RESET]")

    bprint("[DIM]Text for styling...[RESET]")
    bprint("[ITALIC]Text for styling...[RESET]")
    bprint("[UNDERLINE]Text for styling...[RESET]")
    bprint("[REVERSE]Text for styling...[RESET]")


def main():
    print_thlun()
    print_banner_spinner()
    demo_spinner()
    print_banner_logger()
    demo_logger()
    print_banner_styles()
    demo_bprint_styles()


if __name__ == "__main__":
    main()
