# from apscheduler.schedulers.blocking import BlockingScheduler
# import timer,threading
# from deploy import tick

# def foo():
#     tick()
#     threading.Timer(10, foo).start()

# sched = BlockingScheduler()
#
# @sched.scheduled_job('interval', seconds=10)
# def timed_job():
#     tick()
#
# # @sched.scheduled_job('cron', day_of_week='mon-fri', hour=17)
# # def scheduled_job():
# #     print('This job is run every weekday at 5pm.')
#
# sched.start()
