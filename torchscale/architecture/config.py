# Copyright (c) 2022 Microsoft
# Licensed under The MIT License [see LICENSE for details]

from dataclasses import dataclass, field
class EncoderConfig(object):
    def __init__(self, **kwargs):
        self.encoder_embed_dim = kwargs.pop("encoder_embed_dim", 768)
        self.encoder_attention_heads = kwargs.pop("encoder_attention_heads", 12)
        self.encoder_ffn_embed_dim = kwargs.pop("encoder_ffn_embed_dim", 3072)
        self.encoder_layers = kwargs.pop("encoder_layers", 12)
        self.encoder_normalize_before = kwargs.pop("encoder_normalize_before", True)
        self.normalize_output = kwargs.pop("normalize_output", True)
        self.activation_fn = kwargs.pop("activation_fn", "gelu")
        self.dropout = kwargs.pop("dropout", 0.0)
        self.drop_path_rate = kwargs.pop("drop_path_rate", 0.0)
        self.attention_dropout = kwargs.pop("attention_dropout", 0.0)
        self.activation_dropout = kwargs.pop("activation_dropout", 0.0)
        self.no_scale_embedding = kwargs.pop("no_scale_embedding", True)
        self.layernorm_embedding = kwargs.pop("layernorm_embedding", False)
        self.moe_freq = kwargs.pop("moe_freq", 0)
        self.moe_top1_expert = kwargs.pop("moe_top1_expert", False)
        self.moe_expert_count = kwargs.pop("moe_expert_count", 0)
        self.moe_gating_use_fp32 = kwargs.pop("moe_gating_use_fp32", True)
        self.moe_eval_capacity_token_fraction = kwargs.pop(
            "moe_eval_capacity_token_fraction", 0.25
        )
        self.moe_second_expert_policy = kwargs.pop("moe_second_expert_policy", "random")
        self.moe_normalize_gate_prob_before_dropping = kwargs.pop(
            "moe_normalize_gate_prob_before_dropping", False
        )
        self.use_xmoe = kwargs.pop("use_xmoe", False)
        self.rel_pos_buckets = kwargs.pop("rel_pos_buckets", 0)
        self.max_rel_pos = kwargs.pop("max_rel_pos", 0)
        self.deepnorm = kwargs.pop("deepnorm", False)
        self.subln = kwargs.pop("subln", True)
        self.bert_init = kwargs.pop("bert_init", False)
        self.multiway = kwargs.pop("multiway", False)
        self.share_encoder_input_output_embed = kwargs.pop(
            "share_encoder_input_output_embed", False
        )
        self.max_source_positions = kwargs.pop("max_source_positions", 1024)
        self.no_output_layer = kwargs.pop("no_output_layer", False)
        self.layernorm_eps = kwargs.pop("layernorm_eps", 1e-5)
        # Text
        self.vocab_size = kwargs.pop("vocab_size", -1)
        # Vision
        self.img_size = kwargs.pop("img_size", 224)
        self.patch_size = kwargs.pop("patch_size", 16)
        self.in_chans = kwargs.pop("in_chans", 3)
        # Fairscale
        self.checkpoint_activations = kwargs.pop("checkpoint_activations", False)
        self.fsdp = kwargs.pop("fsdp", False)
        self.ddp_rank = kwargs.pop("ddp_rank", 0)
        self.xpos_rel_pos = kwargs.pop("xpos_rel_pos", False)
        self.xpos_scale_base = kwargs.pop("xpos_scale_base", 512)

        if self.deepnorm:
            self.encoder_normalize_before = False
            self.subln = False
        if self.subln:
            self.encoder_normalize_before = True
            self.deepnorm = False
        if self.use_xmoe:
            self.moe_normalize_gate_prob_before_dropping = True
            self.moe_second_expert_policy = "random"
            assert self.moe_freq > 0 and self.moe_expert_count > 0

    def override(self, args):
        for hp in self.__dict__.keys():
            if getattr(args, hp, None) is not None:
                self.__dict__[hp] = getattr(args, hp, None)


