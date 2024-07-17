from core.g_var import Event

class pluginApi:

    def EventRegister(event,function):
        Event.eventMap[event]:list.append(function)