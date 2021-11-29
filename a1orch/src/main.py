# ==================================================================================
#  This SW is developed as part of ITU-5G-AI/ML challenge
#  ITU-ML5G-PS-014: Build-a-thon(PoC) Network resource allocation
#  for emergency management based on closed loop analysis
#  Team : RAN-RIC-xApp
#  Author : Deena Mukundan
#  Description : This file has the main implementation of predictor xApp
# ==================================================================================


import os
from ricxappframe.xapp_frame import RMRXapp, rmr
from constants import Constants
from a1PolicyInterface import A1PolicyInterface
from log import logger


pred_xapp = ""
pred = ""

def post_init(self):
    """
    Function that runs when xapp initialization is complete
    """
    #self.predict_requests = 0
    logger.debug("calling post_init")
    #schedule.every(1).minutes.do(predict, self)


def pred_default_handler(self, summary, sbuf):
    """
    Function that processes messages for which no handler is defined
    """
    #logger.debug("default handler received message type {}".format(summary[rmr.RMR_MS_MSG_TYPE]))
    logger.debug("default handler received message type {}".format(summary[rmr.RMR_MS_MSG_TYPE]))
    # we don't use rts here; free this
    self.rmr_free(sbuf)



def start(thread=False):
    """
    This is a convenience function that allows this xapp to run in Docker
    for "real" (no thread, real SDL), but also easily modified for unit testing
    (e.g., use_fake_sdl). The defaults for this function are for the Dockerized xapp.
    """
    logger.debug("pred xApp starting")
    global pred_xapp, pred
    fake_sdl = os.environ.get("USE_FAKE_SDL", None)
    pred_xapp = RMRXapp(pred_default_handler, rmr_port=4560, post_init=post_init, use_fake_sdl=bool(fake_sdl))
    logger.debug("pred_xapp created@@@")
    a1_intf = A1PolicyInterface(pred_xapp)
    pred_xapp.register_callback(a1_intf.request_handler,Constants.A1_POLICY_REQ)
    a1_intf.send_a1_policy_query()
    pred_xapp.run(thread)
