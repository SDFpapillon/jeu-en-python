from datetime import datetime

log = open('log.txt', 'r+', 1)
#log_time = open('log_time.txt', 'r+', 1)

class ecrire_log():

    def ecrire_log(self, texte):
        # log_time.write(str(datetime.now()))
        # log_time.write("\n")
        log.write(str(datetime.now()))
        log.write(texte)
        log.write("\n")
