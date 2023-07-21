from helm.proxy.clients.huggingface_client import HuggingFaceHubModelConfig
from helm.benchmark.window_services.huggingface_window_service import HuggingFaceWindowService
from helm.benchmark.window_services.tokenizer_service import TokenizerService


class LlamaWindowService(HuggingFaceWindowService):
    def __init__(self, service: TokenizerService):
        # Tokenizer name hf-internal-testing/llama-tokenizer is taken from:
        # https://huggingface.co/docs/transformers/main/en/model_doc/llama#transformers.LlamaTokenizerFast.example
        model_config = HuggingFaceHubModelConfig(
            namespace="hf-internal-testing", model_name="llama-tokenizer", revision=None
        )
        super().__init__(service, model_config)


class Llama2WindowService(HuggingFaceWindowService):
    # To use the Llama-2 tokenizer:
    #
    # 1. Accept the license agreement: https://ai.meta.com/resources/models-and-libraries/llama-downloads/
    # 2. Request to access the Hugging Face repository: https://huggingface.co/meta-llama/Llama-2-7b
    # 3. Run `huggingface-cli login`
    #
    # If you encounter the following error, complete the above steps and try again:
    #
    #     meta-llama/Llama-2-70b-hf is not a local folder and is not a valid model identifier listed on
    #     'https://huggingface.co/models'
    def __init__(self, service: TokenizerService):
        model_config = HuggingFaceHubModelConfig(namespace="meta-llama", model_name="Llama-2-7b-hf", revision=None)
        super().__init__(service, model_config)

    def max_sequence_length(self) -> int:
        return 4096
