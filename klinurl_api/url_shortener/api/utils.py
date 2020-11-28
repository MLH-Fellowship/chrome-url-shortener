import random
import string
from url_shortener.models import Author

ALPHANUMERIC_CHARS = string.ascii_lowercase + string.digits + string.ascii_uppercase
STRING_LENGTH = 5

#function that generates a random string
def create_shortened_url(chars=ALPHANUMERIC_CHARS, length=STRING_LENGTH):
    return "".join(random.choice(chars) for _ in range(length))

request_has_cookie = False
def get_or_create_clientid(request, random_chars):  
    if 'client_id' in request.COOKIES:
        request_has_cookie = True
        client_id = request.COOKIES['client_id']
        return Author.objects.get(client_id=client_id)
    else:
        return Author.create(random_chars)

def set_cookie(request, response, client_id):
    if request_has_cookie:
       print(request.COOKIES['client_id'])
    else:
        response.set_cookie('client_id', client_id, max_age=31556952)