from dify_plugin import ToolProvider


class NoodleProvider(ToolProvider):
    def validate_credentials(self, credentials: dict) -> None:
        return None
