from ThLun import ProgressBar, Logger
import time
import random

# Ініціалізація логера
lg = Logger('DEBUG')

lg.info("Thlun")
lg.warning("Warning")
lg.debug("Debug")
lg.critical("Critical")
lg.trace("Trace")
lg.log('INFO', "Info")

# Імітація різних процесів
lg.info("Запуск процесів...")
download = ProgressBar(100, width=40, color='BLUE', char='█', empty='░')
install = ProgressBar(50, width=40, color='GREEN', char='▓', empty='░')
backup = ProgressBar(40, width=40, color='YELLOW', char='■', empty='·')


download_done = install_done = backup_done = False
while download.current < download.total or install.current < install.total or backup.current < backup.total:
    # швидкий процес
    if download.current < download.total and random.random() > 0.3:
        download.increment(random.randint(1, 3))
    # середній процес
    if install.current < install.total and random.random() > 0.5:
        install.increment()
    # повільний процес
    if backup.current < backup.total and random.random() > 0.7:
        backup.increment()
    
    time.sleep(0.1)

lg.success("\nВсі процеси завершено!")