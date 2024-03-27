from tools.model_config import get_flexibility_config, Flexibility
from tools.model_usage import model_wrapper
from dto.dto_models import BaseCongratRequestDTO, BaseCongratResponseDTO
from tools.model_text_builder import build_input_text_base


def base_congrat_generation_service(request_dto: BaseCongratRequestDTO) -> BaseCongratResponseDTO:
    input_text = build_input_text_base(request_dto)
    max_length = request_dto.max_length

    flexibility = Flexibility(request_dto.flexibility)
    flexibility_config = get_flexibility_config(flexibility)
    top_k, top_p = flexibility_config['top_k'], flexibility_config['top_p']

    generated = model_wrapper.generate(text=input_text, max_length=max_length,
                                       top_k=top_k, top_p=top_p)

    # remove request text
    generated = generated.replace(input_text, '')

    return BaseCongratResponseDTO(request_text=input_text, generated_text=generated)
