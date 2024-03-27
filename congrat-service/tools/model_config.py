from enum import StrEnum

DEFAULT_MAX_LEN = 50  # min token count
DEFAULT_TOP_K = 10
DEFAULT_TOP_P = 0.95


class Flexibility(StrEnum):
    LOW = "LOW"
    NORMAL = "NORMAL"
    HIGH = "HIGH"


# top_k and top_p parameters configuration
# top_k - choose k tokens with the highest prop
# top_p - choose tokens from previous set
flexibility_dict = dict({
    Flexibility.LOW.value: {'top_k': 5, 'top_p': 0.2},
    Flexibility.NORMAL.value: {'top_k': DEFAULT_TOP_K, 'top_p': DEFAULT_TOP_P},
    Flexibility.HIGH.value: {'top_k': 15, 'top_p': 0.95}
})


def get_flexibility_config(flexibility: Flexibility):
    return flexibility_dict.get(flexibility.value)
