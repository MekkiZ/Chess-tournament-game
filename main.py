"""system module."""
import logging
from controllers import main

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
