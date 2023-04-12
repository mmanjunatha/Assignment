FROM python:3.6.4
RUN pip install --no-cache pandas
ARG file=orders.csv
COPY $file task.py /root/
WORKDIR /root/
ENTRYPOINT ["sh", "-c"]
CMD ["python task.py -f $file"]