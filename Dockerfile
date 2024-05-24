FROM paiatech/mlgame:10.4.5.3

ADD . /game
WORKDIR /game
RUN apt update -y && apt install -y swig

RUN pip install -r requirements.txt
CMD ["bash"]
