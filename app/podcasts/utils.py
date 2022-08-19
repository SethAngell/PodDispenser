from django.core.exceptions import ValidationError


def validate_show_art_is_optimally_sized(image):
    def validator(image):
        error = False
        if image.width != 3000:
            error = True
        if image.height != image.width:
            error = True
        if error:
            raise ValidationError(
                ["Show art should be a square image (3000px by 3000px)"]
            )

    return validator
