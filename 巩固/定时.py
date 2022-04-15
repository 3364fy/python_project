import schedule
import time
def job(message='stuff'):
    print("I'm working on:", message)
schedule.every(10).minutes.do(job)
schedule.every(5).to(10).days.do(job)
schedule.every().hour.do(job, message='things')
schedule.every().day.at("10:30").do(job)
while True:
    schedule.run_pending()
    time.sleep(1)