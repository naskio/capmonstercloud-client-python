from typing import Dict, Union
from pydantic import Field, validator

from .ComplexImageTaskBase import ComplexImageTaskRequestBase
from ..exceptions import NumbersImagesErrors, ZeroImagesErrors, TaskNotDefinedError, ExtraParamsError


class RecognitionComplexImageTaskRequest(ComplexImageTaskRequestBase):
    captchaClass: str = Field(default='recognition')
    metadata: Dict[str, str]

    @validator('metadata')
    def validate_metadata(cls, value):
        if value.get('Task') is None:
            raise TaskNotDefinedError(f'Expect that task will be defined.')
        else:
            return value

    @validator('imagesBase64')
    def validate_images_array(cls, value):
        if value is not None:
            if not isinstance(value, (list, tuple)):
                raise TypeError(f'Expect that type imagesBase64 array will be <list> or <tuple>, got {type(value)}')
            elif len(value) > 18:
                raise NumbersImagesErrors(f'Maximum number of images in list 18, got {len(value)}')
            elif not len(value):
                raise ZeroImagesErrors(f'At least one image base64 expected, got {len(value)}')
            # Check for each element type
            contain_types = [isinstance(x, str) for x in value]
            if not all(contain_types):
                raise TypeError(f'Next images from imagesBase64 array are not string: {contain_types}')
        return value

    def getTaskDict(self) -> Dict[str, Union[str, int, bool]]:
        task = {}
        task['type'] = self.taskType
        task['class'] = self.captchaClass
        task['imagesBase64'] = self.imagesBase64
        task['metadata'] = self.metadata
        return task

    # DISALLOWED FIELDS

    @validator('imagesUrls')
    def validate_urls_array(cls, value):
        if value:
            raise ExtraParamsError(f"imagesUrls is not allowed in this task, got {value}")

    @validator('websiteUrl')
    def validate_website_url(cls, value):
        if value:
            raise ExtraParamsError(f"websiteUrl is not allowed in this task, got {value}")

    @validator('userAgent')
    def validate_user_agent(cls, value):
        if value:
            raise ExtraParamsError(f"userAgent is not allowed in this task, got {value}")
