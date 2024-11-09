from  django.dispatch import receiver

from hospital.api.models import Visit, Notification , Doctor
from django.db.models.signals import post_save, pre_save , pre_delete


@receiver(post_save , sender=Visit)
def notify_on_new_visit(sender, instance , created , **kwargs):
    if created:
        Notification.objects.create(
            sender =instance.patient.user,
            recipient =instance.schedule.doctor.user,
            message =f"Новый визит запланирован на {instance.schedule.timestamp_start}.",
            notification_type =Notification.VISIT_CREATED
        )


@receiver(pre_save , sender=Visit)
def notify_on_cancelled_visit(sender, instance  , **kwargs):
    if instance.status == Visit.CANCELLED:
        Notification.objects.create(
            sender =instance.patient.user,
            recipient =instance.schedule.doctor.user,
            message =f"Визит отменен",
            notification_type =Notification.VISIT_CANCELLED
        )



