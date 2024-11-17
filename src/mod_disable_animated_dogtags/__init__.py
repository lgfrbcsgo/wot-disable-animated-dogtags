from gui.battle_control.controllers.dog_tags_ctrl import DogTagsController
from mod_hooking.strategy import override

@override(DogTagsController, "_DogTagsController__onAvatarReady")
def noop(*args, **kwargs):
    pass