class DecoderConfig(object):
    def __init__(self, **kwargs):
        self.decoder_embed_dim = kwargs.pop("decoder_embed_dim", 768)
        self.decoder_attention_heads = kwargs.pop("decoder_attention_heads", 12)
        self.decoder_ffn_embed_dim = kwargs.pop("decoder_ffn_embed_dim", 3072)
        self.decoder_layers = kwargs.pop("decoder_layers", 12)
        self.decoder_normalize_before = kwargs.pop("decoder_normalize_before", True)
        self.activation_fn = kwargs.pop("activation_fn", "gelu")
        self.dropout = kwargs.pop("dropout", 0.0)
        self.drop_path_rate = kwargs.pop("drop_path_rate", 0.0)
        self.attention_dropout = kwargs.pop("attention_dropout", 0.0)
        self.activation_dropout = kwargs.pop("activation_dropout", 0.0)
        self.no_scale_embedding = kwargs.pop("no_scale_embedding", True)
        self.layernorm_embedding = kwargs.pop("layernorm_embedding", False)
        self.moe_freq = kwargs.pop("moe_freq", 0)
        self.moe_top1_expert = kwargs.pop("moe_top1_expert", False)
        self.moe_expert_count = kwargs.pop("moe_expert_count", 0)
        self.moe_gating_use_fp32 = kwargs.pop("moe_gating_use_fp32", True)
        self.moe_eval_capacity_token_fraction = kwargs.pop(
            "moe_eval_capacity_token_fraction", 0.25
        )
        self.moe_second_expert_policy = kwargs.pop("moe_second_expert_policy", "random")
        self.moe_normalize_gate_prob_before_dropping = kwargs.pop(
            "moe_normalize_gate_prob_before_dropping", False
        )
        self.use_xmoe = kwargs.pop("use_xmoe", False)
        self.rel_pos_buckets = kwargs.pop("rel_pos_buckets", 0)
        self.max_rel_pos = kwargs.pop("max_rel_pos", 0)
        self.deepnorm = kwargs.pop("deepnorm", False)
        self.subln = kwargs.pop("subln", True)
        self.bert_init = kwargs.pop("bert_init", False)
        self.multiway = kwargs.pop("multiway", False)
        self.share_decoder_input_output_embed = kwargs.pop(
            "share_decoder_input_output_embed", False
        )
        self.max_target_positions = kwargs.pop("max_target_positions", 1024)
        self.no_output_layer = kwargs.pop("no_output_layer", False)
        self.layernorm_eps = kwargs.pop("layernorm_eps", 1e-5)
        # Text
        self.vocab_size = kwargs.pop("vocab_size", -1)
        # Fairscale
        self.checkpoint_activations = kwargs.pop("checkpoint_activations", False)
        self.fsdp = kwargs.pop("fsdp", False)
        self.ddp_rank = kwargs.pop("ddp_rank", 0)
        self.xpos_rel_pos = kwargs.pop("xpos_rel_pos", False)
        self.xpos_scale_base = kwargs.pop("xpos_scale_base", 512)

        if self.deepnorm:
            self.decoder_normalize_before = False
            self.subln = False
        if self.subln:
            self.decoder_normalize_before = True
            self.deepnorm = False
        if self.use_xmoe:
            self.moe_normalize_gate_prob_before_dropping = True
            self.moe_second_expert_policy = "random"
            assert self.moe_freq > 0 and self.moe_expert_count > 0

    def override(self, args):
        for hp in self.__dict__.keys():
            if getattr(args, hp, None) is not None:
                self.__dict__[hp] = getattr(args, hp, None)


