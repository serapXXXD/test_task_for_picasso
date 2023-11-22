from django.core.exceptions import ValidationError
import magic

mime = magic.Magic(mime=True)


def vaildate_file_types(file):
    allowed_types = ['image/jpeg', 'image/png', 'application/pdf', 'text/plain']
    file_type = mime.from_buffer(file.read(1024))

    if file_type not in allowed_types:
        raise ValidationError('Недопустимый тип файла')

    file.seek(0)
    return file
