# Default configuration options for block observer.
#
# To override settings add `config.whatever = ...` into `local_config.py`; adding settings *here*
# will often cause git conflicts.
#
# To override things that are specific to mainnet/testnet/etc. add `config.whatever = ...` lines
# into `mainnet.py`/`testnet.py`/etc.


# LMQ RPC endpoint of oxend; can be a unix socket 'ipc:///path/to/oxend.sock' (preferred) or a tcp
# socket 'tcp://127.0.0.1:5678'.  Typically you want this running with admin permission.
# Leave this as None here, and set it for each observer in the mainnet.py/testnet.py/etc. script.
beldexd_rpc = 'ipc://beldex-explorer/testnet.sock'

# Default blocks per page for the index.
blocks_per_page=20
# Maximum blocks per page a user can request
max_blocks_per_page=100

# Some display and/or feature options:
pusher=False
key_image_checker=False
output_key_checker=False
autorefresh_option=True
enable_mixins_details=True

# URLs to networks other than the one we are on:
mainnet_url='https://beldex.explorer'
testnet_url='https://testnet.beldex.explorer'
devnet_url='https://devnet.beldex.explorer'

# Same as above, but these apply if we are on a .beldex URL:
beldexnet_mainnet_url='http://blocks.beldex'
beldexnet_testnet_url='http://testnet.beldex'
beldexnet_devnet_url='http://devnet.kcpyawm9se7trdbzncimdi5t7st4p5mh9i1mg7gkpuubi4k4ku1y.beldex'