class EncoderDecoderConfig(object):
    def __init__(self, **kwargs):
        self.encoder_embed_dim = kwargs.pop("encoder_embed_dim", 768)
        self.encoder_attention_heads = kwargs.pop("encoder_attention_heads", 12)
        self.encoder_ffn_embed_dim = kwargs.pop("encoder_ffn_embed_dim", 3072)
        self.encoder_layers = kwargs.pop("encoder_layers", 12)
        self.encoder_normalize_before = kwargs.pop("encoder_normalize_before", True)
        self.normalize_output = kwargs.pop("normalize_output", True)
        self.decoder_embed_dim = kwargs.pop("decoder_embed_dim", 768)
        self.decoder_attention_heads = kwargs.pop("decoder_attention_heads", 12)
        self.decoder_ffn_embed_dim = kwargs.pop("decoder_ffn_embed_dim", 3072)
        self.decoder_layers = kwargs.pop("decoder_layers", 12)
        self.decoder_normalize_before = kwargs.pop("decoder_normalize_before", True)
        self.activation_fn = kwargs.pop("activation_fn", "gelu")
        self.dropout = kwargs.pop("dropout", 0.0)
        self.drop_path_rate = kwargs.pop("drop_path_rate", 0.0)
        self.attention_dropout = kwargs.pop("attention_dropout", 0.0)
        self.activation_dropout = kwargs.pop("activation_dropout", 0.0)
        self.no_scale_embedding = kwargs.pop("no_scale_embedding", True)
        self.layernorm_embedding = kwargs.pop("layernorm_embedding", False)
        self.moe_freq = kwargs.pop("moe_freq", 0)
        self.moe_top1_expert = kwargs.pop("moe_top1_expert", False)
        self.moe_expert_count = kwargs.pop("moe_expert_count", 0)
        self.moe_gating_use_fp32 = kwargs.pop("moe_gating_use_fp32", True)
        self.moe_eval_capacity_token_fraction = kwargs.pop(
            "moe_eval_capacity_token_fraction", 0.25
        )
        self.moe_second_expert_policy = kwargs.pop("moe_second_expert_policy", "random")
        self.moe_normalize_gate_prob_before_dropping = kwargs.pop(
            "moe_normalize_gate_prob_before_dropping", False
        )
        self.use_xmoe = kwargs.pop("use_xmoe", False)
        self.rel_pos_buckets = kwargs.pop("rel_pos_buckets", 0)
        self.max_rel_pos = kwargs.pop("max_rel_pos", 0)
        self.deepnorm = kwargs.pop("deepnorm", False)
        self.subln = kwargs.pop("subln", True)
        self.bert_init = kwargs.pop("bert_init", False)
        self.multiway = kwargs.pop("multiway", False)
        self.share_all_embeddings = kwargs.pop("share_all_embeddings", False)
        self.share_decoder_input_output_embed = kwargs.pop(
            "share_decoder_input_output_embed", False
        )
        self.max_source_positions = kwargs.pop("max_source_positions", 1024)
        self.max_target_positions = kwargs.pop("max_target_positions", 1024)
        self.no_output_layer = kwargs.pop("no_output_layer", False)
        self.layernorm_eps = kwargs.pop("layernorm_eps", 1e-5)
        # Text
        self.vocab_size = kwargs.pop("vocab_size", -1)
        # Fairscale
        self.checkpoint_activations = kwargs.pop("checkpoint_activations", False)
        self.fsdp = kwargs.pop("fsdp", False)
        self.ddp_rank = kwargs.pop("ddp_rank", 0)
        self.xpos_rel_pos = kwargs.pop("xpos_rel_pos", False)
        self.xpos_scale_base = kwargs.pop("xpos_scale_base", 512)

        if self.deepnorm:
            self.encoder_normalize_before = False
            self.decoder_normalize_before = False
            self.subln = False
        if self.subln:
            self.encoder_normalize_before = True
            self.decoder_normalize_before = True
            self.deepnorm = False
        if self.use_xmoe:
            self.moe_normalize_gate_prob_before_dropping = True
            self.moe_second_expert_policy = "random"
            assert self.moe_freq > 0 and self.moe_expert_count > 0

    def override(self, args):
        for hp in self.__dict__.keys():
            if getattr(args, hp, None) is not None:
                self.__dict__[hp] = getattr(args, hp, None)
                
                
