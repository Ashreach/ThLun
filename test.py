from ThLun import ProgressBar, Logger
import time
import random

# Ініціалізація логера
logger = Logger('DEBUG')

# Імітація різних процесів
logger.info("Запуск процесів...")
download = ProgressBar(100, width=40, color='BLUE', char='█', empty='░')
install = ProgressBar(50, width=40, color='GREEN', char='▓', empty='░')
backup = ProgressBar(75, width=40, color='YELLOW', char='■', empty='·')

# Симуляція процесів з різною швидкістю
download_done = install_done = backup_done = False

while download.current < download.total or install.current < install.total or backup.current < backup.total:
    # Download - швидкий процес
    if download.current < download.total and random.random() > 0.3:
        download.increment(random.randint(1, 3))
        if download.current == download.total and not download_done:
            logger.success("Download завершено!")
            download_done = True
    
    # Install - середній процес
    if install.current < install.total and random.random() > 0.5:
        install.increment()
        if install.current == install.total and not install_done:
            logger.success("Install завершено!")
            install_done = True
    
    # Backup - повільний процес
    if backup.current < backup.total and random.random() > 0.7:
        backup.increment()
        if backup.current == backup.total and not backup_done:
            logger.success("Backup завершено!")
            backup_done = True
    
    time.sleep(0.1)

logger.info("Всі процеси завершено!")