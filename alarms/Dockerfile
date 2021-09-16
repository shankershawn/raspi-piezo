FROM shankershawn/python:3
RUN ["mkdir", "-p", "raspi-piezo/alarms"]
WORKDIR raspi-piezo/alarms
COPY *.py ./
CMD ["alarmMain.py"]
ENTRYPOINT ["python3"]