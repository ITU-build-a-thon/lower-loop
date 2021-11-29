# ==================================================================================
#  This SW is developed as part of ITU-5G-AI/ML challenge
#  ITU-ML5G-PS-014: Build-a-thon(PoC) Network resource allocation
#  for emergency management based on closed loop analysis
#  Team : RAN-RIC-xApp
#  Author : Deena Mukundan
#  Description : This file has the main implementation of predictor xApp
# ==================================================================================
FROM frolvlad/alpine-miniconda3
#FROM python:3.7-alpine
# RMR setup
RUN mkdir -p /opt/route/
# copy rmr files from builder image in lieu of an Alpine package
COPY --from=nexus3.o-ran-sc.org:10002/o-ran-sc/bldr-alpine3-rmr:4.0.5 /usr/local/lib64/librmr* /usr/local/lib64/
# rmr_probe replaced health_ck
COPY --from=nexus3.o-ran-sc.org:10002/o-ran-sc/bldr-alpine3-rmr:4.0.5 /usr/local/bin/rmr* /usr/local/bin/
ENV LD_LIBRARY_PATH /usr/local/lib/:/usr/local/lib64
COPY local.rt /opt/route/local.rt
ENV RMR_SEED_RT /opt/route/local.rt

EXPOSE 10000
# sdl needs gcc
RUN apk update && apk add gcc musl-dev bash iproute2 iputils

# Install
RUN pip install gevent
RUN pip install requests
COPY setup.py /tmp
COPY src/ /a1orch
COPY api/ /a1orch
COPY xapp-descriptor/ /a1orch
RUN pip install /tmp
ENV RMR_SRC_ID=service-ricxapp-a1orchxapp-rmr.ricxapp:4560
ENV RMR_VCTL_FILE=/tmp/rmr.v
RUN echo "2" >/tmp/rmr.v

# set  env vars
ENV CONFIG_FILE=/a1orch/config.json
ENV TS_CONTROL_URL=http://localhost:5000/api/echo
# Run
ENV PYTHONUNBUFFERED 1
CMD PYTHONPATH=/a1orch:/usr/lib/python3.7/site-packages/:$PYTHONPATH run-a1orch.py
