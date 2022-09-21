"""system module."""
import logging
from controller import main

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
