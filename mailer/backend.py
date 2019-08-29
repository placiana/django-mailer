from django.conf import settings
from django.core.mail.backends.base import BaseEmailBackend

from mailer.models import Message

class DbBackend(BaseEmailBackend):

    def send_messages(self, email_messages):
        # allow for a custom batch size
        MESSAGES_BATCH_SIZE = getattr(settings, "MAILER_MESSAGES_BATCH_SIZE", None)

        messages = Message.objects.bulk_create([
            Message(email=email) for email in email_messages
        ], MESSAGES_BATCH_SIZE)

        return len(messages)

# 
# class DbBackend(BaseEmailBackend):
# 
#     def send_messages(self, email_messages):
#         num_sent = 0
#         for email in email_messages:
#             msg = Message()
#             msg.email = email
#             msg.save()
#             num_sent += 1
#         return num_sent
