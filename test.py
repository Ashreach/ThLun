import time
import random

from ThLun import (
    ProgressBar,
    LogLevel,
    Spinner,
    Spinners,
    Logger,
    bprint,
)

def demo_progressbar():
    download = ProgressBar(100, width=40, color="BLUE", char="█", empty="░")
    install = ProgressBar(50, width=40, color="GREEN", char="▓", empty="░")
    backup = ProgressBar(40, width=40, color="YELLOW", char="■", empty="·")

    while (
        download.current < download.total
        or install.current < install.total
        or backup.current < backup.total
    ):
        if download.current < download.total and random.random() > 0.3:
            download.increment(random.randint(1, 3))
        if install.current < install.total and random.random() > 0.5:
            install.increment()
        if backup.current < backup.total and random.random() > 0.7:
            backup.increment()

        time.sleep(0.1)


def print_thlun():
    bprint(
        "[RED]\n"
        "___________.__    .__                \n"
        "\\__    ___/|  |__ |  |  __ __  ____  \n"
        "  |    |   |  |  \\|  | |  |  \\/    \\ \n"
        "  |    |   |   Y  \\  |_|  |  /   |  \\\n"
        "  |____|   |___|  /____/____/|___|  /\n"
        "                \\/                \\/ [RESET]"
    )


def print_banner_progressbar():
    bprint(
        "[LIGHT_SLATE_BLUE]\n",
        "██████╗ ██████╗  ██████╗  ██████╗ ██████╗ ███████╗███████╗███████╗    ██████╗  █████╗ ██████╗ \n",
        "██╔══██╗██╔══██╗██╔═══██╗██╔════╝ ██╔══██╗██╔════╝██╔════╝██╔════╝    ██╔══██╗██╔══██╗██╔══██╗\n",
        "██████╔╝██████╔╝██║   ██║██║  ███╗██████╔╝█████╗  ███████╗███████╗    ██████╔╝███████║██████╔╝\n",
        "██╔═══╝ ██╔══██╗██║   ██║██║   ██║██╔══██╗██╔══╝  ╚════██║╚════██║    ██╔══██╗██╔══██║██╔══██╗\n",
        "██║     ██║  ██║╚██████╔╝╚██████╔╝██║  ██║███████╗███████║███████║    ██████╔╝██║  ██║██║  ██║\n",
        "╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝[RESET]",
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
    print_banner_progressbar()
    demo_progressbar()
    print_banner_logger()
    demo_logger()
    print_banner_styles()
    demo_bprint_styles()


if __name__ == "__main__":
    main()
