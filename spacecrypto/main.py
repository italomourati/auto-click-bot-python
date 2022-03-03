import time
from pydoc import importfile

image_click = importfile('./modules/imageclick.py')

WAIT_TIME = 2
WAIT_TIME_LAUNCH = 50
WAIT_TIME_WALLET = 20

CONNECT_WALLET_BTS = './spacecrypto/assets/connect_wallet_bt.PNG'
ICON_SPACE_BTS = './spacecrypto/assets/icon_space_bt.PNG'
PLAY_BTS = './spacecrypto/assets/play_bt.PNG'
SIGN_META_MASK_BT = './spacecrypto/assets/sign_meta_mask_bt.PNG'

def launch_space_crypto():
  image_click('Icon Button', ICON_SPACE_BTS, WAIT_TIME)
  time.sleep(WAIT_TIME_LAUNCH)
  image_click('Connect Wallet Button', CONNECT_WALLET_BTS, WAIT_TIME)
  time.sleep(WAIT_TIME_WALLET)
  image_click('Sign Meta Mask Button', SIGN_META_MASK_BT, WAIT_TIME)
  time.sleep(WAIT_TIME_WALLET)
  image_click('Play Button', PLAY_BTS, WAIT_TIME)

launch_space_crypto()