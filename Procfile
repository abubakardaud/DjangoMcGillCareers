web: gunicorn McGillCSCareers.wsgi --chdir backend --limit-request-line 8188 --log-file -
worker: REMAP_SIGTERM=SIGQUIT celery --workdir backend --app=McGillCSCareers worker --loglevel=info
beat: REMAP_SIGTERM=SIGQUIT celery --workdir backend --app=McGillCSCareers beat -S redbeat.RedBeatScheduler --loglevel=info
