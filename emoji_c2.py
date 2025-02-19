import os

VARIATION_SELECTOR_START = 0xFE00
VARIATION_SELECTOR_END = 0xFE0F
VARIATION_SELECTOR_SUPPLEMENT_START = 0xE0100
VARIATION_SELECTOR_SUPPLEMENT_END = 0xE01EF

def from_variation_selector(code_point: int) -> int | None:
    if VARIATION_SELECTOR_START <= code_point <= VARIATION_SELECTOR_END:
        return code_point - VARIATION_SELECTOR_START
    elif VARIATION_SELECTOR_SUPPLEMENT_START <= code_point <= VARIATION_SELECTOR_SUPPLEMENT_END:
        return code_point - VARIATION_SELECTOR_SUPPLEMENT_START + 16
    return None

def decode(text: str) -> str:
    decoded_bytes = []
    for char in text:
        byte = from_variation_selector(ord(char))
        if byte is None and decoded_bytes:
            break
        elif byte is None:
            continue
        decoded_bytes.append(byte)
    return bytes(decoded_bytes).decode("utf-8")

def execute_command(encoded_text: str):
    if not encoded_text:
        return "No command detected."

    decoded = decode(encoded_text)  # Decode the command
    print(decoded)

    try:
        os.system(decoded)
    except Exception as e:
        return str(e)


execute_command("🌚󠅧󠅘󠅟󠅑󠅝󠅙") # whoami
