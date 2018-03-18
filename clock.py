# from apscheduler.schedulers.blocking import BlockingScheduler
# from deploy import tick


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
