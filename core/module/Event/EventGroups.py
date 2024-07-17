class EventGroup:
    
    class GUILDS:
        name="GUILDS"
        id=1 << 0

    class GUILD_MEMBERS:
        name="GUILD_MEMBERS"
        id=1 << 1

    class PRIVATE_GUILD_MESSAGES:
        name="PRIVATE_GUILD_MESSAGES"
        id=1 << 9
        type="PRIVATE"

    class GUILD_MESSAGE_REACTIONS:
        name="GUILD_MESSAGE_REACTIONS"
        id=1 << 10

    class DIRECT_MESSAGE:
        name="DIRECT_MESSAGE"
        id=1 << 12

    class GROUP_AND_C2C_EVENT:
        name="GROUP_AND_C2C_EVENT"
        id=1 << 25

    class INTERACTION:
        name="INTERACTION"
        id=1 << 26

    class MESSAGE_AUDIT:
        name="MESSAGE_AUDIT"
        id=1 << 27

    class PRIVATE_FORUMS_EVENT:
        name="PRIVATE_FORUMS_EVENT"
        id=1 << 28
        type="PRIVATE"

    class AUDIO_ACTION:
        name="AUDIO_ACTION"
        id=1 << 29

    class PUBLIC_GUILD_MESSAGES:
        name="PUBLIC_GUILD_MESSAGES"
        id=1 << 30
        type="PUBLIC"