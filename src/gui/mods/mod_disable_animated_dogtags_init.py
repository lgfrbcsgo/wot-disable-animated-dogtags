from debug_utils import LOG_CURRENT_EXCEPTION


def init():
    try:
        import mod_disable_animated_dogtags
    except Exception:
        LOG_CURRENT_EXCEPTION()


def fini():
    pass
