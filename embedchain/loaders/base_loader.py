from embedchain.helpers.json_serializable import JSONSerializable


class BaseLoader(JSONSerializable):
    def __init__(self):
        pass

    def load_data():
        """
        Implemented by child classes
        """
        raise NotImplementedError("To be implemented by child classes.")
