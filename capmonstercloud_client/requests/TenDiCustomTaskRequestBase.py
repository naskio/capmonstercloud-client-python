from .baseRequest import BaseRequest, Field
from typing import Optional
from pydantic import field_validator as validator, model_validator
from .CustomTaskRequestBase import CustomTaskRequestBase


class TenDiCustomTaskRequestBase(CustomTaskRequestBase):
    
    type: str = Field(default='CustomTask')
    captchaClass: str = Field(default='TenDI')
    websiteKey: str = Field()