# base image 
FROM python:3.9


#  working directory
WORKDIR /app



# copy
COPY . /app




# run
RUN pip install -r requirement.txt




# port
EXPOSE 5000



# runing cammand

CMD [ "python","./app.py" ] 