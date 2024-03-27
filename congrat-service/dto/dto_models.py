from pydantic import BaseModel, Field, model_validator
from tools.model_config import flexibility_dict, DEFAULT_MAX_LEN, Flexibility


class BaseCongratRequestDTO(BaseModel):
    holiday_name: str = Field(min_length=1)
    person_name: str = Field(min_length=1)
    flexibility: str = Field(default=Flexibility.NORMAL.value)
    max_length: int = Field(default=DEFAULT_MAX_LEN)

    @model_validator(mode='after')
    def check_flexibility(self):
        if self.flexibility not in flexibility_dict.keys():
            raise ValueError(f"'flexibility' should have value from {list(flexibility_dict.keys())}")

        if self.max_length is not None and self.max_length < DEFAULT_MAX_LEN:
            raise ValueError(f"'max_length' can't be less than {DEFAULT_MAX_LEN}")

        return self


class BaseCongratResponseDTO(BaseModel):
    request_text: str = Field(min_length=1)
    generated_text: str = Field(min_length=1)
