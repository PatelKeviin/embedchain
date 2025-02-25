import os
from typing import Dict, List, Optional, Union

from embedchain.config.vectordb.base import BaseVectorDbConfig
from embedchain.helpers.json_serializable import register_deserializable


@register_deserializable
class ElasticsearchDBConfig(BaseVectorDbConfig):
    def __init__(
        self,
        collection_name: Optional[str] = None,
        dir: Optional[str] = None,
        es_url: Union[str, List[str]] = None,
        **ES_EXTRA_PARAMS: Dict[str, any],
    ):
        """
        Initializes a configuration class instance for an Elasticsearch client.

        :param collection_name: Default name for the collection, defaults to None
        :type collection_name: Optional[str], optional
        :param dir: Path to the database directory, where the database is stored, defaults to None
        :type dir: Optional[str], optional
        :param es_url: elasticsearch url or list of nodes url to be used for connection, defaults to None
        :type es_url: Union[str, List[str]], optional
        :param ES_EXTRA_PARAMS: extra params dict that can be passed to elasticsearch.
        :type ES_EXTRA_PARAMS: Dict[str, Any], optional
        """
        # self, es_url: Union[str, List[str]] = None, **ES_EXTRA_PARAMS: Dict[str, any]):
        self.ES_URL = es_url or os.environ.get("ELASTICSEARCH_URL")
        if not self.ES_URL:
            raise AttributeError(
                "Elasticsearch needs a URL attribute, "
                "this can either be passed to `ElasticsearchDBConfig` or as `ELASTICSEARCH_URL` in `.env`"
            )
        self.ES_EXTRA_PARAMS = ES_EXTRA_PARAMS
        # Load API key from .env if it's not explicitly passed.
        # Can only set one of 'api_key', 'basic_auth', and 'bearer_auth'
        if (
            not self.ES_EXTRA_PARAMS.get("api_key")
            and not self.ES_EXTRA_PARAMS.get("basic_auth")
            and not self.ES_EXTRA_PARAMS.get("bearer_auth")
            and not self.ES_EXTRA_PARAMS.get("http_auth")
        ):
            self.ES_EXTRA_PARAMS["api_key"] = os.environ.get("ELASTICSEARCH_API_KEY")
        super().__init__(collection_name=collection_name, dir=dir)
