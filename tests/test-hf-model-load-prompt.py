

from llmware.models import ModelCatalog
from llmware.prompts import Prompt

#   sample code and basic 'test' to illustrate the change in streamlining HF model loading into prompts


def test_load_hf_model_in_prompt(model_name):

    # streamlined the method structure so that loading HF model is parallel with other models

    # for example: to load a gpt-4 model into a prompt - NO CHANGE
    prompter = Prompt().load_model("gpt-4")

    # HF Model - "OLD WAY" - previously, to load a HF model into a prompt required an explicit invocation of the model
    # ... and several lines of code that did not "mirror" the API models

    # transformers 'standard' model loading
    from transformers import AutoTokenizer, AutoModelForCausalLM
    custom_hf_model = AutoModelForCausalLM.from_pretrained(model_name)
    hf_tokenizer = AutoTokenizer.from_pretrained(model_name)

    # + two lines of llmware code to instantiate the model in the prompt
    model = ModelCatalog().load_hf_generative_model(custom_hf_model, hf_tokenizer,instruction_following=False, prompt_wrapper="human_bot")
    prompter = Prompt(llm_model=model, llm_name=model_name,from_hf=True)

    # *** HF Model - "NEW WAY" ***  as a result of the change to streamline
    # ... one-line - exactly the same as OpenAI or Anthropic, but with optional "from_hf" flag set to True
    prompter = Prompt().load_model(model_name, from_hf=True)

    # this enables some nice scenarios to 'swap in/out' a HF model in a RAG workflow with minimal changes

    # example models from HF to try
    model_list = ["llmware/bling-1b-0.1",
                  "llmware/bling-1.4b-0.1",
                  "llmware/bling-falcon-1b-0.1",
                  "llmware/bling-sheared-llama-2.7b-0.1",
                  "llmware/bling-sheared-llama-1.3b-0.1",
                  "llmware/bling-red-pajamas-3b-0.1"]

    return 0

