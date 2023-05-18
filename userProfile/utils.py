import re
from typing import Optional, Match


def validPhoneNumber(number: str) -> Optional[Match[str]]:
    pattern = re.compile("[5-9][0-9]{9}")
    return pattern.match(number)
