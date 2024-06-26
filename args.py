import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Command line argument parser")

    parser.add_argument(
        "--config",
        type=str,
        help="json配置文件输入",
        default="configs/config_holo.json",
    )
    parser.add_argument(
        "--prompt_engineering",
        type=str,
        help="prompt模板类型",
        choices=["general", "extract_url", "accurate_content"],
        default="simple",
    )
    parser.add_argument(
        "--embed_model",
        type=str,
        help="embedding模型名称",
        choices=[
            "bge-large-zh-v1.5",
            "SGPT-125M-weightedmean-nli-bitfit",
            "text2vec-large-chinese",
            "text2vec-base-chinese",
            "paraphrase-multilingual-MiniLM-L12-v2",
        ],
        default="bge-large-zh-v1.5",
    )
    parser.add_argument(
        "--vectordb_type",
        type=str,
        help="向量知识库类型",
        choices=["AnalyticDB", "Hologres", "ElasticSearch", "OpenSearch", "FAISS"],
        default="FAISS",
    )
    parser.add_argument("--embed_dim", type=int, help="embedding向量维度", default=1024)
    parser.add_argument(
        "--upload", action="store_true", help="上传知识库", default=False
    )
    parser.add_argument("--user_query", type=str, help="用户查询请求内容")
    parser.add_argument(
        "--query_type",
        type=str,
        help="所请求模型的类型",
        choices=["retrieval_llm", "only_llm", "only_vectorstore"],
        default="retrieval_llm",
    )
    parser.add_argument("--port", type=int, default=8000)
    parser.add_argument(
        "--log-level",
        type=str.upper,
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
        help="Minimum log level to print.",
    )
    return parser.parse_args()