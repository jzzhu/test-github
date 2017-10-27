FROM python
RUN pip3 install behave
RUN pip3 install selenium


WORKDIR /opt/functional_tests

ENTRYPOINT ["behave", "--lang", "zh-CN"]