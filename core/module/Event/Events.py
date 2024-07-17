from core.module.Event.EventGroups import EventGroup

class Event:

    class GUILD_CREATE:
        name="GUILD_CREATE"
        group=EventGroup.GUILDS

    class GUILD_UPDATE:
        name="GUILD_UPDATE"
        group=EventGroup.GUILDS

    class GUILD_DELETE:
        name="GUILD_DELETE"
        group=EventGroup.GUILDS

    class CHANNEL_CREATE:
        name="CHANNEL_CREATE"
        group=EventGroup.GUILDS
    
    class CHANNEL_UPDATE:
        name="CHANNEL_UPDATE"
        group=EventGroup.GUILDS

    class CHANNEL_DELETE:
        name="CHANNEL_DELETE"
        group=EventGroup.GUILDS

    class GUILD_MEMBER_ADD:
        name="GUILD_MEMBER_ADD"
        group=EventGroup.GUILD_MEMBERS

    class GUILD_MEMBER_UPDATE:
        name="GUILD_MEMBER_UPDATE"
        group=EventGroup.GUILD_MEMBERS
    
    class GUILD_MEMBER_REMOVE:
        name="GUILD_MEMBER_REMOVE"
        group=EventGroup.GUILD_MEMBERS
    
    class MESSAGE_CREATE:
        name="MESSAGE_CREATE"
        group=EventGroup.PRIVATE_GUILD_MESSAGES
    
    class MESSAGE_DELETE:
        name="MESSAGE_DELETE"
        group=EventGroup.PRIVATE_GUILD_MESSAGES
    
    class MESSAGE_REACTION_ADD:
        name="MESSAGE_REACTION_ADD"
        group=EventGroup.GUILD_MESSAGE_REACTIONS

    class MESSAGE_REACTION_REMOVE:
        name="MESSAGE_REACTION_REMOVE"
        group=EventGroup.GUILD_MESSAGE_REACTIONS

    class DIRECT_MESSAGE_CREATE:
        name="DIRECT_MESSAGE_CREATE"
        group=EventGroup.DIRECT_MESSAGE

    class DIRECT_MESSAGE_DELETE:
        name="DIRECT_MESSAGE_DELETE"
        group=EventGroup.DIRECT_MESSAGE

    class C2C_MESSAGE_CREATE:
        name="C2C_MESSAGE_CREATE"
        group=EventGroup.GROUP_AND_C2C_EVENT

    class FRIEND_ADD:
        name="FRIEND_ADD"
        group=EventGroup.GROUP_AND_C2C_EVENT

    class FRIEND_DEL:
        name="FRIEND_DEL"
        group=EventGroup.GROUP_AND_C2C_EVENT

    class C2C_MSG_REJECT:
        name="C2C_MSG_REJECT"
        group=EventGroup.GROUP_AND_C2C_EVENT

    class C2C_MSG_RECEIVE:
        name="C2C_MSG_RECEIVE"
        group=EventGroup.GROUP_AND_C2C_EVENT

    class GROUP_AT_MESSAGE_CREATE:
        name="GROUP_AT_MESSAGE_CREATE"
        group=EventGroup.GROUP_AND_C2C_EVENT

    class GROUP_ADD_ROBOT:
        name="GROUP_ADD_ROBOT"
        group=EventGroup.GROUP_AND_C2C_EVENT

    class GROUP_DEL_ROBOT:
        name="GROUP_DEL_ROBOT"
        group=EventGroup.GROUP_AND_C2C_EVENT

    class GROUP_MSG_REJECT:
        name="GROUP_MSG_REJECT"
        group=EventGroup.GROUP_AND_C2C_EVENT

    class GROUP_MSG_RECEIVE:
        name="GROUP_MSG_RECEIVE"
        group=EventGroup.GROUP_AND_C2C_EVENT

    class INTERACTION_CREATE:
        name="INTERACTION_CREATE"
        group=EventGroup.INTERACTION

    class MESSAGE_AUDIT_PASS:
        name="MESSAGE_AUDIT_PASS"
        group=EventGroup.MESSAGE_AUDIT

    class MESSAGE_AUDIT_REJECT:
        name="MESSAGE_AUDIT_REJECT"
        group=EventGroup.MESSAGE_AUDIT

    class FORUM_THREAD_CREATE:
        name="FORUM_THREAD_CREATE"
        group=EventGroup.PRIVATE_FORUMS_EVENT

    class FORUM_THREAD_UPDATE:
        name="FORUM_THREAD_UPDATE"
        group=EventGroup.PRIVATE_FORUMS_EVENT

    class FORUM_THREAD_DELETE:
        name="FORUM_THREAD_DELETE"
        group=EventGroup.PRIVATE_FORUMS_EVENT

    class FORUM_POST_CREATE:
        name="FORUM_POST_CREATE"
        group=EventGroup.PRIVATE_FORUMS_EVENT

    class FORUM_POST_DELETE:
        name="FORUM_POST_DELETE"
        group=EventGroup.PRIVATE_FORUMS_EVENT

    class FORUM_REPLY_CREATE:
        name="FORUM_REPLY_CREATE"
        group=EventGroup.PRIVATE_FORUMS_EVENT

    class FORUM_REPLY_DELETE:
        name="FORUM_REPLY_DELETE"
        group=EventGroup.PRIVATE_FORUMS_EVENT

    class FORUM_PUBLISH_AUDIT_RESULT:
        name="FORUM_PUBLISH_AUDIT_RESULT"
        group=EventGroup.PRIVATE_FORUMS_EVENT

    class AUDIO_START:
        name="AUDIO_START"
        group=EventGroup.AUDIO_ACTION

    class AUDIO_FINISH:
        name="AUDIO_FINISH"
        group=EventGroup.AUDIO_ACTION

    class AUDIO_ON_MIC:
        name="AUDIO_ON_MIC"
        group=EventGroup.AUDIO_ACTION

    class AUDIO_OFF_MIC:
        name="AUDIO_OFF_MIC"
        group=EventGroup.AUDIO_ACTION

    class AT_MESSAGE_CREATE:
        name="AT_MESSAGE_CREATE"
        group=EventGroup.PUBLIC_GUILD_MESSAGES

    class PUBLIC_MESSAGE_DELETE:
        name="PUBLIC_MESSAGE_DELETE"
        group=EventGroup.PUBLIC_GUILD_MESSAGES