from .baseRequest import BaseRequest, Field
from typing import Optional
from pydantic import field_validator as validator, model_validator
from .CustomTaskRequestBase import CustomTaskRequestBase


class BasiliskCustomTaskRequestBase(CustomTaskRequestBase):
    
    type: str = Field(default='CustomTask')
    captchaClass: str = Field(default='Basilisk')
    websiteKey: str = Field()