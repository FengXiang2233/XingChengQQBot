from core.g_var import Event

class pluginApi:

    def EventRegister(event,function):
        Event.eventMap[event].append(function)