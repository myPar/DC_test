from dto.dto_models import BaseCongratRequestDTO
import random


patterns = ["Напиши поздравление с '{0}' для {1}:",
            "Сгенерируй поздравление с '{0}' для {1}:",
            "Сделай шикарное поздравление с '{0}' для нашего замечательного {1}:"]


def build_input_text_base(request_dto: BaseCongratRequestDTO):
    name = request_dto.person_name
    holiday = request_dto.holiday_name

    pattern = random.choice(patterns)

    return pattern.format(holiday, name)

