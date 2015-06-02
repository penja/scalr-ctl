__author__ = 'shaitanich'
__doc__ = 'Event management'


from scalrtools import commands


name = "event"
enabled = True


def callback(*args, **kwargs):
    """
    print('in event module')
    print(args)
    print(kwargs)
    """
    pass


class Event(commands.SubCommand):
    pass


class ListEvents(Event):
    name = "list"
    route = "/events/"
    method = "get"
    enabled = True


class RetrieveEvent(Event):
    name = "retrieve"
    route = "/events/{eventId}/"
    method = "get"
    enabled = True


class CreateEvent(Event):
    name = "create"
    route = "/events/"
    method = "post"
    enabled = True


class ChangeEventAttrs(Event):
    name = "change-attributes"
    route = "/events/{eventId}/"
    method = "patch"
    enabled = True


class DeleteEvent(Event):
    name = "delete"
    route = "/events/{eventId}/"
    method = "delete"
    enabled = True