class RetNetConfig(object):
    def __init__(self, **kwargs):
        self.decoder_embed_dim = kwargs.pop("decoder_embed_dim", 768)
        self.decoder_retention_heads = kwargs.pop("decoder_retention_heads", 3)
        self.decoder_ffn_embed_dim = kwargs.pop("decoder_ffn_embed_dim", 1536)
        self.decoder_layers = kwargs.pop("decoder_layers", 12)
        self.decoder_normalize_before = kwargs.pop("decoder_normalize_before", True)
        self.activation_fn = kwargs.pop("activation_fn", "gelu")
        self.dropout = kwargs.pop("dropout", 0.0)
        self.drop_path_rate = kwargs.pop("drop_path_rate", 0.0)
        self.activation_dropout = kwargs.pop("activation_dropout", 0.0)
        self.no_scale_embedding = kwargs.pop("no_scale_embedding", True)
        self.layernorm_embedding = kwargs.pop("layernorm_embedding", False)
        self.moe_freq = kwargs.pop("moe_freq", 0)
        self.moe_top1_expert = kwargs.pop("moe_top1_expert", False)
        self.moe_expert_count = kwargs.pop("moe_expert_count", 0)
        self.moe_gating_use_fp32 = kwargs.pop("moe_gating_use_fp32", True)
        self.moe_eval_capacity_token_fraction = kwargs.pop(
            "moe_eval_capacity_token_fraction", 0.25
        )
        self.moe_second_expert_policy = kwargs.pop("moe_second_expert_policy", "random")
        self.moe_normalize_gate_prob_before_dropping = kwargs.pop(
            "moe_normalize_gate_prob_before_dropping", False
        )
        self.use_xmoe = kwargs.pop("use_xmoe", False)
        self.rel_pos_buckets = kwargs.pop("rel_pos_buckets", 0)
        self.max_rel_pos = kwargs.pop("max_rel_pos", 0)
        self.deepnorm = kwargs.pop("deepnorm", False)
        self.subln = kwargs.pop("subln", True)
        self.multiway = kwargs.pop("multiway", False)
        self.share_decoder_input_output_embed = kwargs.pop(
            "share_decoder_input_output_embed", False
        )
        self.max_target_positions = kwargs.pop("max_target_positions", 1024)
        self.no_output_layer = kwargs.pop("no_output_layer", False)
        self.layernorm_eps = kwargs.pop("layernorm_eps", 1e-5)
        # Blockwise
        self.chunkwise_recurrent = kwargs.pop("chunkwise_recurrent", False)
        self.recurrent_chunk_size = kwargs.pop("recurrent_chunk_size", 512)
        # Text
        self.vocab_size = kwargs.pop("vocab_size", -1)
        # Fairscale
        self.checkpoint_activations = kwargs.pop("checkpoint_activations", False)
        self.fsdp = kwargs.pop("fsdp", False)
        self.ddp_rank = kwargs.pop("ddp_rank", 0)
        self.xpos_rel_pos = kwargs.pop("xpos_rel_pos", False)
        self.xpos_scale_base = kwargs.pop("xpos_scale_base", 512)
        self.random_permute_times  = kwargs.pop("random_permute_times", None)

        if self.deepnorm:
            self.decoder_normalize_before = False
            self.subln = False
        if self.subln:
            self.decoder_normalize_before = True
            self.deepnorm = False
        if self.use_xmoe:
            self.moe_normalize_gate_prob_before_dropping = True
            self.moe_second_expert_policy = "random"
            assert self.moe_freq > 0 and self.moe_expert_count > 0

    def override(self, args):
        for hp in self.__dict__.keys():
            if getattr(args, hp, None) is not None:
                self.__dict__[hp] = getattr(args, hp, None)


@dataclass
class RetNetConfigDataclass(object):
    decoder_embed_dim: int = field(default=768)
    decoder_retention_heads: int = field(default=3)
    decoder_ffn_embed_dim: int = field(default=1536)
    decoder_layers: int = field(default=12)
    decoder_normalize_before: bool = field(default=True)
    activation_fn: str = field(default="gelu")
    dropout: float = field(default=0.0)
    drop_path_rate: float = field(default=0.0)
    activation_dropout: float = field(default=0.0)
    no_scale_embedding: bool = field(default=True)
    layernorm_embedding: bool = field(default=False)
    moe_freq: int = field(default=0)
    moe_top1_expert: bool = field(default=False)
    moe_expert_count: int = field(default=0)
    moe_gating_use_fp32: bool = field(default=True)
    moe_eval_capacity_token_fraction: float = field(default=0.25)
    moe_second_expert_policy: str = field(default="random")
    moe_normalize_gate_prob_before_dropping: bool = field(default=False)
    use_xmoe: bool = field(default=False)
    rel_pos_buckets: int = field(default=0)
    max_rel_pos: int = field(default=0)
    deepnorm: bool = field(default=False)
    subln: bool = field(default=True)
    multiway: bool = field(default=False)
    share_decoder_input_output_embed: bool = field(default=False)
    max_target_positions: int = field(default=1024)
    no_output_layer: bool = field(default=False)
    layernorm_eps: float = field(default=1e-5)
    chunkwise_recurrent: bool = field(default=False)
    recurrent_chunk_size: int = field(default=512)
    vocab_size: int = field(default=-1)
    checkpoint_activations: bool = field(default=False)
    fsdp: bool = field(default=False)
    ddp_rank: int = field(default=0)
    xpos_rel_pos: bool = field(default=False)
    xpos_scale_base: int = field(default=512)
    random_permute_times: int = field(default=None)

    def __post_init__(self):
        if self.deepnorm:
            self.decoder_normalize_before = False
            self.subln = False
        if self.subln:
            self.decoder_normalize_before = True
            self.deepnorm = False
        if self.use_xmoe:
            self.moe_normalize_gate_prob_before_dropping = True
            self.moe_second_expert_policy = "random"
            assert self.moe_freq > 0 and self.moe_expert_count > 0

    def override(self, args):
        for hp in self.__dict__.keys():
            if getattr(args, hp, None) is not None:
                self.__dict__[hp] = getattr(args, hp, None)

