FROM shankershawn/python:3
#RUN ["mkdir", "gitrepos"]
#WORKDIR gitrepos
#RUN ["git", "clone", "https://github.com/shankershawn/raspi-piezo.git"]
RUN ["mkdir", "-p", "raspi-piezo/alarms"]

WORKDIR raspi-piezo/alarms

COPY *.py ./

CMD ["alarmMain.py"]

ENTRYPOINT ["python3"]

