import os
import json
import logging
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Setup logging
logging.basicConfig(
    format='[%(asctime)s] p%(process)s {%(filename)s:%(lineno)d} %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Verify API key is set
if os.getenv("GROQ_API_KEY"):
    logger.info("GROQ_API_KEY is set")
elif os.getenv("OPENAI_API_KEY"):
    logger.info("OPENAI_API_KEY is set")
elif os.getenv("ANTHROPIC_API_KEY"):
    logger.info("ANTHROPIC_API_KEY is set")
else:
    logger.warning("No API key found! Please set GROQ_API_KEY in your .env file")

# Check for Cohere API key (needed for re-ranking)
if os.getenv("COHERE_API_KEY"):
    logger.info("COHERE_API_KEY is set (for re-ranking)")
else:
    logger.warning("COHERE_API_KEY not set - re-ranking section will not work")

from langchain_community.chat_models import ChatLiteLLM

# Configure the LLM - using Groq's free Llama model
# You can change this to other models like:
# - "groq/llama-3.3-70b-versatile" (larger, FREE)
# - "gpt-4o-mini" (OpenAI, paid)
# - "claude-3-5-haiku-20241022" (Anthropic, paid)

MODEL_ID = "groq/llama-3.1-8b-instant"

llm = ChatLiteLLM(
    model=MODEL_ID,
    temperature=0
)
logger.info(f"Using model: {MODEL_ID}")

from langchain_community.embeddings import HuggingFaceEmbeddings

# Using a free, local embedding model
embeddings_model = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)
logger.info("Embeddings model loaded successfully")