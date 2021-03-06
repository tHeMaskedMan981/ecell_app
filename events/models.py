from uuid import uuid4
from django.db import models
from common.v1.utils.helpers import get_url_friendly
from common.models import LifeTimeTrackingModel, ActiveModel
from venue.models import Venue
# from user.models import User

COMPETITIONS = 'competitions'
NETWORKING = 'networking'
SPEAKER = 'speaker'
OTHERS = 'others'
EVENT_CHOICES = (
	(COMPETITIONS, 'competitions'),
	(NETWORKING, 'networking'),
	(SPEAKER, 'speaker'),
	(OTHERS, 'others')
)
DAY1 = 'day1'
DAY2 = 'day2'
DAY_CHOICES = (
	(DAY1, 'day1'),
	(DAY2, 'day2'),

)

class Event(ActiveModel):
	# id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
	event_id = models.AutoField(primary_key=True)
	str_id = models.CharField(max_length=58, editable=False, null=True)
	# time_of_creation = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=50)
	description = models.TextField(blank=True)
	image_url = models.URLField(blank=True, null=True)
	website_url = models.URLField(blank=True, null=True)
	speaker = models.CharField(max_length=50, blank=True, null=True)
	speaker_image_url = models.URLField(blank=True, null=True)
	speaker_website_url = models.URLField(blank=True, null=True)
	# date = models.DateTimeField(blank=True, null=True)
	day = models.CharField(max_length=200, default=DAY1, choices=DAY_CHOICES)
	start_time = models.TimeField(blank=True, null=True)
	# venue = models.OneToOneField(Venue, blank=True, null=True, on_delete=models.CASCADE())
	venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.SET_NULL)
	venue_name = models.CharField(max_length=500, blank=True, null=True, default=None, editable=False)
	venue_url = models.CharField(max_length=500, blank=True, null=True, default=None, editable=False)
	all_day = models.BooleanField(default=False)
	# venues = models.ManyToManyField('locations.Location', related_name='events', blank=True)
	# followers = models.ManyToManyField('users.UserProfile', through='UserEventStatus',
	# 									related_name='followed_events', blank=True)
	archived = models.BooleanField(default=False)
	event_type = models.CharField(max_length=200, default=COMPETITIONS, choices=EVENT_CHOICES)
	updated = models.BooleanField(default=False)
	highlight = models.BooleanField(default=False)




		

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		self.venue_url = self.venue.url
		self.venue_name = self.venue.name
		super(Event, self).save(*args, **kwargs)

	class Meta:
		verbose_name = "Event"
		verbose_name_plural = "Events"
		ordering = ('start_time',)

# class UserEventStatus(models.Model):
#     """Associates a User and an Event, describing probabilty of attending.

#     Attributes:
#         `status` - probability of attending the event,
#         e.g. 0 - not going, 1 - interested, 2 - going etc.
#     """

#     id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
#     time_of_creation = models.DateTimeField(auto_now_add=True)

#     # Cascading on delete is delibrate here, since the entry
#     # makes no sense if the user or event gets deleted
#     user = models.ForeignKey('users.UserProfile', on_delete=models.CASCADE,
#                              default=uuid4, related_name='ues')
#     event = models.ForeignKey(Event, on_delete=models.CASCADE,
#                               default=uuid4, related_name='ues')

#     status = models.IntegerField(default=0)

#     class Meta:
#         verbose_name = "User-Event Status"
#         verbose_name_plural = "User-Event Statuses"
		